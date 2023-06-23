from tkinter import Tk, Button
from image_viewer_app import ImageViewer

# Create the Tkinter root window
root = Tk()

# Create the image viewer instance
image_viewer = ImageViewer(root)

# Create buttons for image navigation
prev_button = Button(root, text="Previous", command=image_viewer.load_previous_image)
prev_button.pack(side="left")

next_button = Button(root, text="Next", command=image_viewer.load_next_image)
next_button.pack(side="right")

# Create a button to open the file dialog
open_button = Button(root, text="Open Image", command=image_viewer.open_image)
open_button.pack()

# Start the Tkinter event loop
root.mainloop()
