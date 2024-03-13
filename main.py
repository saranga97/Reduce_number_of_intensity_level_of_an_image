import cv2
import numpy as np


def reduce_intensity_levels(image, levels):
    # Calculate the scaling factor to map the original intensity levels to the desired levels
    scaling_factor = 255 / (levels - 1)

    # Apply the scaling factor to reduce the intensity levels
    reduced_image = np.round(image / scaling_factor) * scaling_factor

    # Convert the reduced image to uint8 data type
    reduced_image = reduced_image.astype(np.uint8)

    return reduced_image


def main():
    # Read the image
    image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Get the desired number of intensity levels from the user
    levels = int(input("Enter the desired number of intensity levels (greater than 1): "))

    # Validate the input
    if levels < 2:
        print("Error: Number of intensity levels must be greater than 1.")
        return

    # Reduce the intensity levels
    reduced_image = reduce_intensity_levels(image, levels)

    # Display the original and reduced images
    cv2.imshow('Original Image', image)
    cv2.imshow('Reduced Image', reduced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
