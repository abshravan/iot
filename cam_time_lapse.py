import time
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

for i in range(10):
    picam2.capture_file(f"image_{i}.jpg")
    time.sleep(5)  # capture every 5 seconds
