import customtkinter as ctk
import settings

class Calculator(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()

        ctk.set_appearance_mode('dark')
        self.attributes('-alpha', settings.alpha)
        self.geometry(f'{settings.app_size[0]}x{settings.app_size[1]}')
        self.resizable(False, False)
        self.iconbitmap(settings.title_ico)
        self.title('Calculator')

        self.mainloop()


if __name__ == '__main__':
    Calculator()