import smbus2
import time

# Register addresses
ADXL345_ADDR = 0x53
POWER_CTL = 0x2D
DATAX0 = 0x32

bus = smbus2.SMBus(1)  # 1 indicates /dev/i2c-1

def init_adxl345():
    # Wake up the ADXL345
    bus.write_byte_data(ADXL345_ADDR, POWER_CTL, 0x08)

def read_axes():
    # Read 6 bytes from DATAX0 to DATAZ1
    data = bus.read_i2c_block_data(ADXL345_ADDR, DATAX0, 6)

    # Convert the data to 10-bit signed values
    x = int.from_bytes(data[0:2], byteorder='little', signed=True)
    y = int.from_bytes(data[2:4], byteorder='little', signed=True)
    z = int.from_bytes(data[4:6], byteorder='little', signed=True)

    return x, y, z

if __name__ == "__main__":
    init_adxl345()
    print("ADXL345 initialized. Reading values...")
    while True:
        x, y, z = read_axes()
        print(f"X={x} Y={y} Z={z}")
        time.sleep(0.5)
