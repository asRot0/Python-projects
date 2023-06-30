import os
from tkinter import Tk, filedialog

# Create a Tkinter root window (needed for the file dialog)
root = Tk()
root.withdraw()

# Open a file dialog to select the drive path
drive_path = filedialog.askdirectory(title="Select Drive or Directory Containing Photos")

# Check if a drive path was selected
if drive_path:
    # Initialize a counter for the number of photos
    photo_count = 0

    # Iterate over all files and directories in the drive path
    for root, dirs, files in os.walk(drive_path):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Check if the file extension corresponds to an image format
            image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            if extension.lower() in image_extensions:
                # Increment the photo count
                photo_count += 1

    print(f"Total number of photos: {photo_count}")
else:
    print("No drive path selected.")

