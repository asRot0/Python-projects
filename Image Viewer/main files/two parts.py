from tkinter import Tk, Frame, Label

def create_widgets(root):
    # Create a frame for the left part
    left_frame = Frame(root, width=200, height=200)
    left_frame.pack(side="left", padx=10, pady=10)

    # Create a label in the left frame
    left_label = Label(left_frame, text="Left Part")
    left_label.pack(anchor="w")

    # Create a frame for the right part
    right_frame = Frame(root, width=200, height=200)
    right_frame.pack(side="right", padx=10, pady=10)

    # Create a label in the right frame
    right_label = Label(right_frame, text="Right Part")
    right_label.pack(anchor="e")

def main():
    # Create the Tkinter root window
    root = Tk()

    # Set the window title
    root.title("Divided Window")

    # Set the window size
    root.geometry("500x300")

    # Call the function to create the widgets
    create_widgets(root)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
