# HSV Color Filtering with OpenCV

This project uses OpenCV to capture video from the camera, apply HSV color filtering, and visualize the results. Users can adjust the color range using trackbars to filter specific colors in the live video stream. The program displays the original video, the mask, and the resulting image with the applied color filter.

## Overview

- **Functionality:** Captures video from the webcam, applies HSV color filtering, and allows the user to adjust the filter range using trackbars.
- **Objective:** Enable real-time color filtering to identify specific colors in the video feed by adjusting HSV (Hue, Saturation, Value) ranges.

## Key Learning Areas

### 1. Video Capture with OpenCV
- **Webcam Integration:** Capturing live video feed from the webcam using OpenCV's `cv2.VideoCapture()` method.
- **Error Handling:** Ensuring the webcam is accessible and handling any errors that may occur when capturing frames.

### 2. Color Filtering with HSV
- **HSV Color Space:** Converting the video frame from BGR to RGB and then to HSV color space for easier color-based filtering.
- **Trackbars:** Using OpenCV trackbars to dynamically adjust the hue, saturation, and value ranges for the color filter.
- **Masking:** Creating a binary mask that isolates the colors within the specified HSV range.

### 3. Real-time Visualization
- **Displaying Results:** Showing the original video, the mask, and the filtered result in real-time using OpenCV's `cv2.imshow()`.

## Languages and Tools Used

### Python
- **OpenCV:** For video capture and image processing.
- **NumPy:** For handling arrays and performing numerical operations.

## Visual representation

<table>
<tr>
  <td width="50%">
    <h3 align="center">Red Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/efafc758-b3e9-4ead-9b45-a37c4990eb8e" width="400">
    </div>
  </td>

  <td width="50%">
    <h3 align="center">Orange Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/ca5ee0ae-db28-4505-ad05-2347f0d3542e" width="400">
    </div>
  </td>
</tr>

<tr>
  <td width="50%">
    <h3 align="center">Yellow Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/820eefac-88d5-4c2d-8542-e01c5eac685c" width="400">
    </div>
  </td>

  <td width="50%">
    <h3 align="center">Blue Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/baf73583-a58d-4620-9e5a-163f516a0556" width="400">
    </div>
  </td>
</tr>

<tr>
  <td width="50%">
    <h3 align="center">White Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/9c071ab4-f62a-41a7-bb15-0cb720f3ca69" width="400">
    </div>
  </td>

  <td width="50%">
    <h3 align="center">Green Filter</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/217bdaa4-85af-4e6b-baab-be11bccbadc1" width="400">
    </div>
  </td>
</tr>
</table>

## Installation and Usage

### Requirements
- **Python 3.x** to run the script.
- **OpenCV library**: To install OpenCV, run the following:
```bash
pip install opencv-python
```
## Instructions
Clone the repository
  ```bash
  git clone https://github.com/carlosagalicia/HSV-Color-Filtering-with-OpenCV.git
  ```
Run the script
  ```bash
  python color_filtering.py
  ```
**Adjust the trackbars** to set the desired HSV range for color filtering.

**Press 'q'** to exit the program and close the windows.
