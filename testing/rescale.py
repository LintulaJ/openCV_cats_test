
import cv2 as cv



def rescale(image, scalar):
    
    new_dimensions = (int(image.shape[1] * scalar), int(image.shape[0] * scalar))
    return cv.resize(image, new_dimensions, interpolation=None)


def resize(image, new_dimensions):

    return cv.resize(image, new_dimensions, interpolation=None)