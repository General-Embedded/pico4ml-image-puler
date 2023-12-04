from PIL import Image
import serial
import struct
import datetime
from datetime import datetime
import os

# Start datetime for folder creation
current_datetime = datetime.now()
hourminute = current_datetime.strftime("%H_%M")

# Create the folder
os.makedirs(hourminute, exist_ok=True)

# Define the COM port and baud rate
com_port = 'COM13'
baud_rate = 9600

# Open the serial port
ser = serial.Serial(com_port, baud_rate, timeout=1)

# Specify the file to save the data
file_path = 'received_data.txt'

def create_bmp_from_string(input_string, width, height, output_file):
    # Assuming the input string contains signed integers separated by spaces
    pixel_values = list(map(int, input_string.split()))

    # Check if the number of pixels matches the expected size
    if len(pixel_values) != width * height:
        raise ValueError("Invalid number of pixels in the input string.")

    # Normalize pixel values to the range [0, 255]
    normalized_pixels = [pixel + 128 for pixel in pixel_values]

    # Create a new image with the specified size
    image = Image.new("L", (width, height))

    # Put the normalized pixel values into the image
    image.putdata(normalized_pixels)

    # Save the image in BMP format
    image.save(output_file, "BMP")

if __name__ == "__main__":
    try:
    # Open the file for writing
        with open(file_path, 'w') as file:
            while True:
                # Read a line from the serial port
                data = ser.readline().decode('utf-8').strip()
                spaces = data.count(" ")
                if spaces == 9215:
                        
                    # Print the received data
                    print(data.count(" "))
                    print(" ^spaces, newlines V")
                    print(data.count("\n"))
                    # Write the data to the file
                    file.write(data + '\n')
                    # Example input string (replace this with your actual input string)
                    input_string = data
                    # Specify the size of the image
                    image_width = 96
                    image_height = 96

                    #give each generated file a unique, date-based filename
                    # Get the current date and time
                    current_datetime = datetime.now()

                    # Format the datetime string with hour underscored
                    formatted_datetime = current_datetime.strftime("%H_%M_%S")

                    
                    # Specify the output BMP file
                    output_bmp_file = hourminute +"/p_"+formatted_datetime+".bmp"
                    print(output_bmp_file)

                    # Create BMP from the input string
                    create_bmp_from_string(input_string, image_width, image_height, output_bmp_file)

                    print(f"BMP image saved to {output_bmp_file}")
    except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
        print("Program terminated by user.")

    finally:
        # Close the serial port
        ser.close()
                