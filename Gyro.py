from mpu6050 import mpu6050 
import time

# Create a new Mpu6050 object
gyro = mpu6050(address=0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    accelerometer_data = gyro.get_accel_data()

    # Read the gyroscope values
    gyroscope_data = gyro.get_gyro_data()

    # Read temp
    temperature = gyro.get_temp()

    return accelerometer_data, gyroscope_data, temperature

# Start a while loop to continuously read the sensor data
while True:

    # Read the sensor data
    accelerometer_data, gyroscope_data, temperature = read_sensor_data()

    # Print the sensor data
    print("Accelerometer data:", accelerometer_data)
    print("Gyroscope data:", gyroscope_data)
    print("Temp:", temperature)

    # Wait for 1 second
    time.sleep(1)