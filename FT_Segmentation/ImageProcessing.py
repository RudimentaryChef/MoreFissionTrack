from PIL import Image
import numpy as np
import os

def modify_images_in_folder(input_folder, output_folder):
    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Iterate through each file in the folder
    for file in files:
        # Check if the file is a PNG image
        if file.endswith(".png"):
            # Construct the full input and output paths
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".png", "MOD.png"))
            # Converts every file in the folder accordingly
            ConvertOneMask(input_path, output_path)

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
input_folder = "/Users/adikrish/Desktop/input_folder"
output_folder = "/Users/adikrish/Desktop/output_folder"
modify_images_in_folder(input_folder, output_folder)

# Example usage:
ConvertOneMask("/Users/adikrish/Desktop/4795.png", "/Users/adikrish/Desktop/4795MOD.png")
