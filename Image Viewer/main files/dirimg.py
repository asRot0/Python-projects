import os
from tkinter import Tk, Frame, Label, Button, filedialog, Toplevel
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Create a frame to hold the image display
        self.image_frame = Frame(self.root, bg="lightgray")
        self.image_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        # Create a label to display the image
        self.image_label = Label(self.image_frame)
        self.image_label.pack(fill="both", expand=True)

        # Create buttons for image navigation
        self.prev_button = Button(self.image_frame, text="Previous", command=self.load_previous_image)
        self.prev_button.pack(side="left", padx=5, pady=5)

        self.next_button = Button(self.image_frame, text="Next", command=self.load_next_image)
        self.next_button.pack(side="right", padx=5, pady=5)

        # Create a button to open the file dialog
        self.open_button = Button(self.image_frame, text="Open Image", command=self.open_image)
        self.open_button.pack(padx=5, pady=5)

        # Create a button to save the image
        self.save_button = Button(self.image_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(padx=5, pady=5)

        # Create a button to edit the image
        self.edit_button = Button(self.image_frame, text="Edit Image", command=self.open_edit_window)
        self.edit_button.pack(padx=5, pady=5)

        # Initialize variables
        self.images = []
        self.image_index = 0

    def open_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])

        if file_path:
            # Load the image using PIL
            image = Image.open(file_path)

            # Convert the PIL image to Tkinter PhotoImage
            image_tk = ImageTk.PhotoImage(image)

            # Update the image label
            self.image_label.configure(image=image_tk)
            self.image_label.image = image_tk

            # Store the image file path and Tkinter PhotoImage
            self.images.append((file_path, image_tk))

            # Update the image index and enable/disable navigation buttons
            self.image_index = len(self.images) - 1
            self.prev_button.config(state="normal")
            self.next_button.config(state="disabled")

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

    def open_edit_window(self):
        if self.images:
            # Get the current image file path and Tkinter PhotoImage
            file_path, image_tk = self.images[self.image_index]

            # Create a new Toplevel window for editing
            edit_window = Toplevel(self.root)
            edit_window.title("Image Editor")

            # Create a label to display the image in the edit window
            image_label = Label(edit_window, image=image_tk)
            image_label.pack()

            # Create a button to apply the edits and update the main window image
            apply_button = Button(edit_window, text="Apply", command=lambda: self.apply_edits(file_path))
            apply_button.pack(padx=5, pady=5)

            # Close the edit window when the main window is closed
            edit_window.protocol("WM_DELETE_WINDOW", edit_window.destroy)

    def apply_edits(self, file_path):
        # Reload the edited image using PIL
        edited_image = Image.open(file_path)

        # Convert the edited image to Tkinter PhotoImage
        edited_image_tk = ImageTk.PhotoImage(edited_image)

        # Update the image label in the main window
        self.image_label.configure(image=edited_image_tk)
        self.image_label.image = edited_image_tk

        # Update the image in the images list
        self.images[self.image_index] = (file_path, edited_image_tk)

    def load_previous_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.load_image()

    def load_next_image(self):
        if self.image_index < len(self.images) - 1:
            self.image_index += 1
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

# Create the Tkinter root window
root = Tk()

# Create the image viewer instance
image_viewer = ImageViewer(root)

# Start the Tkinter event loop
root.mainloop()
