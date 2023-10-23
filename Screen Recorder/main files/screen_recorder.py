import threading
import cv2
from gui_elements import create_control_frame, create_live_video_canvas
from video_capture import capture_and_display_frames

class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('../pics/line.ico')
        self.root.attributes("-alpha", 0.9)
        self.root.title("Screen Recorder")
        self.root.config(bg="#f5f5f5")
        self.root.resizable(False, False)

        self.recording = False
        self.resolution = (1920, 1080)
        self.filename = "Recording.avi"
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.recording_thread = None  # To hold the recording thread

        # Create GUI elements
        self.control_frame = create_control_frame(self.root, self)
        self.live_canvas = create_live_video_canvas(self.root)

        self.recording_thread = None

    def start_recording(self):
        self.recording = True
        self.fpsvalue = int(self.control_frame.fps.get())
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fpsvalue, self.resolution)

        capture_and_display_frames(self.out, self.live_canvas, self.recording)

    def stop_recording(self):
        # Stop the recording
        self.recording = False
        self.out.release()


    def toggle_recording(self):
        # Toggle the recording state when the button is pressed
        if not self.recording:
            self.control_frame.record_button["text"] = "Stop Recording"
            recording_thread = threading.Thread(target=self.start_recording)
            recording_thread.start()
        else:
            self.control_frame.record_button["text"] = "Start Recording"
            self.stop_recording()

