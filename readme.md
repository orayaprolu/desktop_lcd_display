# led_image_sharing

User friendly software to send images to your ESP32

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project showcases the integration of a React frontend with a Flask backend. The frontend allows users to upload and send images to the backend to be parsed into a bitmap image which is then sent to your ESP32.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) for running the React frontend.
- [Python](https://www.python.org/) for running the Flask backend.
- [npm](https://www.npmjs.com/) (comes with Node.js) for managing frontend dependencies.

In `backend/app.py` make sure to add your ESP32's local IP and the port that it is running on in the constant at the top.

## Getting Started

Follow these steps to set up and run both the Flask backend and the React frontend.

### Backend Setup

1. Navigate to the `backend` directory:

   ```bash
   cd backend

2. Create Python virtual environment
  
  ```bash
  python -m venv venv

3. Activate virtual environment
  
  ```bash
  source venv/bin/activate

4. Install dependencies
  
  ```bash
  pip install -r requirements.txt

5. Run the Flask dev server (making sure it is open to all trafic with --host=0.0.0.0), I like to run it on 4000 which usually isn't occupied
  
  ```bash
  flask run --host=0.0.0.0 --port=4000

### Frontend Setup

1. On a new terminal navigate to the `frontend` directory:

   ```bash
   cd frontend

2. Install frontend dependencies
  
  ```bash
  npm install

3. Start your frontend locally
  
  ```bash
  npm run dev

### License 

This project is licensed under the MIT License.

