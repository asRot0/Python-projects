import tkinter as tk
import threading
import cv2
import numpy as np
import pyautogui

class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.resolution = (1920, 1080)
        self.filename = "Recording.avi"
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.fps = tk.StringVar(value="60")  # Default FPS value

        # Create a frame for the control panel
        control_frame = tk.Frame(self.root, bg="#1E3C72", pady=10)
        control_frame.pack(side="top", fill='x')

        # Create labels and dropdown
        fps_label = tk.Label(control_frame, text="Select FPS:", fg="white", bg="#1E3C72")
        fps_label.grid(row=0, column=0, padx=10)

        fps_options = ["10", "15", "20", "24", "30", "60"]
        fps_dropdown = tk.OptionMenu(control_frame, self.fps, *fps_options)
        fps_dropdown.config(bg="#0D1B3D")
        fps_dropdown["menu"].config(bg="#0D1B3D")
        fps_dropdown.grid(row=0, column=1, padx=10)

        self.record_button = tk.Button(control_frame, text="Start Recording", command=self.toggle_recording, bg="#D90368", fg="white")
        self.record_button.grid(row=0, column=2, padx=10)

        # Create a frame for live video display
        live_frame = tk.Frame(self.root, bg="#2E2E2E")
        live_frame.pack(side="top", pady=10, expand=True, fill='both')

        # Create a canvas for smoother live video display
        self.live_canvas = tk.Canvas(live_frame, width=480, height=270, bg="#2E2E2E")
        self.live_canvas.grid(row=0, column=0, padx=10)

    def start_recording(self):
        self.recording = True
        self.fpsvalue = int(self.fps.get())
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fpsvalue, self.resolution)

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)

            # Display the recording on the canvas
            frame = cv2.resize(frame, (480, 270))
            img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.imencode('.png', img)[1].tobytes()
            self.display_image(img)

        self.out.release()

    def stop_recording(self):
        self.recording = False

    def toggle_recording(self):
        if not self.recording:
            self.record_button["text"] = "Stop Recording"
            self.record_button.config(bg="#00A86B")
            recording_thread = threading.Thread(target=self.start_recording)
            recording_thread.start()
        else:
            self.record_button["text"] = "Start Recording"
            self.record_button.config(bg="#D90368")
            self.stop_recording()

    def display_image(self, image_data):
        image = tk.PhotoImage(data=image_data)
        self.live_canvas.create_image(0, 0, anchor="nw", image=image)
        self.live_canvas.image = image

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()
