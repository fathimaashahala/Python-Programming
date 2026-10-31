
import numpy as np

# Create an image matrix
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Image:")
print(image)

# 1. Reshape the image matrix
reshaped = image.reshape(2, 8)
print("\nReshaped Image:")
print(reshaped)

# 2. Slice a specific region
region = image[0:2, 0:2]
print("\nSliced Image Region:")
print(region)

# 3. Brightness adjustment using broadcasting
brightness = 30
bright_image = np.clip(image + brightness, 0, 255)
print("\nBrightness Adjusted Image:")
print(bright_image)

# 4. Matrix multiplication for transformation
transformation = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

transformed = np.dot(transformation, image)
print("\nTransformed Image:")
print(transformed)

# 5. Display image information
print("\nImage Shape:", image.shape)
print("Image Size:", image.size)
print("Maximum Pixel Value:", image.max())
print("Minimum Pixel Value:", image.min())
