import machine
import time
import network
import urequests
import ujson

TRIG_PIN = 5
ECHO_PIN = 4
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

FLASK_SERVER_IP = "127.0.0.1"
FLASK_PORT = 5000
SET_ZOOM_PATH = "/set_zoom"

def medir_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1) #Enviamos un pulso de 10 microsegundos
    time.sleep_us(10)
    trig.value(0)

    while echo.value() == 0: #Esperamos a que el pin echo se ponga en alto
        pass
    inicio = time.ticks_us()  #Guardamos el tiermpo inicial
    while echo.value() == 1: #Esperamos a que el pin echo se ponga en bajo
        pass
    fin = time.ticks_us()  #Guardamos el tiempo final
    duracion = time.ticks_diff(fin, inicio)
    distancia = (duracion * 0.034) / 2 
    return distancia

ssid = "AcáESP32"
wifipassword = "12345678"
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

while True:
    distancia = medir_distancia()
    
    if distancia > 0:
        zoom_value = max(0, min(int(distancia), 100))
        
        try:
            url = f"http://{FLASK_SERVER_IP}:{FLASK_PORT}{SET_ZOOM_PATH}?value={zoom_value}"
            response = urequests.get(url)
            print(f"Respuesta del servidor: {response.text}")
            response.close()
        except Exception as e:
            print(f"Error al enviar datos al servidor Flask: {e}")
    else:
        print("Fuera de rango o no se detectó eco.")
    time.sleep(1)