import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb
import numpy as np
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

# Get the picture:
nemo = cv2.imread("C:/Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/nemo2.jpg")
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo)
#plt.show()

# Visualize picture in RGB:
r, g, b = cv2.split(nemo)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()

# Visualize picture in HSV:
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_nemo)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()

# Selecting colours:
light_orange = (25, 255, 255)
dark_orange = (0, 175, 100)

"""lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8)
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8)

lo_square_rgb = cv2.cvtColor(lo_square, cv2.COLOR_HSV2RGB)
do_square_rgb = cv2.cvtColor(do_square, cv2.COLOR_HSV2RGB)

plt.subplot(1, 2, 1)
plt.imshow(do_square_rgb)
plt.title('Dark Orange')
plt.subplot(1, 2, 2)
plt.imshow(lo_square_rgb)
plt.title('Light Orange')
plt.show()"""

# Creating an orange mask:
mask_orange = cv2.inRange(hsv_nemo, dark_orange, light_orange)
result_orange = cv2.bitwise_and(nemo, nemo, mask=mask_orange)
plt.subplot(1, 2, 1)
plt.imshow(mask_orange, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result_orange)
plt.show()

# Whites
light_white_hsv = (0, 0, 100)
dark_white_hsv = (175, 150, 255)
mask_white_hsv = cv2.inRange(hsv_nemo, light_white_hsv, dark_white_hsv)
result_white_hsv = cv2.bitwise_and(hsv_nemo, hsv_nemo, mask=mask_white_hsv)

light_white_rgb = (160, 160, 145)
dark_white_rgb = (255, 255, 255)

mask_white_rgb = cv2.inRange(nemo, light_white_rgb, dark_white_rgb)
result_white_rgb = cv2.bitwise_and(nemo, nemo, mask=mask_white_rgb)

mask_white_combined = cv2.bitwise_and(mask_white_hsv, mask_white_rgb)
result_white = cv2.bitwise_and(nemo, nemo, mask=mask_white_combined)

plt.subplot(1, 2, 1)
plt.imshow(mask_white_combined, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result_white)
plt.show()

# Final result
final_mask = mask_orange + mask_white_combined
final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
plt.subplot(1, 2, 1)
plt.imshow(final_result)
plt.show()
