import customtkinter as ctk
from button import Button, ImageButton, NumButton, MathButton, MathImageButton
import settings
from PIL import Image


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

        # grid layout
        self.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        self.columnconfigure((0,1,2,3), weight=1, uniform='a')
        self.columnconfigure(4, weight=2, uniform='a')

        # data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='')
        self.display_nums = []
        self.full_operation = []

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=settings.FONT, size=settings.NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=settings.FONT, size=settings.OUTPUT_FONT_SIZE)

        # output labels
        OutputLabel(self, 0, 'se', main_font, self.formula_string)
        OutputLabel(self, 1, 'e', result_font, self.result_string)

        # Clear (C) button
        Button(parent=self, text=settings.OPERATORS['clear']['text'], func=self.clear,
               col=settings.OPERATORS['clear']['col'], row=settings.OPERATORS['clear']['row'],
               font=main_font)

        # percentage button
        Button(parent=self, text=settings.OPERATORS['percent']['text'], func=self.percent,
               col=settings.OPERATORS['percent']['col'], row=settings.OPERATORS['percent']['row'],
               font=main_font)

        # invert button
        invert_image = ctk.CTkImage(dark_image=Image.open(settings.OPERATORS['invert']['image path']))
        ImageButton(parent=self, func=self.invert, col=settings.OPERATORS['invert']['col'],
                    row=settings.OPERATORS['invert']['row'], image=invert_image)

        # back button
        back_image = ctk.CTkImage(dark_image=Image.open(settings.OPERATORS['back']['image path']))

        ImageButton(parent=self, func=self.back, col=settings.OPERATORS['back']['col'],
                    row=settings.OPERATORS['back']['row'], image=back_image, color='dark-gray')

        # number buttons
        for num, data in settings.NUM_POSITIONS.items():
            NumButton(parent=self, text=num, func=self.num_press,
                      col=data['col'], row=data['row'], font=main_font)

        # math buttons
        for operator, data, in settings.MATH_POSITIONS.items():
            if data['image path']:
                image_button = ctk.CTkImage(dark_image=Image.open(data['image path']))
                MathImageButton(parent=self, operator=operator, func=self.math_press,
                                col=data['col'], row=data['row'], image=image_button)
            else:
                MathButton(parent=self, text=data['character'], operator=operator,
                           func=self.math_press,  col=data['col'], row=data['row'], font=main_font)

    def num_press(self, value):
        self.display_nums.append(str(value))
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)

    def math_press(self, value):
        current_number = ''.join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update data
                self.full_operation.append(value)
                self.display_nums.clear()

                # update output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))

            else:
                formula = ' '.join(self.full_operation)
                result = eval(formula)

                # format the result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)

                # update data
                self.full_operation.clear()
                self.display_nums = [str(result)]

                # update output
                self.result_string.set(result)
                self.formula_string.set(formula)

    def clear(self):
        # clear the output
        self.result_string.set(0)
        self.formula_string.set('')

        # clear the data
        self.display_nums.clear()
        self.full_operation.clear()

    def percent(self):
        if self.display_nums:
            current_number = float(''.join(self.display_nums))
            percent_number = current_number / 100

            self.display_nums = list(str(percent_number))
            self.result_string.set(''.join(self.display_nums))

    def invert(self):
        current_number = ''.join(self.display_nums)

        if current_number:
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                if len(self.display_nums) > 1:
                    del self.display_nums[0]
                else:
                    self.display_nums[:] = self.display_nums[0][1:]

            self.result_string.set(''.join(self.display_nums))

    def back(self):
        print(self.display_nums)
        del self.display_nums[-1]
        print(self.display_nums)
        self.result_string.set(''.join(self.display_nums))


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, side, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=side, padx=10)


if __name__ == '__main__':
    Calculator()