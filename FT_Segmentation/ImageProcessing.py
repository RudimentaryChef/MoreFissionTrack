from PIL import Image
import numpy as np

def ConvertOneMask(input_path, output_path):
    # Load the PNG image from input
    image = Image.open(input_path)

    # Image to array
    image_array = np.array(image)

    # Multiply every element by 255
    image_array *= 255

    # Save the modified image
    modified_image = Image.fromarray(image_array.astype(np.uint8))
    modified_image.save(output_path)

# Example usage:
ConvertOneMask("/Users/adikrish/Desktop/4795.png", "/Users/adikrish/Desktop/4795MOD.png")
