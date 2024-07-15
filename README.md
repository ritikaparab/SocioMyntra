Virtual Dressing Room

Welcome to the Virtual Dressing Room project! This application allows users to try on virtual clothes using their webcam. Built with Python, Flask, OpenCV, and integrated with Zeole for live streaming, this system provides an interactive and immersive experience.
Table of Contents

    Introduction
    Features
    Technologies Used
    Setup Instructions
    Usage
    License

Introduction

The Virtual Dressing Room application leverages computer vision to overlay images of clothes onto the user's live webcam feed, allowing them to see how different items would look on them in real-time. The system also includes a live stream feature using Zeole, enabling users to share their virtual dressing experience.
Features

    Real-time virtual dressing: Try on different clothes virtually using a webcam.
    Face detection: Utilizes OpenCV to detect and track faces.
    Dynamic resizing: Ensures clothes are appropriately scaled to fit the user's body.
    Live streaming: Share your virtual dressing experience with others using Zeole.
    Responsive design: Accessible from various devices and screen sizes.

Technologies Used

    Flask: Web framework for building the server-side application.
    OpenCV: Computer vision library for face detection and image processing.
    NumPy: Fundamental package for numerical computations in Python.
    Pillow: Python Imaging Library (PIL) for image manipulation.
    Zeole: Live streaming service integration.

Setup Instructions
Prerequisites

    Python 3.x
    Virtual environment (optional but recommended)

Installation

    Clone the repository:

bash

git clone https://github.com/yourusername/virtual-dressing-room.git
cd virtual-dressing-room

    Create and activate a virtual environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install the required dependencies:

bash

pip install -r requirements.txt

Running the Application

    Start the Flask server:

bash

python app.py

    Access the application:

Open your web browser and navigate to http://127.0.0.1:5000/.
Usage
Try On Clothes

    Navigate to the virtual dressing room page:
        Click on the "Try Now" button on the homepage.

    Allow webcam access:
        Grant the application permission to access your webcam.

    Choose an item:
        Use the interface to select different clothes and see them overlaid on your live webcam feed.

Live Streaming with Zegocloud

    Setup Zeole:
        Create an account on Zeole and obtain your stream key.

    Start streaming:
        Use the provided stream key to start your live stream directly from the application.
