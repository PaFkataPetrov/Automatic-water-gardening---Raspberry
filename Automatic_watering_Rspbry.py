import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the humidity sensor and water pump
humidity_sensor_pin = 14
water_pump_pin = 15

# Set the GPIO pins to input/output mode
GPIO.setup(humidity_sensor_pin, GPIO.IN)
GPIO.setup(water_pump_pin, GPIO.OUT)

# Define the minimum humidity level for watering (adjust as needed)
min_humidity = 30

# Define the watering time in seconds (adjust as needed)
watering_time = 5

try:
    while True:
        # Read the humidity sensor value
        humidity = GPIO.input(humidity_sensor_pin)

        if humidity < min_humidity:
            # If the humidity is below the minimum threshold, turn on the water pump
            GPIO.output(water_pump_pin, GPIO.HIGH)
            print("Watering the garden...")
            time.sleep(watering_time)
            GPIO.output(water_pump_pin, GPIO.LOW)
            print("Done watering.")

        # Wait for a few seconds before checking the humidity again
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
