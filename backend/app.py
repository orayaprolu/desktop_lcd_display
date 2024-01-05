from flask import Flask, request, send_file
import requests
from PIL import Image

# all the routes are stuff that should be called by the frontend

app = Flask(__name__)

esp32_ip = '192.168.254.150'
esp32_port = 80 

@app.route('/')
def hello():
    return 'Hello, this is my Flask app running on my local network for our led image sharing project!'

# Turning the onboard LED on and off

@app.route('/turn_on_led', methods=['GET'])
def turn_on_led():
    success = trigger_action('H')
    if success:
        return 'Turned on LED on ESP32'
    else:
        return 'Failed to turn on LED on ESP32'
    
@app.route('/turn_off_led', methods=['GET'])
def turn_off_led():
    success = trigger_action('L')
    if success:
        return 'Turned off LED on ESP32'
    else:
        return 'Failed to turn off LED on ESP32'
    
def trigger_action(endpoint):
    url = f'http://{esp32_ip}:{esp32_port}/{endpoint}'
    response = requests.get(url)
    return response.ok
    
# Uploading an image onto the server from the frontend
@app.route('/upload_image', methods=['POST'])
def upload_image():
    
    # file refers to the name of the name="file" attribute in the input field of an html element
    if 'file' not in request.files:
        print("no file part")
        return 'No file part'
    
    # Creates a FileStorage object with the contents of the image file
    image = request.files['file']
    if image.filename == '':
        print("no seleceted file")
        return 'No selected file'

    # Save the received image temporarily
    image.save('temp_image.jpg')
    print("image saved")

    # Open the image using Pillow (PIL)
    with Image.open('temp_image.jpg') as img:
        # Convert the image to a colored bitmap (adjust the mode as needed)
        converted_img = img.convert('RGB')

        # Save the converted colored bitmap image temporarily
        converted_img.save('temp_image2.bmp')

    print("going to send image esp32 func")
    success = send_image_to_esp32('temp_image2.bmp')
    
    if success:
        return 'Image sent to ESP32'
    else:
        return 'Failed to send image to ESP32'

# def send_image_to_esp32(image_path):
#     url = f'http://{esp32_ip}:{esp32_port}/receive_image'  # Replace with your ESP32 endpoint
#     with open(image_path, 'rb') as img_file:
#         files = {'image': img_file}
#         print("sending to ESP32")
#         response = requests.post(url, files=files)
#     return response.ok

@app.route('/get_image', methods=['GET'])
def get_image():
    # Assuming you have the image path or data to be sent
    image_path = 'path/to/your/image.jpg'  # Replace this with your image path
    # Send the image file as a response
    return send_file(image_path, mimetype='image/jpeg')  # Adjust mimetype as needed


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
