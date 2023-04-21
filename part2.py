import cv2
import matplotlib.pyplot as plt

import os
import numpy as np


def images_paths():
    """

    :rtype: string of path folder pictures.
    """
    image_paths = []
    # take the current path
    current_path = os.getcwd()
    image_dir = current_path + r"\img"
    if not os.path.isdir(image_dir):
        print('Directory not found:', image_dir)

    # List to store image file paths

    # Traverse the directory tree and find all image files
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            image_paths.append(os.path.join(root, file))

    # Print the list of image paths
    return image_paths


def print_picture(path, index):
    """
    show the picture with the stars at red color.
    for each star we print his coordinate radius and brightness.

    :rtype: return false if cant load the picture or no found stars else return true.
    """
    img = cv2.imread(path)
    if img is None:
        print('Error: Failed to load image', path)
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw the stars at red color.
    cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

    number_stars = len(contours)

    if number_stars == 0:
        print('No stars found in image', path)
        return False

    print("numbers in the picture " + str(index) + ":" + str(number_stars))
    # print for each picture all the starts x,y,r,b
    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        brightness = np.mean(gray[int(y) - 2:int(y) + 2, int(x) - 2:int(x) + 2])
        print(f"Star: x={x}, y={y}, radius={radius}, brightness={brightness}")
    print("\n")
    plt.imshow(img)
    plt.show()
    return True


def run_all_db():
    paths = images_paths()
    print("numbers of the pictures: " + str(len(paths)))
    index = 1
    for path in paths:
        print(path)
        print_picture(path=path, index=index)
        index += 1

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    run_all_db()
