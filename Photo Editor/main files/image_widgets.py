import customtkinter as ctk
from tkinter import filedialog
import settings


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')
        self.import_func = import_func

        ctk.CTkButton(self, text='open image', command=self.open_dialog, fg_color=settings.BUTTON_COLOR,
                      hover_color=settings.BUTTON_HOVER_COLOR).pack(expand=True)

    def open_dialog(self):
        path = filedialog.askopenfilename()
        self.import_func(path)


class ImageOutput(ctk.CTkCanvas):
    def __init__(self, parent, resize_image):
        super().__init__(master=parent, background=settings.BACKGROUND_COLOR,  relief='ridge',
                         bd=0, highlightthickness=0)
        self.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        self.bind('<Configure>', resize_image)


class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master=parent, command=close_func, text='X', text_color=settings.WHITE,
                         fg_color='transparent', width=40, height=40, corner_radius=0,
                         hover_color=settings.CLOSE_RED)
        self.place(relx=0.99, rely=0.02, anchor='ne')