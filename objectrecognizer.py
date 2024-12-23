import cv2
import numpy as np

# Camera initialization
video = cv2.VideoCapture(0)

# Validate if the camera is available
if not video.isOpened():
    print("Error: Unable to access the camera.")
    exit()

# Create a window and trackbars to adjust HSV ranges
cv2.namedWindow("Video", 2)
cv2.createTrackbar("HL", "Video", 0, 180, lambda x: None)
cv2.createTrackbar("HH", "Video", 0, 180, lambda x: None)
cv2.createTrackbar("SL", "Video", 0, 255, lambda x: None)
cv2.createTrackbar("SH", "Video", 0, 255, lambda x: None)
cv2.createTrackbar("VL", "Video", 0, 255, lambda x: None)
cv2.createTrackbar("VH", "Video", 0, 255, lambda x: None)

# Main loop
while video.isOpened():
    # Capture frame from the camera
    ret, frame = video.read()

    # Validate if the frame capture was successful
    if not ret:
        print("Error: Unable to read frame from the camera.")
        break

    # Color space conversion
    frame_aux = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame_aux, cv2.COLOR_RGB2HSV)

    # Read values from the trackbars
    hl = cv2.getTrackbarPos("HL", "Video")
    hh = cv2.getTrackbarPos("HH", "Video")
    sl = cv2.getTrackbarPos("SL", "Video")
    sh = cv2.getTrackbarPos("SH", "Video")
    vl = cv2.getTrackbarPos("VL", "Video")
    vh = cv2.getTrackbarPos("VH", "Video")

    # Define HSV ranges
    lower_red = np.array([hl, sl, vl])
    upper_red = np.array([hh, sh, vh])

    # Create mask and apply masking
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original video, the mask, and the result
    cv2.imshow("Video", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Res", res)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
video.release()
cv2.destroyAllWindows()
