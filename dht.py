import time
import board
import adafruit_dht

# Set up DHT22 on GPIO4
dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temp: {temperature:.1f} C  Humidity: {humidity:.1f}%")
    except RuntimeError as error:
        print(f"Error: {error.args[0]}")
        time.sleep(2.0)
        continue
    time.sleep(2.0)
