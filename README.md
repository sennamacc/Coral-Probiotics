# Coral-Probiotics
This repository includes all the projects I'm building to learn how AUVs can be used to scale up the delivery of coral probiotics.

# Part 1
This code was made with the help of the 'Image Segmentation Using Color Spaces in OpenCV + Python' tutorial on Real Python by Rebecca Stone.
It takes an image of "nemo" and displays both the HSV and RGB values, then uses them to display only the clownfish (without the background) by masking out values outside of selected ranges.

# Part 2
I wrote this program using the lessons I learned from Part 1 (+ my own research) to classify pictures of coral.
The RGB values of an inputed image are averaged out and used to determine whether the coral in the image is healthy, bleached, or dead.
