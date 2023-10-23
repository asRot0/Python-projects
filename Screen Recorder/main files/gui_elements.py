import tkinter as tk
from tkinter import ttk


def create_control_frame(root, app):
    control_frame = tk.Frame(root, bg="#424242", pady=10)
    control_frame.pack(fill="x")

    fps_label = tk.Label(control_frame, text="Select FPS:", bg="#424242", fg="white", font=("Arial", 12))
    fps_label.pack(side="left", padx=10)

    style = ttk.Style()
    style.configure("TMenubutton", background="#424242", foreground="white", font=("Arial", 12))
    style.configure("Menubutton.dropdown", background="#424242", foreground="white", font=("Arial", 12))

    fps_options = ["60", "10", "15", "20", "24", "30", "60"]
    fps = tk.StringVar(value="60")
    fps_dropdown = ttk.OptionMenu(control_frame, fps, *fps_options)
    fps_dropdown.pack(side="left")

    record_button = tk.Button(control_frame, text="Start Recording", command=app.toggle_recording,
                              bg="#2196f3", fg="white", font=("Arial", 12))
    record_button.pack(side="left", padx=10)

    control_frame.fps = fps
    control_frame.record_button = record_button
    return control_frame


def create_live_video_canvas(root):
    live_frame = tk.Frame(root, bg="#212121", pady=10)
    live_frame.pack(fill="both", expand=True)

    live_canvas = tk.Canvas(live_frame, width=480, height=270, bg="#212121", relief="ridge",
                            highlightbackground="#212121")
    live_canvas.pack()

    return live_canvas

