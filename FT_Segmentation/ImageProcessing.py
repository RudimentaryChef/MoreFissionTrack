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
            output_path = os.path.join(output_folder)
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

def merge_to_tiff(folder_path, output_path, sort = False):
    # Get list of files in folder
    files = os.listdir(folder_path)

    # Filter out non-image files. A just in case precaution.
    image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    # Sort image files if required
    if(sort):
        image_files.sort()

    # Open images and merge them into a single TIFF file
    images = [Image.open(os.path.join(folder_path, f)) for f in image_files]
    images[0].save(output_path, save_all=True, append_images=images[1:], format='TIFF')

    print("TIFF file created successfully!")


import os

def rename_file_endings(directory, find, replace):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(replace):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.replace(find, replace))
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")

# Provide the directory path you want to search through
directory_path = "/Users/adikrish/PycharmProjects/MoreFissionTrack/training/M/segmented"

# Call the function to rename the files
rename_file_endings(directory_path, "MOD.png", ".png")

seg_folder_path = '/Users/adikrish/PycharmProjects/MoreFissionTrack/training/M/segmented'
seg_output_path = '/Users/adikrish/PycharmProjects/MoreFissionTrack/training/SegTrainTIFF/masks.TIFF'
patch_folder_path = '/Users/adikrish/PycharmProjects/MoreFissionTrack/training/M/image_patch'
patch_output_path = '/Users/adikrish/PycharmProjects/MoreFissionTrack/training/SegTrainTIFF/patches.TIFF'
merge_to_tiff(patch_folder_path, patch_output_path, True)
merge_to_tiff(seg_folder_path, seg_output_path, True)

#How to use modify_images_in_folder
#input_folder = "/Users/adikrish/PycharmProjects/MoreFissionTrack/training/M/label_patch"
#output_folder = "/Users/adikrish/PycharmProjects/MoreFissionTrack/training/M/segmented"
#modify_images_in_folder(input_folder, output_folder)

#How to use ConvertOneMask
#ConvertOneMask("/Users/adikrish/Desktop/4795.png", "/Users/adikrish/Desktop/4795MOD.png")
