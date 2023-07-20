import tkinter as tk

def process_input():
    input_text = text_widget.get("1.0", "end-1c")
    print("Input Text:")
    print(input_text)

root = tk.Tk()
root.title("Multi-Line Input")

# Create a Text widget
text_widget = tk.Text(root, font=('Arial', 14), wrap='word', width=40, height=10)
text_widget.pack(padx=10, pady=10)

# Create a button to process the input
process_button = tk.Button(root, text="Process Input", command=process_input)
process_button.pack(pady=5)

root.mainloop()
