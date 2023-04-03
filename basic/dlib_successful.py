# Import necessary libraries
import cv2
import dlib
import numpy as np

# Initialize the face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor(r"C:\Users\asui\Downloads\shape_predictor_68_face_landmarks.dat")./shape_predictor_68_face_landmarks
predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")
# Define the left and right eye landmarks
left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

# Initialize the video capture device
cap = cv2.VideoCapture(1)
ret, img = cap.read()
thresh = img.copy()

# Create a window to display the image and a trackbar to adjust the threshold value
cv2.namedWindow('image')
SLIDER_MIN = 0
SLIDER_MAX = 255
kernel = np.ones((9, 9), np.uint8)
cv2.createTrackbar('threshold', 'image', SLIDER_MIN, SLIDER_MAX)

# Function to convert facial landmarks into NumPy array
def shape_to_np(shape, dtype="int"):
    # Initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)
    # Loop over the 68 facial landmarks and convert them to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # Return the list of (x, y)-coordinates
    return coords

# Function to create a mask for the eye
def eye_on_mask(mask, side):
    # Get the coordinates of the eye landmarks
    points = [shape[i] for i in side]
    # Convert the points into a NumPy array of integers
    points = np.array(points, dtype=np.int32)
    # Create a convex polygon on the mask with the eye landmarks
    mask = cv2.fillConvexPoly(mask, points, 255)
    # Return the mask
    return mask

# Function to find the contour of the eye
def contouring(thresh, mid, img, right=False):
    # Find the contours in the thresholded image
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    try:
        # Find the largest contour
        cnt = max(cnts, key = cv2.contourArea)
        # Calculate the centroid of the contour
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        # Adjust the centroid position for the right eye
        if right:
            cx += mid
        # Draw a circle on the image at the centroid position
        cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
    except:
        pass


# Loop through the video frames
while(True):
    ret, img = cap.read()
    # Convert the image to grayscale and detect faces in the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    # Loop through the detected faces
    for rect in rects:
        # Get the facial landmarks for the face
        shape = predictor(gray, rect)
        # Convert the landmarks into a NumPy array
        shape = shape_to_np(shape)
        # Create a mask for the eyes
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, left)
        mask = eye_on_mask(mask, right)
        mask = cv2.dilate(mask, kernel, 5)
        eyes = cv2.bitwise_and(img, img, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        mid = (shape[42][0] + shape[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
        threshold = cv2.getTrackbarPos('threshold', 'image')
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1
        thresh = cv2.dilate(thresh, None, iterations=4) #2
        thresh = cv2.medianBlur(thresh, 3) #3
        thresh = cv2.bitwise_not(thresh)
        contouring(thresh[:, 0:mid], mid, img)
        contouring(thresh[:, mid:], mid, img, True)
        # for (x, y) in shape[36:48]:
        #     cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    # show the image with the face detections + facial landmarks
    cv2.imshow('eyes', img)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()