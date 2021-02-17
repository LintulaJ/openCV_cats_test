import cv2 as cv
import cats_toolbox

def cats(image_name):
    "Label the image with the number of cats in it and mark the cats with rectangles"

    ## read image
    image = cv.imread(image_name)

    ## rescale image to abide by max aspect ratios
    image = cats_toolbox.rescale(image)

    ## find cats
    cats = cats_toolbox.find_cats(image)

    ## mark the cats
    image = cats_toolbox.draw_rectangles(image, cats)

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


def main():
    "A quick temporary test function for the program"

    ## The images are named in the format seen on the initialisation strings below.
    ## Iterate through all the images in the image folder by changing the file name using string operations.
    ## Currently the image folder has 5 images of cats and 5 of not cats.
    cat_string = "images/cat0.jpg"
    not_cat_string = "images/notcat0.jpg"

    for i in range(0, 5):
        if i != 0:
            cat_string = cat_string.replace(str(i-1), str(i))
            not_cat_string = not_cat_string.replace(str(i-1), str(i))
        
        cats(cat_string)
        cats(not_cat_string)
    
if __name__ == "__main__":
    main()