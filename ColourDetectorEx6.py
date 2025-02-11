import numpy as np
from extras import*
import matplotlib.pyplot as plt
from skimage.filters.thresholding import threshold_isodata, threshold_li, threshold_local, threshold_mean, threshold_minimum, threshold_multiotsu, threshold_niblack, threshold_otsu, threshold_sauvola, threshold_triangle
import skimage as ski
from PIL import Image
import cv2 as cv
cap = cv.VideoCapture(0)  # Open the webcam

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()  # Read a frame

    if not ret:
        print("Warning: Empty frame received. Retrying...")
        continue  # Skip processing if frame is empty

    into_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # Convert to HSV

    
    L_limit = np.array([20, 100, 100])  # Lower limit 
    U_limit = np.array([40, 255, 255])  # Upper limit 

    b_mask = cv.inRange(into_hsv, L_limit, U_limit)  # Create mask
    yellow = cv.bitwise_and(frame, frame, mask=b_mask)  # Apply mask

    # Display results
    cv.imshow('Original', frame)
    cv.imshow('Yellow Detector', yellow)

    if cv.waitKey(1) & 0xFF == 27:  # Exit on 'Esc' key
        break

cap.release()
cv.destroyAllWindows()
