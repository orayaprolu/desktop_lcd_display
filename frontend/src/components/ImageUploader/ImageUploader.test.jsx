import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import ImageUploader from './ImageUploader';

describe('ImageUploader Component', () => {
  test('renders without crashing', () => {
    render(<ImageUploader />);
  });

  test('handles file change correctly', () => {
    render(<ImageUploader />);
    const fileInput = screen.getByLabelText('File Upload');
    const file = new File(['image'], 'test.jpg', { type: 'image/jpg' });

    fireEvent.change(fileInput, { target: { files: [file] } });

    // Assert that the selectedFile state is updated
    // You need to access the state, depending on your state management (e.g., using hooks testing library)
  });

  test('handles image upload correctly', async () => {
    render(<ImageUploader />);
    const fileInput = screen.getByLabelText('File Upload');
    const uploadButton = screen.getByText('Upload');

    const file = new File(['image'], 'test.jpg', { type: 'image/jpg' });
    fireEvent.change(fileInput, { target: { files: [file] } });

    fireEvent.click(uploadButton);

    // Mock the fetch call and assert the fetch parameters
    // Use waitFor to wait for asynchronous actions to complete
    await waitFor(() => {
      // Assert UI changes after the image is uploaded
      // For example, check if the image URL is displayed
    });
  });

  // Write similar tests for other functions (handleFetchImage, handleFetchImageAndBinary, handleDeleteImage, handleTurnOnLED, handleTurnOffLED)
});
