import network
import esp
import gc
import urequests
import time
import random

esp.osdebug(None)

ssid = 'AcáESP32'
wifipassword = '12345678'

def conexion():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, wifipassword)
    print("Conectando")
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print("")
    print("Conectado a Internet: ", sta_if.ifconfig())

FLASK_SERVER_IP = "192.168.0.12" #IP DEL SV
FLASK_SERVER_PORT = 5050 #PUERTO

Flask = [
    "/"
    "/secret"
    "/time"
    "/error"
    ]

USERNAME = "Estudiantes"
PASSWORD = "educar_2018"

conexion()

try:
    while True:
        random_path = random.choice(PATHS)
        url = "https://{}:{}{}".format(FLASK_SERVER_IP, FLASK_SERVER_PORT, random_path)
        print("\nConsultando: ", url)
        
        try:
            if random_path == "/secret":
                response = urequest.get(url auth =(USERNAME, PASSWORD.SECRET))
            else:
                responde = urequest.get(url)
            print("Codigo de estado HTTP: ",  response.status_code)
            print("Respuesta:")
            print(response.text)
            response.close
        except Exception as e:
            print("Error al realizar la consulta HTTP: ", e)
            time.sleep(1)
except KeyboardInterrupt:
    print("Programa detenido por el usuario")
except Exception as e:
    print("Se produjo un error inesperado: ", e)
finally:
    print("Desconectando Wi-Fi")
    network.WLAN(network.STA_IF).disconect()
    network.Wlan(newtwork.STA_IF).active(False)
    print("WIFi desconectado")