import requests

url = 'http://192.168.254.161:4000/upload_image'  # Replace with your Flask server's endpoint
file_path = 'benson.jpeg'  # Replace with the actual path to your PNG file

with open(file_path, 'rb') as file:
    files = {'file': (file_path, file, 'image/jpeg')}
    response = requests.post(url, files=files)

if response.ok:
    print("File sent successfully to Flask server")
else:
    print("Failed to send file to Flask server")
