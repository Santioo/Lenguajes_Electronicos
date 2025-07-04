import machine
import time
from umqtt.simple import MQTTClient
import network

# Definiciones
ssid = 'Wokwi-GUEST'
wifipassword = ''
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Conexión a internet
sta_if.connect(ssid, wifipassword)
print("Conectando")
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print("")
print("Conectado a Internet")

# Conexión a los tópicos
mqtt_server = "io.adafruit.com"
port = 1883
user = "Santio0o"
password = "aio_eSdJ57apDS3NfUMv9gsipqHvxsZK"
client_id_gauge = "Identificador"
topico_distancia = "Santio0o/feeds/distancia"
topico_estado = "Santio0o/feeds/estado"
topico_sonando = "Santio0o/feeds/sonando"

# Conexión al broker
try:
    conexionMQTT = MQTTClient(client_id_gauge, mqtt_server, user=user, password=password, port=int(port))
    conexionMQTT.connect()
    print("Conectado con Broker MQTT")
except OSError as e:
    print("Fallo la conexion al Broker, reiniciando...")
    time.sleep(5)
    machine.reset()

# Funciones
def enviar_msg(topico, msg):
    try:
        conexionMQTT.publish(topico, str(msg))
        print(f'Mensaje enviado con exito al tópico {topico}: {msg}')
    except OSError as e:
        print("Error ", e)
        time.sleep(5)
        machine.reset()


print("Sistema Inicializado...")

TRIG = machine.Pin(5, machine.Pin.OUT)  #Pin para el trigger del ultrasonido
ECHO = machine.Pin(18, machine.Pin.IN)  #Pin para el echo del ultrasonido
BUZZER = machine.Pin(15, machine.Pin.OUT)  #Pin para el buzzer
BOTON = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  #Pin para el botón
LED_ESTADO = machine.Pin(2, machine.Pin.OUT)  #LED que muestra si la alarma está encendida
LED_SONANDO = machine.Pin(19, machine.Pin.OUT)  #LED que parpadea si el buzzer suena

alarma_encendida = False
distancia_maxima = 50  #Distancia a la que se activa la alarma
ultimo_estado_boton = 1  #Para detecctar los ambio en el botón
ultimo_estado_enviado = "Apagada"  #Para rastrear cambios en el estado
ultimo_sonando_enviado = "NO"  #Para rastrear cambios en el estado del buzzer

enviar_msg(topico_distancia, distancia_maxima)
enviar_msg(topico_estado, "Apagada")
enviar_msg(topico_sonando, "NO")

def medir_distancia():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1) #Enviamos un pulso de 10 microsegundos
    time.sleep_us(10)
    TRIG.value(0)

    while ECHO.value() == 0: #Esperamos a que el pin echo se ponga en alto
        pass
    inicio = time.ticks_us()  #Guardamos el tiermpo inicial
    while ECHO.value() == 1: #Esperamos a que el pin echo se ponga en bajo
        pass
    fin = time.ticks_us()  #Guardamos el tiempo final
    duracion = time.ticks_diff(fin, inicio)
    distancia = (duracion * 0.034) / 2 
    return distancia

while True:
    estado_boton = BOTON.value() #leemos el estado del boton
    
    if estado_boton == 0 and ultimo_estado_boton == 1: #Nos fijamos si el boton fue presionado
        alarma_encendida = not alarma_encendida  #cambiamos el estado de la alarma
        LED_ESTADO.value(alarma_encendida)
        estado_texto = "Encendida" if alarma_encendida else "Apagada"
        if estado_texto != ultimo_estado_enviado:
            enviar_msg(topico_estado, estado_texto)
            ultimo_estado_enviado = estado_texto

        BUZZER.value(0)
        LED_SONANDO.value(0)
        if ultimo_sonando_enviado != "NO":
            enviar_msg(topico_sonando, "NO")
            ultimo_sonando_enviado = "NO"
        time.sleep(0.2)  #antirebote
    
    ultimo_estado_boton = estado_boton  #guardamos el último estado del botón
    
    if alarma_encendida: #si la alarma está encendidad
        distancia = medir_distancia()

        if distancia < distancia_maxima: #si distancia es menor activa la alrma
            BUZZER.value(1)
            LED_SONANDO.value(1)

            if ultimo_sonando_enviado != "SONANDO":
                enviar_msg(topico_sonando, "SONANDO")
                ultimo_sonando_enviado = "SONANDO"

            time.sleep(0.5)
            BUZZER.value(0)
            LED_SONANDO.value(0)
            time.sleep(0.5)
        else: #En caso de que no apaga todo
            BUZZER.value(0)
            LED_SONANDO.value(0)

            if ultimo_sonando_enviado != "NO":
                enviar_msg(topico_sonando, "NO")
                ultimo_sonando_enviado = "NO"
    else:
        BUZZER.value(0)  
        LED_SONANDO.value(0) 

        if ultimo_estado_enviado != "Apagada":
            enviar_msg(topico_estado, "Apagada")
            ultimo_estado_enviado = "Apagada"

        if ultimo_sonando_enviado != "NO":
            enviar_msg(topico_sonando, "NO")
            ultimo_sonando_enviado = "NO"

    time.sleep(0.1)
