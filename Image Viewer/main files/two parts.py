from tkinter import Tk, Frame, Label

def create_widgets(root):
    # Create a frame for the left part with background color
    left_frame = Frame(root, width=200, height=200, bg="lightblue")
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Create a label in the left frame
    left_label = Label(left_frame, text="Left Part")
    left_label.pack()

    # Create a frame for the right part with background color
    right_frame = Frame(root, width=200, height=200, bg="lightgreen")
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    # Create a label in the right frame
    right_label = Label(right_frame, text="Right Part")
    right_label.pack()

def main():
    # Create the Tkinter root window
    root = Tk()

    # Set the window title
    root.title("Divided Window")

    # Set the window size
    root.geometry("500x300")

    # Configure grid row and column weights
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Call the function to create the widgets
    create_widgets(root)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
