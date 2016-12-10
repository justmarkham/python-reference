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

#Display an image with openCV
cv2.namedWindow(window_name, property)  #creates a window with specific properties:
                                        #cv.WINDOW_NORMAL :User can resize the window (no constrain)
                                        #cv.WINDOW_AUTOSIZE: Window size is automatically adjusted
                                        #cv.WINDOW_OPENGL: Window created with OPENGL support


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

