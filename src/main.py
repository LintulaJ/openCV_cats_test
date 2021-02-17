import cv2 as cv
import cats_toolbox

def cats(image_name):
    "Label the image with the number of cats in it and mark the cats with rectangles"

    ## read image
    image = cv.imread(image_name)
    ## cv.imshow("-1", image)

    ## rescale image to abide by max aspect ratios
    image = cats_toolbox.rescale(image)
    ## cv.imshow("0", image)

    ## find cats
    cats = cats_toolbox.find_cats(image)
    ## cv.imshow("1", image)

    ## mark the cats
    image = cats_toolbox.draw_rectangles(image, cats)
    ## cv.imshow("2", image)

    ## create label
    label = ""
    if (len(cats) == 0):
        label = "No cats found"
    elif (len(cats) == 1):
        label = "1 cat"
    else:
        label = str(len(cats)) + " cats"

    cv.imshow(label, image)
    cv.waitKey(0)


numberstring = "01234"
cat_string = "images/cat0.jpg"
not_cat_string = "images/notcat0.jpg"

for i in range(0, 5):
    if i != 0:
        cat_string = cat_string.replace(numberstring[i-1], numberstring[i])
        not_cat_string = not_cat_string.replace(numberstring[i-1], numberstring[i])
    
    cats(cat_string)
    cats(not_cat_string)
    