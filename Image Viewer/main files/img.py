import cv2

img = cv2.imread(r'G:\allpic\hh\BoywithUke.jpg')
print(img)
edited_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img)
cv2.imshow('edit', edited_image)

cv2.waitKey()


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
    self.edit_frame.grid(row=0, column=1, rowspan=1, sticky='e')

    # Create a frame2 for the editing section
    self.edit_frame2 = Frame(self.root, bg='#CFCFCF')
    self.edit_frame2.grid(row=1, column=1, rowspan=1, sticky='en')

    # Create buttons for image navigation
    self.prev_button = Button(self.image_button_frame, text="Previous", command=self.load_previous_image,
                              width=40, bg='#BDBFBF')
    self.prev_button.pack(side="left", padx=5, pady=5)

    self.next_button = Button(self.image_button_frame, text="Next", command=self.load_next_image,
                              width=40, bg='#BDBFBF')
    self.next_button.pack(side="right", padx=5, pady=5)

    # Create a button to open the file dialog
    self.open_button = Button(self.edit_frame, text="Open Image", command=self.open_image,
                              bg='#BDBFBF')
    self.open_button.pack(side='right', padx=5, pady=5)

    # Create a button to delete the current image
    self.delete_button = Button(self.edit_frame, text="Delete Image", command=self.delete_image,
                                bg='#BDBFBF')
    self.delete_button.pack(side='right', padx=5, pady=5)

    self.edit_button = Button(self.edit_frame2, text="Edit", command=self.edit_image,
                              width=10, bg='#BDBFBF')
    self.edit_button.pack(side='top', padx=5, pady=5)
    self.edit_button.config(state='disabled')

    self.save_image_button = Button(self.edit_frame2, text="Save Image", command=self.save_image,
                                    width=10, bg='#BDBFBF')
    self.save_image_button.pack(side='bottom', padx=5, pady=5)
    self.save_image_button.config(state='disabled')

    # Initialize variables
    self.images = []
    self.image_index = 0
