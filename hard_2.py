import cv2
import math
import numpy as np

def detect_arrow(image_path):
	# Read the image
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Apply Gaussian Blur to reduce noise
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)

	# Perform edge detection using Canny
	edges = cv2.Canny(blurred, 50, 150)

	# Find contours
	contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

		if len(approx) == 7:  # Arrows typically have 7 sides
			cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
			print("Arrow detected!")

			# Calculate bounding box
			x, y, w, h = cv2.boundingRect(approx)
			perceived_width = max(w, h)

			# Find distance (Function to be implemented)
			distance = find_distance(perceived_width)
			print(f"Estimated Distance: {distance:.2f} cm")

	# Show the result
	cv2.imshow('Detected Arrow', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def find_distance(perceived_width):
	
    # 1. Webcam Specifications
	w_px = 1280      # Resolution Width [cite: 201]
	h_px = 720       # Resolution Height [cite: 202]
	fov_deg = 55     # Diagonal FOV in degrees [cite: 202]
	real_width = 17.0 # Actual width of the arrow in cm 
	
	# Avoid division by zero if no contour/width is detected
	if perceived_width <= 0:
		return 0.0

	# 2. Calculate the diagonal resolution of the image in pixels
	diagonal_px = math.sqrt(w_px**2 + h_px**2)
	
	# 3. Calculate Focal Length (F) in pixels
	# Math library requires angles in radians for trigonometric functions
	fov_rad = math.radians(fov_deg)
	focal_length_px = diagonal_px / (2 * math.tan(fov_rad / 2))
	
	# 4. Apply the Pinhole Camera Distance Equation
	distance_cm = (real_width * focal_length_px) / perceived_width
	
	return distance_cm

# Provide the path to your image
image_path = 'arrow.jpg'
detect_arrow(image_path)