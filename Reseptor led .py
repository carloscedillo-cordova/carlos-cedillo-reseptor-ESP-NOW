import network
import espnow
import machine
import time

# Inicializa la interfaz WLAN
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Inicializa ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Configuración del pin del LED
led_pin = machine.Pin(2, machine.Pin.OUT)

# Esperar un momento para asegurar que ESP-NOW está activo
time.sleep(1)

print("Esperando mensajes...")

while True:
    # Esperar por mensajes recibidos
    try:
        sender, msg = esp.recv()
        if msg:
            if msg == b'ledOn':
                print("Encendiendo LED")
                led_pin.on()
            elif msg == b'ledOff':
                print("Apagando LED")
                led_pin.off()
            else:
                print(f"Mensaje desconocido: {msg}")
    except OSError:
        # Ignorar errores de tiempo de espera
        pass

