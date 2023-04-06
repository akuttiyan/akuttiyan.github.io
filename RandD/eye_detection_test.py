# Import the OpenCV library
import cv2

# Load the face and eye classifiers from XML files
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

# Open the camera device for video capturing
cam = cv2.VideoCapture(0)

# Set flag for video capturing status
ret = True

# Start the video capturing loop
while ret:
    # Read a frame from the camera
    ret, frame = cam.read()

    # If frame reading is successful
    if ret == True:
        scale_factor = 1.3
        min_num_neighbors = 5
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        face_points = face_detector.detectMultiScale(gray, scale_factor, min_num_neighbors)

        # For each face detected
        for (x, y, w, h) in face_points:
            line_thickness = 2
            # Draw a rectangle around the face on the original color frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 20), line_thickness)
        
            # Extract the region of interest (ROI) of the face
            face = frame[y:y+h,x:x+w]

            # Detect eyes in the face ROI
            eyes = eye_detector.detectMultiScale(face, scale_factor, min_num_neighbors)

            # For each eye detected
            for (x, y, w, h) in eyes:
                # Draw a rectangle around the eye on the face ROI
                cv2.rectangle(face, (x, y), (x+w, y+h), (155, 0, 120), line_thickness)

        # Display the original color frame with face and eye rectangles
        cv2.imshow('Live feed', frame)

    # Exit the loop if 'ESC' key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the camera device and close all windows
cam.release()
cv2.destroyAllWindows()