import os
from tkinter import Tk, Frame, Label, Button, filedialog, Toplevel
from PIL import ImageTk, Image
import cv2
import numpy as np


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Create a frame to hold the next and previous button
        self.image_button_frame = Frame(self.root, bg='#CFCFCF')
        self.image_button_frame.grid(row=0, column=0, sticky='w', pady=1)

        # Create a frame to hold the image display
        self.image_frame = Frame(self.root, bg='#9B9C9C')
        self.image_frame.grid(row=1, column=0, sticky='w')

        # Create a label to display the image
        self.image_label = Label(self.image_frame, bg='#9B9C9C')
        self.image_label.pack(fill='both', expand=True)

        # Create a frame for the editing section
        self.edit_frame = Frame(self.root, bg='#CFCFCF')
        self.edit_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')

        self.edit_frame2 = Frame(self.root, bg='#CFCFCF')
        self.edit_frame2.grid(row=2, column=1, rowspan=1, sticky='nsew')

        # Create buttons for image navigation
        self.prev_button = Button(self.image_button_frame, text="Previous", width=40, bg='#BDBFBF')
        self.prev_button.pack(side="left", padx=5, pady=5)

        self.next_button = Button(self.image_button_frame, text="Next", width=40, bg='#BDBFBF')
        self.next_button.pack(side="right", padx=5, pady=5)

        # Create a button to open the file dialog
        self.open_button = Button(self.edit_frame, text="Open Image", bg='#BDBFBF')
        self.open_button.pack(side='right', padx=5, pady=5)

        # Create a button to delete the current image
        self.delete_button = Button(self.edit_frame, text="Delete Image", bg='#BDBFBF',
                                    state="disabled")
        self.delete_button.pack(side='right', padx=5, pady=5)

        # Create a button to apply edits to the current image
        self.apply_button = Button(self.edit_frame, text="Apply Edits", bg='#BDBFBF',
                                   state="disabled")
        self.apply_button.pack(side='right', padx=5, pady=5)

        self.save_image_button = Button(self.edit_frame2, text="Save Image", bg='#BDBFBF',
                                        state="disabled")
        self.save_image_button.pack(side='left', padx=5, pady=5)

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
                    root_width = self.root.winfo_width()
                    root_height = self.root.winfo_height()
                    new_width = int(root_width * 0.8)
                    new_height = int(root_height * 0.8)

                    image.thumbnail((new_width, new_height), Image.LANCZOS)  # Resize the image for display

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

            # Enable the edit save and delete buttons
            self.apply_button.config(state="normal")
            self.save_image_button.config(state="normal")
            self.delete_button.config(state="normal")

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

            if self.images:
                # If there are remaining images, update the image display
                if self.image_index >= len(self.images):
                    self.image_index = len(self.images) - 1
                self.load_image()
            else:
                # If there are no remaining images, clear the image display
                self.clear_image()

    def clear_image(self):
        # Clear the image label
        self.image_label.configure(image=None)
        self.image_label.image = None

        # Update the window title
        self.root.title("Image Viewer")

        # Disable the previous/next buttons
        self.prev_button.config(state="disabled")
        self.next_button.config(state="disabled")

    def apply_edits(self):
        if self.images:
            # Get the current image file path
            file_path, image_tk = self.images[self.image_index]

            # Create a new Toplevel window for editing
            edit_window = Toplevel(self.root)
            edit_window.title("Image Editor")
            edit_window.geometry('300x300')
            edit_window.resizable(False, False)

            # Create a button to apply the edits and update the main window image
            apply_button = Button(edit_window, text="Apply", command=lambda: self.edit_image(file_path))
            apply_button.pack(padx=5, pady=5)

            # Close the edit window when the main window is closed
            edit_window.protocol("WM_DELETE_WINDOW", edit_window.destroy)

    def edit_image(self, file_path):
        if self.images:
            # Retrieve the file path and Tkinter PhotoImage
            # file_path, _ = self.images[self.image_index]

            # Reload the edited image using PIL
            edited_image = Image.open(file_path)

            # Convert the edited image to a NumPy array
            edited_image_np = np.array(edited_image)

            # Apply the color conversion using OpenCV
            edited_img = cv2.cvtColor(edited_image_np, cv2.COLOR_BGR2GRAY)

            # Convert the edited image back to PIL format
            edited_image_pil = Image.fromarray(edited_img)

            # Convert the edited image to Tkinter PhotoImage
            edited_image_tk = ImageTk.PhotoImage(edited_image_pil)

            # Update the image label in the main window
            self.image_label.configure(image=edited_image_tk)
            self.image_label.image = edited_image_tk

            # Update the image in the images list
            self.images[self.image_index] = (file_path, edited_image_tk)

    def save_image(self):
        if self.images:
            # Get the current image file path
            file_path, _ = self.images[self.image_index]

            # Open the file dialog to select a save location
            save_path = filedialog.asksaveasfilename(defaultextension=".png")

            if save_path:
                # Save the image
                image = Image.open(file_path)
                image.save(save_path)


# Create the Tkinter root window
window = Tk()

# Set the window size
window.geometry('1000x500')
window.resizable(False, False)
window.config(bg='#9B9C9C')

# Configure grid row and column weights
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=0)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)

# Create the image viewer instance
image_viewer = ImageViewer(window)

# Bind the buttons to their respective functions
image_viewer.open_button.config(command=image_viewer.open_image)
image_viewer.prev_button.config(command=image_viewer.load_previous_image)
image_viewer.next_button.config(command=image_viewer.load_next_image)
image_viewer.delete_button.config(command=image_viewer.delete_image)
image_viewer.apply_button.config(command=image_viewer.apply_edits)
image_viewer.save_image_button.config(command=image_viewer.save_image)

# Start the Tkinter event loop
window.mainloop()
