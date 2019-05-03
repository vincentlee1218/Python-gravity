##########################################################
# Reading and displaying images
#import brings in different modules
import matplotlib.pyplot as plt
import os.path
import numpy as np # "as" lets us use standard abbreviations



# img contains image documents

img = plt.imread('rings.jpg')
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()

# Things to type in
# type(img)
# img
# len(img)
#
# GETTING COLORS
#Option 1
# GETTING COLOR VALUES
#
# red   = img[r][c][0]
# green = img[r][c][1]
# blue  = img[r][c][2]
#
# SETTING COLOR VALUES
# img[r][c][0]=red
# img[r][c][1]=green
# img[r][c][2]=blue
#
#
#Option 2
# [red green blue]=img[r][c]
# img[r][c] = [red green blue]
# 
# for png files, you have
#    [red green blue alpha]
# where alpha is the transparency
#
#
#

###############################################################
# PART 2
###
# Make a rectangle of pixels yellow

height = len(img)
width = len(img[0])
for row in range(20, 170):
  for column in range(20, 170):
    img[row][column] = [255, 133, 255] # red + green = yellow
ax.imshow(img, interpolation='none')
fig.show()

#################################################################
# PART 3A
###
# Change a region if condition is True
###
#height = len(img)
#width = len(img[0])
#for r in range(355):
#  for c in range(355):
#    if sum(img[r][c])==765: # brightness R+G+B goes up to 3*255=765
#      img[r][c]=[0,0,0] # R + B = magenta
#ax.imshow(img, interpolation='none')
#fig.show()
#################################################################
# PART 3B
###
# Change a region if condition is True
###
height = len(img)
width = len(img[0])
for r in range(height):
  for c in range(width):
    if (img[r][c][0])>100: # brightness R+G+B goes up to 3*255=765
      img[r][c]=[200,200,0] # R + B = magenta
ax.imshow(img, interpolation='none')
fig.show()

###################################################################
# PART 4
#height = len(img)
#width = len(img[0])
#for r in range(155):
# for c in range(width):
# if (img[r][c][0])>140: # brightness R+G+B goes up to 3*255=765
# img[r][c-5]=img[r][c] # R + B = magenta
#ax.imshow(img, interpolation='none')
#fig.show()



