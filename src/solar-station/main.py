import time
import board
import busio
import adafruit_bme680
import sys


# Attempts at printing out sensor data.
NUM_ATTEMPTS: int = 0
MAX_ATTEMPTS: int = 30

# Set up I2C connection. 
i2c = busio.I2C(board.SCL, board.SDA) 
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Local sea level pressure in hPa.
# Used for getting an accurate altitude. 
bme680.sea_level_pressure = 1013.25

def main() -> int:
	print("Running solar station...")
	
	while NUM_ATTEMPTS < MAX_ATTEMPTS:
		print(f"\nTemperature: {bme680.temperature:0.1f} C")
		print(f"Gas: {bme680.gas:d} ohm")
		print(f"Humidity: {bme680.relative_humidity:0.1f} %")
		print(f"Pressure: {bme680.pressure:0.3f} hPa")
		print(f"Altitude: {bme680.altitude:0.2f} meters")
		
		NUM_ATTEMPTS+=1
	
		time.sleep(1)
	
	return 0


if __name__ == "__main__":
	sys.exit(main())
