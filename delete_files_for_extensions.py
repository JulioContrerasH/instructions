import os

# Define the path to the directory
directory_path = "/home/contrerasnetk/Documents/Repositories/IPL-UV.github.io/static/old_pages"

# List of image file extensions to remove (case insensitive)
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.webp']

# Store the paths of removed files
removed_files = []

# Iterate over the files in the directory and remove images
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions):
            file_path = os.path.join(root, file)
            os.remove(file_path)
            removed_files.append(file_path)

# Display the removed file paths
removed_files
