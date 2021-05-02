from .get_window_position import get_window_position
from .grab_screen import grab_screen
from .save_one_frame import save_one_frame
import numpy as np
import cv2
from random import randint

def get_center_coordinates():
    position = get_window_position('_tb')
    xmin, ymin, xmax, ymax = get_window_position('_tb')

    image = grab_screen((xmin, ymin, xmax, ymax))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0], dtype="uint8")
    upper = np.array([45, 255, 255], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)

    # Uncomment the below line to save image to screenshots directory
    # save_one_frame(mask)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    centers = []
    for c in cnts:
        center_point, radius = cv2.minEnclosingCircle(c)
        if radius > 10:
            centers.append((int(center_point[0]), int(center_point[1])))

    return centers

if __name__ == '__main__':
    print(get_center_coordinates())
