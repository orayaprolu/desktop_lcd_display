from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import requests
from PIL import Image

# all the routes are stuff that should be called by the frontend

app = Flask(__name__)
CORS(app)

esp32_ip = '192.168.254.150'
esp32_port = 80 

@app.route('/')
def hello():
    return 'Hello, this is my Flask app running on my local network for our led image sharing project!'

### Turning the onboard LED on and off
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
    print("waiting for response")
    response = requests.get(url)
    print(response)
    print("response received")
    return response.ok
    
### Uploading an image onto the server from the frontend and pinging ESP32 to fetch it from the server
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
    print("jpg image saved")

    # Open the image using Pillow to covert and it the "with" syntax for resource management
    with Image.open('temp_image.jpg') as img:
        converted_img = img.convert('RGB')
        converted_img.save('converted_image.bmp')
        print("bitmap image saved on server")

    print("pinging esp32 to call get_image")
    success = trigger_esp32_to_fetch_image()
    if success:
        return jsonify({'message': 'Bitmap image was saved on server and sent to ESP32'}), 200
    else:
        return jsonify({'error': 'Failed to send image to ESP32'}), 500

    

def trigger_esp32_to_fetch_image():
    url = f'http://{esp32_ip}:{esp32_port}/receive_image'

    # Send a request to ESP32 to fetch the image

    response = requests.get(url)
    
    # Check the response and return success or failure
    return response.ok

### Sending bmp image from server to ESP
@app.route('/get_image', methods=['GET'])
def get_image():
    print("recieved request to get image from esp32")

    image_path = 'converted_image.bmp'
    try:
        print("attempting to send file")
        return send_file(image_path, mimetype='image/bmp')
    except FileNotFoundError:
        return "Image file not found", 404 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
