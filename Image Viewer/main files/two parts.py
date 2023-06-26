from tkinter import Tk, Frame, Label

def create_widgets(root):
    # Create a frame for the left part
    left_frame = Frame(root, width=200, height=200)
    left_frame.grid(row=0, column=0, padx=10, pady=10)

    # Create a label in the left frame
    left_label = Label(left_frame, text="Left Part")
    left_label.pack(side="left")

    # Create a frame for the right part
    right_frame = Frame(root, width=200, height=200)
    right_frame.grid(row=0, column=1, padx=10, pady=10)

    # Create a label in the right frame
    right_label = Label(right_frame, text="Right Part")
    right_label.pack(side="right")

def main():
    # Create the Tkinter root window
    root = Tk()

    # Set the window title
    root.title("Divided Window")
    root.geometry('400x400')
    # Call the function to create the widgets
    create_widgets(root)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
