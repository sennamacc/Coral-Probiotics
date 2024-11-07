import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb
import numpy as np
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

state = 0
# if it's 1 that means it's alive
# if it's 2 that means it's bleached
# if it's 3 that means it's dead
# 0 is just being used as a placeholder for now

# Get the picture:
path_input = input("Please input the name of a downloaded image:\n")
path = f"/Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/{path_input}" # insert your own file path
coral_1 = cv2.imread(path)

# Check if the image loaded correctly
if coral_1 is None:
    print("Error: Could not load the image. Please check the file path.")
else:
    # Convert from BGR to RGB
    coral_1 = cv2.cvtColor(coral_1, cv2.COLOR_BGR2RGB)
    plt.imshow(coral_1)
    plt.axis("off")

# Find average colour
pixels = coral_1.reshape(-1, 3)
mean_rgb = np.mean(pixels, axis=0)
std_rgb = np.std(pixels, axis=0)
threshold = 2
lower_bound = mean_rgb - threshold * std_rgb
upper_bound = mean_rgb + threshold * std_rgb
mask = np.all((pixels >= lower_bound) & (pixels <= upper_bound), axis=1)
filtered_pixels = pixels[mask]
avg_rgb = np.mean(filtered_pixels, axis=0)

print("Average rgb values:",avg_rgb)

# Define rgb ranges
healthy_min = np.array([70, 45, 25])
healthy_max = np.array([120, 80, 135])

bleached_min = np.array([140, 130, 120])
bleached_max = np.array([255, 255, 255])

dead_min = np.array([0, 0, 0])
dead_max = np.array([80, 110, 100])

# Classify state
if np.all((avg_rgb >= healthy_min) & (avg_rgb <= healthy_max)):
    state = 1
elif np.all((avg_rgb >= bleached_min) & (avg_rgb <= bleached_max)):
    state = 2
elif np.all((avg_rgb >= dead_min) & (avg_rgb <= dead_max)):
    state = 3
else:
    state = 1 # Defaulting to healthy

# Print state
if state == 1:
    print("This image shows a healthy coral.")
if state == 2:
    print("This image shows a bleached coral.")
if state == 3:
    print("This image shows a dead coral.")

plt.show()

""" info:

alive 1 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/alive coral 1.png
avg_rgb = [ 80.58274935  77.33952761 127.17205503]

alive 2 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/alive coral 2.png
avg_rgb = [116.32602708  53.84148189  31.99274824]



bleached 1 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/bleached coral 1.png
avg_rgb = [147.83832106 147.38571897 126.39375754]

bleached 2 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/bleached coral 2.png
avg_rgb = [185.75170534 182.55972926 175.26422127]



dead 1 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/dead coral 1.png
avg_rgb = [65.46923785 78.03089058 63.99304222]

dead 2 = /Users/Home/Documents/Python Projects/TKS 24-25/Replicate 1/dead coral 2.png
avg_rgb = [ 76.12816933 105.25936734  93.96454954]

"""
