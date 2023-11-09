import customtkinter as ctk
from image_widgets import ImageImport, ImageOutput, CloseOutput
from menu import Menu
from PIL import Image, ImageTk
import settings


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        self.image = None
        self.image_ratio = None
        self.image_tk = None
        self.image_output = None

        # layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # widgets
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def init_parameters(self):
        self.ratate_float = ctk.DoubleVar(value=settings.ROTATE_DEFAULT)



    def import_image(self, path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_remove()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self)

    def resize_image(self, event):
        canvas_ratio = event.width / event.height

        # resize
        if canvas_ratio > self.image_ratio:
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else:
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)

        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2, event.height / 2, image=self.image_tk)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import.grid()


App()
