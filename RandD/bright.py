# import the necessary packages
import numpy as np
import argparse
import cv2
import dlib
# construct the argument parse and parse the arguments

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")

ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
cap = cv2.VideoCapture(1)

left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

ret, image = cap.read()
thresh = image.copy()


# Create a window to display the image and a trackbar to adjust the threshold value
cv2.namedWindow('image')
SLIDER_MIN = 0
SLIDER_MAX = 255
kernel = np.ones((9, 9), np.uint8)
cv2.createTrackbar('threshold', 'image', SLIDER_MIN, SLIDER_MAX)

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	# return the list of (x, y)-coordinates
	return coords


def eye_on_mask(mask, side):
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask

def contouring(thresh, mid, img, img_gray, right=False):
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    try:
        cnt = max(cnts, key = cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        if right:
            cx += mid
        cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)

        # begining of custom-written code
        x = cx
        y = cy
        r = 10
        max_brightness = 255.0
        max_center = (0, 0)
        for i in range(x - r, x + r):
            for j in range(y - r, y + r):
                rgb = img_gray[i][j]
                i_j_brightness = rgb
                if i_j_brightness < max_brightness:
                        max_brightness = i_j_brightness
                        max_center = (i, j)
        cv2.circle(img, max_center, 3, (0, 255, 0), -1)
    except:
        pass


scale_factor = 1

while(True):
    scale_factor = 1
    dilation_num = 5
    kernel_size = 3
    ret, img = cap.read()
	#image = cv2.imread(args["image"])
    orig = image.copy()

    # Convert the image to grayscale and detect faces in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, scale_factor)
    #eyes_gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
    #(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(eyes_gray)
    image = orig.copy()
    cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 2)
    # Loop through the detected faces
    for rect in rects:
        # Get the facial landmarks for the face
        shape = predictor(gray, rect)
        # Convert the landmarks into a NumPy array
        shape = shape_to_np(shape)
        # Create a mask for the eyes
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, left)
        mask = eye_on_mask(mask, right)
        mask = cv2.dilate(mask, kernel, dilation_num)######################
        eyes = cv2.bitwise_and(image, image, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]########################3
        mid = (shape[42][0] + shape[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
        eyes_gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(eyes_gray)
        threshold = cv2.getTrackbarPos('threshold', 'image')
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1
        thresh = cv2.dilate(thresh, None, iterations=4) #2
        thresh = cv2.medianBlur(thresh, kernel_size) #3 ###################
        thresh = cv2.bitwise_not(thresh)
        contouring(thresh[:, 0:mid], mid, image)
        contouring(thresh[:, mid:], mid, image, True)
        # for (x, y) in shape[36:48]:
        #     cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    # show the image with the face detections + facial landmarks
    cv2.imshow('eyes', image)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()