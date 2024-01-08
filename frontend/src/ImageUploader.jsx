import { useState } from 'react';
import './ImageUploader.css'; // Import the CSS file

function ImageUploader() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imageUrl, setImageUrl] = useState('');
  const serverAddress = "http://192.168.254.161:4000"
  
  // Function to handle file selection
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  // Function to upload the selected image
  const handleUpload = () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      // Send POST request to upload the image
      fetch(`${serverAddress}/upload_image`, {
        method: 'POST',
        body: formData
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          // Handle the response from the API if needed
          console.log('Response from API:', data);
        })
        .catch(error => {
          // Handle errors
          console.error('There was an error:', error);
        });
    } else {
      console.error('Please select an image file');
    }
  };

  // Function to fetch the image
  const handleFetchImage = () => {
    fetch(`${serverAddress}/get_image`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        setImageUrl(`${serverAddress}/get_image`);
      })
      .catch(error => {
        console.error('There was an error fetching the image:', error);
      });
  };

  // Function to delete the image
  const handleDeleteImage = () => {
    // Clear the displayed image URL locally
    setImageUrl('');
  };

  // Function to turn on the LED
  const handleTurnOnLED = () => {
    fetch(`${serverAddress}/turn_on_led`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Handle success if needed
      })
      .catch(error => {
        console.error('There was an error turning on LED:', error);
      });
  };

  // Function to turn off the LED
  const handleTurnOffLED = () => {
    fetch(`${serverAddress}/turn_off_led`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Handle success if needed
      })
      .catch(error => {
        console.error('There was an error turning off LED:', error);
      });
  };

  return (
    <div className="container">
      {/* File upload section */}
      <input type="file" accept=".jpg" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {/* Image manipulation buttons */}
      <div className="button-group">
        <button onClick={handleFetchImage}>Fetch Image</button>
        <button onClick={handleDeleteImage}>Delete Image</button>
        <button onClick={handleTurnOnLED}>Turn On LED</button>
        <button onClick={handleTurnOffLED}>Turn Off LED</button>
      </div>

      {/* Display the uploaded image */}
      {imageUrl && <img src={imageUrl} alt="Uploaded" className="uploaded-image" />}
    </div>
  );
}

export default ImageUploader;
