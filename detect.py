import cv2
import numpy as np

def detect_currency(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return "Invalid Image"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),0)

    edges = cv2.Canny(blur,100,200)

    feature_value = np.mean(edges)

    threshold = 50

    if feature_value > threshold:
        result = "Real Currency"
    else:
        result = "Fake Currency"

    return result