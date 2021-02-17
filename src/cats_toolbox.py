import cv2 as cv

def find_cats(image):
    "Returns a list of tuples containing positions of cats in an image, empty list = no cats"

    ## load haar cascade
    haar_cascade = cv.CascadeClassifier("haar_cascade/haar_cascade.xml")

    ## grayscale
    image_copy = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    ## find cats
    cats = haar_cascade.detectMultiScale(image_copy, scaleFactor=1.1, minNeighbors=9)
    return cats


def rescale(image, max_aspect = (720, 720)):
    "Returns an image rescaled to the maximum dimensions, default (720, 720)"

    ## set scalar to fit our wants
    scalar = min(max_aspect[1] / image.shape[1], max_aspect[0] / image.shape[0], 1)

    ## resize the image according to the scalar
    new_dimensions = (int(image.shape[1] * scalar), int(image.shape[0] * scalar))
    return cv.resize(image, new_dimensions, interpolation=cv.INTER_AREA)


def draw_rectangles(image, positions):
    "Draws rectangles on image around positions (list of tuples) given in the form (x, y, w, h), where the left top corner coordinates are (x, y) and right bottom (x + w, y + h)"

    for (x,y,w,h) in positions:
        cv.rectangle(image, (x,y), (x+w, y+h), (0,0,255), thickness=3)
    return image
