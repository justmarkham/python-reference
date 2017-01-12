'''
OpenCV Quick Reference
https://github.com/justmarkham/python-reference

By Stein Castillo (kevin@dataschool.io)
http://www.dataschool.io

Table of Contents:
    Imports
    Basic Image Operations
    Image Manipulation

    ****
    Data Types
    Math
    Comparisons and Boolean Operations
    Conditional Statements
    Lists
    Tuples
    Strings
    Dictionaries
    Sets
    Defining Functions
    Anonymous (Lambda) Functions
    For Loops and While Loops
    Comprehensions
    Map and Filter
'''

### IMPORTS ###

#Generic imports
import cv2
import numpy as np 

#Import matplotlib to display images
from matplotlib import pyplot as plt 

#Extended mahotas functionality
import mahotas
import mahotas as mh    #typical import 

#Import if command line arguments are required
import argparse


### BASIC IMAGE OPERATIONS ###

#Load an image
image = cv2.imread(image)

#Load an image and convert to grayscale
image = cv2.imread(image, 0)
image = cv2.imread(image, cv2.IMREAD_GRAYSCALE) #both commands do the same thing

#Determine image properties
(h, w, c) = image.shape     #h: Height, w: Width, c: Channels
size = image.size           #Number of pixels
imgtype = image.dtype       #Image type
max = image.max()           #Maximum value
min = image.min()           #Minimum value

#Display an image with openCV
cv2.namedWindow(window_name, property)  #creates a window with specific properties:
                                        #cv2.WINDOW_NORMAL :User can resize the window (no constrain)
                                        #cv2.WINDOW_AUTOSIZE: Window size is automatically adjusted
                                        #cv2.WINDOW_OPENGL: Window created with OPENGL support


cv2.imshow(window_name, image)  #display image, automatic window properties


cv2.destroyWindow(window_name)  #Closes specified window
cv2.destroyAllWindows()         #Close all opencv windows


cv2.waitKey()                   #Display the windows and wait for user keypress
key = cv.waitKey(0) &0xFF       #Display the windows and store keypress 


#Display an image with MATPLOTLIB
img = cv2.imread(image, 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


###IMAGE MANIPULATION###

#convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Blur image

#Gaussian blur
#Very effective to remove gaussian noise in an image
#It is recommended to convert the image to grayscale before applying the blur filter.
blurred = cv2.GaussianBlur(image, (5, 5), 0)    #image: source image
                                                #(5, 5): Kernel size, must be positive and odd

#Average blur
#Used to smooth an image applying normalized box filter
#Average filter. takes the average of all the pixels under the kernel
blurred = cv2.blur(image, (5,5))        #image: Source image
                                        #(5,5): Kernel size, must be positive and odd

#Median blur
#Used to remove "salt and pepper" noise from an image
#Computes the median of all the pixels under the kernel
blurred = cv2.medianBlur(image, 5)      #image: Source image
                                        #5: Kernel size, most be positive and odd

#Applyng Gaussian blur filter with Mahotas
blurred = mahotas.gaussian_filter(image, 8) #imageö Source image
                                            #8: standard deviation for Gaussian kernel (in pixel units)



#Thresholding an image

""" Thresholding is the binarization of an image:
    any value over an index (C) is set to 255 (White)
    any value under the index (C) is set ot 0 (black)

    inverse binarizacion is also possible:
    any value over the index (C) is the to 0 (black)
    any value under the index (C) is set to 255 (white)"""

#Simple thresholding
#requires user intervetion to provide the index (C) value
(T, thresh) = cv2.threshold(src, C, 255, cv2.THRESH_BINARY) #src: source image
                                                            #C: index (as explained above)
                                                            #255: max value to assign if value greater than C
                                                            #Method:    cv2.THRESH_BINARY
                                                            #           cv2.THRESH_BINARY_INV
                                                            #Returns:   T: max value
                                                            #           thresh: Thresholded image
#examples of simple thresholding
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)





