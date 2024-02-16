import cv2
import os
import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

folder_path = './imgs'
dataset = os.listdir(folder_path)
dataset = [file for file in dataset]

# Sort the list of image files in ascending order
dataset = sorted(dataset)

print(dataset)

# Print the sorted list

areas = []

# The main loop for segmentation and area counting
for img in dataset:
    # Loading the image in grayscale and applying Gaussian blur
    image = cv2.imread(f"{folder_path}/{img}")
    
    print(f"processing image: {img}")

    scale_percent = 50 # percent of base size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Function that creates a new white image using cv2
    def new_image(img):
        dimensions = img.shape
        w, h = dimensions[0], dimensions[1]
        new_img = np.ones((w, h, 3), dtype = np.uint8)
        new_img = 255* new_img
        return new_img
    
    # resize image
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    imsize = int(image.shape[1]) * int(image.shape[0])

    base = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    base = cv2.GaussianBlur(base, (9,9), 0)

    # Applying adaptive threshold to account for the darkness difference
    adapt_thresh = cv2.adaptiveThreshold(base, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 3)

    # Applying entropy 
    entropy_trs = entropy(adapt_thresh, disk(1)) 
    trs_value = threshold_otsu(entropy_trs) 
    entropy_img = entropy_trs <= trs_value

    entropy_img = entropy_img.astype(int)
    entropy_img = (entropy_img*255).astype(np.uint8)

    entropy_trs2 = entropy(entropy_img, disk(1)) 
    trs_value2 = threshold_otsu(entropy_trs2) 
    entropy_img2 = entropy_trs2 <= trs_value2

    entropy_img2 = entropy_img2.astype(int)
    entropy_img2 = (entropy_img2*255).astype(np.uint8)

    entropy_padded =  cv2.copyMakeBorder(entropy_img2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, 0)

    contours, hierarchy = cv2.findContours(entropy_padded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    white2 = new_image(entropy_padded)
        
    masked = cv2.drawContours(image=white2, contours=contours, contourIdx=-1, color=(0, 0, 0), thickness = -1, lineType=cv2.LINE_AA)

    area = cv2.countNonZero(entropy_padded)
    areas.append(area)
 
# Plot Area VS Hours   
plt.plot(range(len(areas)), areas)
plt.xlabel('Hours')
plt.ylabel('Area')
plt.title('Area of scratch over time')
plt.show()
    