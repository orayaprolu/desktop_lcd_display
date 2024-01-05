import { useState } from 'react';

function ImageUploader() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    // Get the selected file from the input
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = () => {
    // Check if a file is selected
    if (selectedFile) {
      // Create a FormData object
      const formData = new FormData();
      formData.append('image', selectedFile);

      fetch('YOUR_API_ENDPOINT', {
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
          // Handle the response from your API
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

  return (
    <div>
      <input type="file" accept=".jpg" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default ImageUploader;
