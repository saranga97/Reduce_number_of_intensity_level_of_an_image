import cv2
import numpy as np


def reduce_intensity_levels(image, levels):

    scaling_factor = 255 / (levels - 1)

    reduced_image = np.round(image / scaling_factor) * scaling_factor

    reduced_image = reduced_image.astype(np.uint8)

    return reduced_image


def main():

    image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Could not open or find the image.")
        return

    levels = int(input("Enter the desired number of intensity levels (greater than 1): "))

    if levels < 2:
        print("Error: Number of intensity levels must be greater than 1.")
        return

    reduced_image = reduce_intensity_levels(image, levels)

    cv2.imshow('Original Image', image)
    cv2.imshow('Reduced Image', reduced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
