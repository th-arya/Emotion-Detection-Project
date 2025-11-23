# ImageEmo - Real-Time Emotion Detection

A real-time facial emotion detection application that uses your webcam to detect and display emotions in real-time.

## Features

- Real-time emotion detection from webcam feed
- Face detection using MTCNN (Multi-task Cascaded Convolutional Networks)
- Emotion classification with confidence scores
- Visual feedback with bounding boxes and emotion labels
- Simple and intuitive interface

## Requirements

- Python 3.7+
- Webcam/Camera access

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ImageEmo
```

2. Install the required dependencies:
```bash
pip install opencv-python fer
```

Or if you prefer using a requirements file:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your webcam is connected and accessible
2. Run the application:
```bash
python web.py
```

3. The application will:
   - Open a window showing your webcam feed
   - Detect faces in real-time
   - Display the detected emotion and confidence score above each face
   - Draw a green bounding box around detected faces

4. To exit the application, press `q` in the window

## How It Works

- The application uses OpenCV to capture video frames from your webcam
- FER (Facial Expression Recognition) library with MTCNN backend detects faces and emotions
- Detected emotions are displayed with their confidence scores
- The application continuously processes frames until you press 'q' to quit

## Project Structure

```
ImageEmo/
├── web.py              # Main application file
├── test_images/        # Test images directory
│   └── t1.jpeg
└── README.md           # This file
```

## Technologies Used

- **OpenCV (cv2)**: Computer vision library for video capture and image processing
- **FER**: Facial Expression Recognition library for emotion detection
- **MTCNN**: Multi-task Cascaded Convolutional Networks for face detection

## Notes

- Make sure you have proper camera permissions on your system
- The application requires good lighting for optimal emotion detection
- Performance may vary depending on your hardware and camera quality

## License

This project is open source and available for personal and educational use.

