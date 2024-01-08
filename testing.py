import requests

url = 'http://127.0.0.1:4000/upload_image' 
file_path = 'benson.jpeg' 

with open(file_path, 'rb') as file:
    files = {'file': (file_path, file, 'image/jpeg')}
    response = requests.post(url, files=files)

if response.ok:
    print("File sent successfully to Flask server")
else:
    print("Failed to send file to Flask server")


