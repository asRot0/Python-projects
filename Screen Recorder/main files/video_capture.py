import cv2
import numpy as np
import pyautogui
import tkinter as tk


def capture_and_display_frames(out, live_canvas, recording):
    while recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        # Display the recording on the canvas
        frame = cv2.resize(frame, (480, 270))
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.imencode('.png', img)[1].tobytes()
        display_image(img, live_canvas)

    out.release()


def display_image(image_data, live_canvas):
    # Display the image on the canvas
    image = tk.PhotoImage(data=image_data)
    live_canvas.create_image(0, 0, anchor="nw", image=image)
    live_canvas.image = image
