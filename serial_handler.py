import serial

# Define the COM port and baud rate
com_port = 'COM13'
baud_rate = 9600

# Open the serial port
ser = serial.Serial(com_port, baud_rate, timeout=1)

# Specify the file to save the data
file_path = 'received_data.txt'

try:
    # Open the file for writing
    with open(file_path, 'w') as file:
        while True:
            # Read a line from the serial port
            data = ser.readline().decode('utf-8').strip()

            # Print the received data
            print(data)

            # Write the data to the file
            file.write(data + '\n')

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Program terminated by user.")

finally:
    # Close the serial port
    ser.close()
