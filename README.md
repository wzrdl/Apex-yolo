# Apex Legends AI Aimbot Using YOLO

This project is an AI-based aimbot for Apex Legends, utilizing the YOLO (You Only Look Once) deep learning model for real-time enemy detection and tracking. The system is designed to enhance gameplay by automatically aiming at detected enemies within the game environment. By leveraging GPU acceleration through CUDA and using cloud servers for training, this project provides a high-performance, real-time solution for enemy recognition and aiming.

## Features

- **Real-Time Enemy Detection**: The aimbot uses the YOLO deep learning model to detect enemies within the Apex Legends game environment in real time.
- **Efficient Tracking**: Once detected, the system automatically tracks and locks onto enemies, ensuring precise aiming during gameplay.
- **High-Performance GPU Acceleration**: CUDA GPU acceleration ensures that the deep learning model can process frames quickly and maintain high FPS during gameplay.
- **Cloud-Based Training**: The YOLO model is trained on cloud servers for optimal performance, taking advantage of high computational resources to reduce local hardware strain.
- **Manual Dataset Labeling and Preprocessing**: All datasets were manually labeled to ensure accurate enemy detection. Preprocessing steps included noise reduction, image enhancement, resizing, and color space conversion to prepare the data for efficient training.

## System Architecture

The project involves multiple steps from dataset preparation to real-time deployment within the game environment. Below is an outline of the core processes:

1. **Dataset Collection & Labeling**: 
   - Screenshots or video frames from Apex Legends were manually labeled to identify enemy players.
   - Image preprocessing was performed to enhance the dataset, including noise reduction, resizing, color space conversion, and image augmentation.

2. **Model Training**: 
   - The YOLO deep learning model was trained using the preprocessed and labeled dataset.
   - Training was done on cloud servers to take advantage of faster processing speeds and avoid local hardware limitations.
   - PaddlePaddle (Paddle) was used as the deep learning framework for building and training the YOLO model.

3. **Real-Time Aiming**:
   - Once trained, the YOLO model was integrated into the game environment to detect and track enemies in real time.
   - CUDA was utilized for GPU acceleration, ensuring that the model could handle high frame rates and provide real-time feedback without FPS drops.

4. **Deployment**:
   - The system is designed to work seamlessly within the Apex Legends game, providing immediate feedback to enhance gameplay.
   - The model runs locally during gameplay, detecting and aiming at enemies automatically based on the trained YOLO model.

## Tools and Technologies

- **Python**: The core programming language used for model development and integration with Apex Legends.
- **PaddlePaddle (Paddle)**: The deep learning framework used for building and training the YOLO model.
- **YOLO (You Only Look Once)**: A state-of-the-art real-time object detection model used for identifying enemies in the game.
- **CUDA**: For GPU acceleration during both the training phase and real-time gameplay integration.
- **Cloud Server**: Used for training the YOLO model with the labeled dataset, ensuring faster processing times and resource availability.

## Setup and Installation

### Prerequisites
To run this project, you will need:

- Python 3.7 or later
- CUDA-compatible GPU and drivers
- PaddlePaddle (Paddle) deep learning framework
- YOLO pre-trained model weights or ability to train on a labeled dataset
- Apex Legends game installed on your machine
