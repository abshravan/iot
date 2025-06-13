import time
import board
import adafruit_dht
import tkinter as tk
from threading import Thread

# Initialize DHT22 sensor on GPIO4
dht_device = adafruit_dht.DHT22(board.D4)

# GUI Setup
root = tk.Tk()
root.title("DHT22 Temperature & Humidity Monitor")
root.geometry("300x150")
root.resizable(False, False)

temperature_label = tk.Label(root, text="Temp: -- °C", font=("Arial", 16))
temperature_label.pack(pady=10)

humidity_label = tk.Label(root, text="Humidity: -- %", font=("Arial", 16))
humidity_label.pack(pady=10)

status_label = tk.Label(root, text="Status: Initializing...", fg="blue")
status_label.pack()

# Update function
def update_readings():
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            temperature_label.config(text=f"Temp: {temperature:.1f} °C")
            humidity_label.config(text=f"Humidity: {humidity:.1f} %")
            status_label.config(text="Status: OK", fg="green")
        except RuntimeError as e:
            status_label.config(text=f"Error: {e.args[0]}", fg="red")
        time.sleep(2)

# Run the sensor read loop in a separate thread
thread = Thread(target=update_readings, daemon=True)
thread.start()

# Start GUI event loop
root.mainloop()
