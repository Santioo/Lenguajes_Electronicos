from machine import Pin
from utime import sleep

import time
from machine import Pin

from umqtt.simple import MQTTClient
import network


# Definiciones
ssid = 'AcáESP32'
wifipassword = '12345678'
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
# ----


# Conexión a los tópicos
mqtt_server = "io.adafruit.com"
port = 1883
user = "Santio0o"
password = "aio_eSdJ57apDS3NfUMv9gsipqHvxsZK"
client_id_gauge = "Identificador"
topico_lectura="Santio0o/feeds/Lectura"


# Conexión al broker
try:
   conexionMQTT = MQTTClient(client_id_gauge, mqtt_server,user=user,password=password,port=int(port))
   conexionMQTT.connect() #Hacemos la conexión.
   print("Conectado con Broker MQTT")
except OSError as e:
   #Si falló la conexión, reiniciamos todo
   print("Fallo la conexion al Broker, reiniciando...")
   time.sleep(5)
   machine.reset()


# Funciones
def enviar_msg(msg):
   try:
       conexionMQTT.publish(topico_lectura,str(msg))
       print(f'Mensaje enviado con exito: {msg}')
   except OSError as e:
       print("Error ",e)
       time.sleep(5)
       machine.reset()
# ----

print("Sistema Inicializado...")

pin_a = Pin(23, Pin.OUT)
pin_b = Pin(27, Pin.OUT)
pin_c = Pin(15, Pin.OUT)
pin_d = Pin(18, Pin.OUT)
pin_e = Pin(19, Pin.OUT)
pin_f = Pin(21, Pin.OUT)
pin_g = Pin(22, Pin.OUT)

def mostrar_digito(digito_hex):
    if digito_hex == 0:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(0)
    elif digito_hex == 1:
        pin_a.value(0)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(0)
        pin_e.value(0)
        pin_f.value(0)
        pin_g.value(0)
    elif digito_hex == 2:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(0)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(0)
        pin_g.value(1)
    elif digito_hex == 3:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(0)
        pin_f.value(0)
        pin_g.value(1)
    elif digito_hex == 4:
        pin_a.value(0)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(0)
        pin_e.value(0)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 5:
        pin_a.value(1)
        pin_b.value(0)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(0)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 6:
        pin_a.value(1)
        pin_b.value(0)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 7:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(0)
        pin_e.value(0)
        pin_f.value(0)
        pin_g.value(0)
    elif digito_hex == 8:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 9:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(0)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 10:
        pin_a.value(1)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(0)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 11:
        pin_a.value(0)
        pin_b.value(0)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 12:
        pin_a.value(1)
        pin_b.value(0)
        pin_c.value(0)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(0)
    elif digito_hex == 13:
        pin_a.value(0)
        pin_b.value(1)
        pin_c.value(1)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(0)
        pin_g.value(1)
    elif digito_hex == 14:
        pin_a.value(1)
        pin_b.value(0)
        pin_c.value(0)
        pin_d.value(1)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    elif digito_hex == 15:
        pin_a.value(1)
        pin_b.value(0)
        pin_c.value(0)
        pin_d.value(0)
        pin_e.value(1)
        pin_f.value(1)
        pin_g.value(1)
    else:
        print("Dígito hexadecimal no válido:", digito_hex)



boton_1 = Pin(14, Pin.IN, Pin.PULL_UP)
boton_3 = Pin(12, Pin.IN, Pin.PULL_UP)
boton_2 = Pin(13, Pin.IN, Pin.PULL_UP)

contador = 0
turno = 0

mostrar_digito(0)

while True:
    estado_1 = boton_1.value()
    estado_3 = boton_3.value()
    estado_2 = boton_2.value()

    if estado_1 == 0:
        contador = contador + 1
        if contador > 15:
            contador = contador - 15
        elif contador < 0:
            contador = contador + 15
        mostrar_digito(contador)
        print(contador)
        enviar_msg(contador)
        time.sleep(1)
    elif estado_3 == 0:
        contador = contador - 3
        if contador >= 15:
            contador = contador - 15
        elif contador <= 0:
            contador = contador + 15
        mostrar_digito(contador)
        print(contador)
        enviar_msg(contador)
        time.sleep(1)
    elif estado_2 == 0:
        contador = contador * 2
        if contador >= 15:
            contador = contador - 15
        elif contador <= 0:
            contador = contador + 15
        mostrar_digito(contador)
        print(contador)
        enviar_msg(contador)
        time.sleep(1)

    if contador >= 15:
        contador = 15
    elif contador <= 0:
        contador = 0


