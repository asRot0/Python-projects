import os
from tkinter import Tk, Frame, Label, Button, filedialog, Toplevel, Scale, HORIZONTAL, \
    Checkbutton, BooleanVar, font
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
        self.next_button.pack(side="left", padx=5, pady=5)

        # Create a frame for the buttons
        self.buttons_frame = Frame(self.edit_frame, bg='#CFCFCF')
        self.buttons_frame.pack(side='top', pady=5)

        # Create a button to open the file dialog
        self.open_button = Button(self.buttons_frame, text="Open Image", bg='#BDBFBF')
        self.open_button.pack(side='left', padx=5, pady=5)

        # Create a button to delete the current image
        self.delete_button = Button(self.buttons_frame, text="Delete Image", bg='#BDBFBF',
                                    state="disabled")
        self.delete_button.pack(side='left', padx=5, pady=5)

        # Create a button to apply edits to the current image
        self.apply_button = Button(self.buttons_frame, text="Apply Edits", bg='#BDBFBF',
                                   state="disabled")
        self.apply_button.pack(side='left', padx=5, pady=5)

        # Create a label for image info
        self.image_info_label = Label(self.edit_frame, text="INFO", bg='#BDBFBF', justify='left')
        self.image_info_label.pack(side='top', padx=5, pady=5, anchor='nw')

        # Create a button to save the current image
        self.save_image_button = Button(self.edit_frame2, text="Save Image", bg='#BDBFBF',
                                        state="disabled")
        self.save_image_button.pack(side='left', padx=5, pady=5)

        # Create a checkbutton for resizable option
        self.resizable_var = BooleanVar()
        self.resizable_var.set(False)  # Initial value is not resizable

        self.resizable_checkbutton = Checkbutton(self.edit_frame2, text="Resizable",
                                                 variable=self.resizable_var,
                                                 command=self.toggle_resizable,
                                                 bg='#CFCFCF', font=font.Font(size=8))
        self.resizable_checkbutton.pack(side='left', padx=5, pady=5)

        # Initialize variables
        self.images = []
        self.image_index = 0

    def toggle_resizable(self):
        resizable = self.resizable_var.get()
        self.root.resizable(resizable, resizable)

    def open_image(self):
        # Open a file dialog to select a directory
        directory = filedialog.askdirectory()

        if directory:
            # Get a list of image files in the selected directory
            image_files = [file for file in os.listdir(directory) if
                           file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.jfif', '.bmp', '.tiff', '.ico'))]

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
                self.image_index = 0
                self.load_image()
            else:
                # If no valid image files found, clear the images
                self.clear_images()
        else:
            # If no directory selected, clear the images
            self.clear_images()

    def clear_images(self):
        # Clear the images list
        self.images = []

        # Clear the image label
        self.clear_image()

    def load_image(self):
        if self.images and self.image_index < len(self.images):
            # Get the current image file and Tkinter PhotoImage
            file_path, image_tk = self.images[self.image_index]

            # Update the image label
            self.image_label.configure(image=image_tk)
            self.image_label.image = image_tk

            # Update the window title with the image file name
            self.root.title(f"Image Viewer - {os.path.basename(file_path)}")

            # update the info box
            self.update_image_info(file_path, image_tk)

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

    def update_image_info(self, file_path, image_tk):
        # Extract and display the image info in the label
        directory_name = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)

        # Split the directory name into multiple lines with 32 characters per line
        lines = [directory_name[i:i+32] for i in range(0, len(directory_name), 32)]
        directory_name_formatted = '\n'.join(lines)

        # Split the file name into multiple lines with 32 characters per line
        lines = [file_name[i:i+32] for i in range(0, len(file_name), 32)]
        file_name_formatted = '\n'.join(lines)

        width = image_tk.width()
        height = image_tk.height()

        file_info = f"Directory: {directory_name_formatted}\n"
        file_info += f"File Name: {file_name_formatted}\n"
        file_info += f"Size: {width} x {height} -- modified"
        # file_info += f"File: {file_path}"
        self.image_info_label.config(text=file_info, justify='left')

    def apply_edits(self):
        if self.images:
            # Get the current image file path
            file_path, image_tk = self.images[self.image_index]

            # Create a new Toplevel window for editing
            edit_window = Toplevel(self.root)
            edit_window.title("Image Editor")
            edit_window.geometry('300x300')
            edit_window.resizable(False, False)

            # Create Scale widgets to adjust the editing parameters
            brightness_scale = Scale(edit_window, from_=0, to=255, orient=HORIZONTAL, label="Brightness")
            brightness_scale.pack(padx=5, pady=5)

            contrast_scale = Scale(edit_window, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, label="Contrast")
            contrast_scale.pack(padx=5, pady=5)

            # Create a button to apply the edits and update the main window image
            apply_button = Button(edit_window, text="Apply",
                                  command=lambda: self.apply_edits_params(file_path,
                                                                          image_tk, brightness_scale.get(),
                                                                          contrast_scale.get()))
            apply_button.pack(padx=5, pady=5)

            # Close the edit window when the main window is closed
            edit_window.protocol("WM_DELETE_WINDOW", edit_window.destroy)

    def apply_edits_params(self, file_path, image_tk, brightness, contrast):
        if self.images:
            # Retrieve the file path and Tkinter PhotoImage
            # file_path, _ = self.images[self.image_index]

            # Convert Tkinter image back to Pillow image
            edited_image = ImageTk.getimage(image_tk)

            # Convert the edited image to a NumPy array
            edited_image_np = np.array(edited_image)

            # Apply brightness and contrast adjustments using OpenCV
            edited_image_np = cv2.cvtColor(edited_image_np, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            edited_image_np = cv2.convertScaleAbs(edited_image_np, alpha=contrast, beta=brightness)

            # Convert the edited image back to PIL format
            edited_image_pil = Image.fromarray(edited_image_np)

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
            _, edited_img = self.images[self.image_index]

            # Convert Tkinter image back to Pillow image
            pil_image = ImageTk.getimage(edited_img)

            # Open the file dialog to select a save location
            save_path = filedialog.asksaveasfilename(defaultextension=".png")

            if save_path:
                # Save the image
                # image = Image.open(file_path)
                # image.save(save_path)
                pil_image.save(save_path)


# Create the Tkinter root window
window = Tk()

# Set the window size
window.geometry('1040x520')
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
