# Hand Gesture Mouse Controller

## Project Overview
Hand Gesture Mouse Controller is an innovative software that enables users to control their computer's mouse cursor using hand gestures. This project uses computer vision and hand landmark detection to translate hand movements and gestures captured by a webcam into mouse actions, offering a unique and intuitive way of interacting with your computer.

## Features
- **Real-Time Hand Tracking**: Utilizes a webcam to track hand movements in real time.
- **Mouse Movement and Click Control**: Translates hand movements into mouse cursor movements and interprets gestures as mouse clicks.
- **Gesture Recognition**: Detects specific hand gestures, like closed hand or index finger pointing, to perform corresponding mouse actions.
- **Smooth Cursor Movement**: Implements a smoothing algorithm for more natural and fluid cursor motion.

## Components
- **HandDetector**: Uses MediaPipe to detect hand landmarks in video frames.
- **MouseController**: Controls mouse actions based on interpreted hand gestures.
- **ScreenInfo**: Gathers screen dimension information for accurate cursor movement across different monitor setups.
- **Smoother**: Smoothens the mouse cursor movement for a more natural feel.
- **VelocityCalculator**: Calculates the velocity of hand movements to enhance cursor motion accuracy.

## Requirements
- Python 3.x
- OpenCV (cv2)
- MediaPipe
- PyAutoGUI
- numpy
- screeninfo

## Installation
1. Clone the repository: `git clone [repository URL]`
2. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Run the main script: `python src/main.py`
2. Control the mouse cursor using hand gestures in front of the webcam.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page] for open issues or to open a new issue.