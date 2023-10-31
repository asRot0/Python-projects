import customtkinter as ctk
import settings

class Calculator(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()

        ctk.set_appearance_mode('dark')
        # self.attributes('-alpha', 0.7)
        self.geometry(f'{settings.app_size[0]}x{settings.app_size[1]}')
        self.resizable(False, False)


        self.mainloop()


if __name__ == '__main__':
    Calculator()