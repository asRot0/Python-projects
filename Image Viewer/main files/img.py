def edit_image(self, file_path, image_tk):
    if self.images:
        # Retrieve the file path and Tkinter PhotoImage
        # file_path, _ = self.images[self.image_index]

        # Convert Tkinter image back to Pillow image
        edited_image = ImageTk.getimage(image_tk)

        # Convert the edited image to a NumPy array
        edited_image_np = np.array(edited_image)

        # Convert the image to grayscale using OpenCV
        edited_image_gray = cv2.cvtColor(edited_image_np, cv2.COLOR_BGR2GRAY)

        # Apply brightness adjustment
        brightness_factor = 1.5  # Increase brightness by a factor of 1.5
        adjusted_image = cv2.convertScaleAbs(edited_image_gray, alpha=brightness_factor, beta=0)

        # Convert the adjusted image back to PIL format
        adjusted_image_pil = Image.fromarray(adjusted_image)

        # Convert the adjusted image to Tkinter PhotoImage
        adjusted_image_tk = ImageTk.PhotoImage(adjusted_image_pil)

        # Update the image label in the main window
        self.image_label.configure(image=adjusted_image_tk)
        self.image_label.image = adjusted_image_tk

        # Update the image in the images list
        self.images[self.image_index] = (file_path, adjusted_image_tk)
