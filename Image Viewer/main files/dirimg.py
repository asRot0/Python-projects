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

        # Initialize variables
        self.images = []
        self.image_index = 0

    def open_image(self):
        # Open a file dialog to select a directory
        directory = filedialog.askdirectory()

        if directory:
            # Get a list of image files in the selected directory
            image_files = [file for file in os.listdir(directory) if
                           file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if image_files:
                # Sort the image files alphabetically
                image_files.sort()

                # Load and store the images
                self.images = []
                for file in image_files:
                    # Construct the full file path
                    file_path = os.path.join(directory, file)

                    # Load the image using PIL
                    image = Image.open(file_path)
                    image.thumbnail((800, 800))  # Resize the image for display

                    # Convert the PIL image to Tkinter PhotoImage
                    image_tk = ImageTk.PhotoImage(image)

                    # Store the file path and PhotoImage in the list
                    self.images.append((file_path, image_tk))

                # Display the first image
                self.load_image()

    def load_image(self):
        if self.images:
            # Get the current image file and Tkinter PhotoImage
            file_path, image_tk = self.images[self.image_index]

            # Update the image label
            self.image_label.configure(image=image_tk)
            self.image_label.image = image_tk

            # Update the window title with the image file name
            self.root.title(f"Image Viewer - {os.path.basename(file_path)}")

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


# Create the Tkinter root window
window = Tk()

# Create the image viewer instance
image_viewer = ImageViewer(window)

# Start the Tkinter event loop
window.mainloop()
