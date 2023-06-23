import os
from tkinter import Tk, Frame, Label, Button, filedialog
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Create a frame to hold the image
        self.image_frame = Frame(self.root)
        self.image_frame.pack()

        # Create a label to display the image
        self.image_label = Label(self.image_frame)
        self.image_label.pack()

        # Create buttons for image navigation
        self.prev_button = Button(self.root, text="Previous", command=self.load_previous_image)
        self.prev_button.pack(side="left")

        self.next_button = Button(self.root, text="Next", command=self.load_next_image)
        self.next_button.pack(side="right")

        # Create a button to open the file dialog
        self.open_button = Button(self.root, text="Open Image", command=self.open_image)
        self.open_button.pack()

        # Create a button to delete the current image
        self.delete_button = Button(self.root, text="Delete Image", command=self.delete_image)
        self.delete_button.pack()

        # Initialize variables
        self.image_index = 0
        self.images = []

    def open_image(self):
        # Open a file dialog to select the image
        filetypes = (("Image Files", "*.jpg;*.jpeg;*.png;*.gif"), ("All Files", "*.*"))
        image_file = filedialog.askopenfilename(filetypes=filetypes)

        if image_file:
            # Load the image using PIL
            image = Image.open(image_file)
            image.thumbnail((800, 800))  # Resize the image for display

            # Convert the PIL image to Tkinter PhotoImage
            image_tk = ImageTk.PhotoImage(image)

            # Store the image file and PhotoImage in the list
            self.images.append((image_file, image_tk))

            # Display the loaded image
            self.load_image()

    def load_image(self):
        # Get the current image file and Tkinter PhotoImage
        image_file, image_tk = self.images[self.image_index]

        # Update the image label
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

        # Update the window title with the image file name
        self.root.title(f"Image Viewer - {os.path.basename(image_file)}")

        # Enable or disable the previous/next buttons based on the current image index
        self.prev_button.config(state="normal" if self.image_index > 0 else "disabled")
        self.next_button.config(state="normal" if self.image_index < len(self.images) - 1 else "disabled")

    def load_previous_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.load_image()

    def load_next_image(self):
        if self.image_index < len(self.images) - 1:
            self.image_index += 1
            self.load_image()

    def delete_image(self):
        if self.images:
            # Remove the current image from the list
            del self.images[self.image_index]

            # Adjust the image index if necessary
            if self.image_index >= len(self.images):
                self.image_index = len(self.images) - 1

            # Load the new current image or clear the display if no images left
            if self.images:
                self.load_image()
            else:
                self.clear_image()

    def clear_image(self):
        # Clear the image label
        self.image_label.configure(image=None)

        # Update the window title
        self.root.title("Image Viewer")

        # Disable the previous/next buttons
        self.prev_button.config(state="disabled")
        self.next_button.config(state="disabled")

# Create the Tkinter root window
root = Tk()

# Create the image viewer instance
image_viewer = ImageViewer(root)

# Start the Tkinter event loop
root.mainloop()
