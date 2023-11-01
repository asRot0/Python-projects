import customtkinter as ctk
from button import Button, ImageButton, NumButton, MathButton, MathImageButton, DeleteButton
import settings
from PIL import Image


class Calculator(ctk.CTk):
    def __init__(self):
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
        self.history_string = ctk.StringVar(value='There\'s no history yet')
        self.display_nums = []
        self.full_operation = []

        self.flag = False

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=settings.FONT, size=settings.NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=settings.FONT, size=settings.OUTPUT_FONT_SIZE)
        small_font = ctk.CTkFont(family=settings.FONT, size=settings.SMALL_FONT_SIZE)

        # output labels
        OutputLabel(self, 0, 'se', main_font, self.formula_string)
        OutputLabel(self, 1, 'e', result_font, self.result_string)
        HistoryFrame(self, 0, 'w', main_font, small_font, self.history_string)

        # history labels
        self.history_label = HistoryLabel(self, 'nsew', small_font)

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

        # delete button
        delete_image = ctk.CTkImage(dark_image=Image.open(settings.OPERATORS['delete']['image path']))
        self.delete_button = DeleteButton(parent=self, func=self.delete,  col=settings.OPERATORS['delete']['col'],
                                          row=settings.OPERATORS['delete']['row'], image=delete_image)
        self.delete_button.grid_remove()

    def num_press(self, value):

        if self.flag:
            self.display_nums.clear()
            self.full_operation.clear()
            self.flag = False

        self.display_nums.append(str(value))
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)

    def math_press(self, value):
        current_number = ''.join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update flag
                self.flag = False

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
                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                # update data
                self.full_operation.clear()
                self.display_nums = [str(result)]

                # update output
                self.result_string.set(result)
                self.formula_string.set(formula)

                # update flag
                self.flag = True
                self.history_string.set('')

                # update delete button
                self.delete_button.grid()

                # update the history section
                self.history_label.configure(state='normal')
                # self.history_text.delete('1.0', 'end')  # Clear previous history
                self.history_label.insert('1.0', f'{formula} = {result}\n\n')
                self.history_label.configure(state='disabled')

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
        del self.display_nums[-1]
        self.result_string.set(''.join(self.display_nums))

    def delete(self):
        # update the history section
        self.history_label.configure(state='normal')
        self.history_label.delete('1.0', 'end')  # Clear previous history
        self.history_label.configure(state='disabled')

        # update delete button
        self.delete_button.grid_remove()
        self.history_string.set(value='There\'s no history yet')


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, side, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=side, padx=10)


class HistoryFrame(ctk.CTkFrame):
    def __init__(self, parent, row, side, font1, font2, string_var):
        super().__init__(master=parent, fg_color='transparent')
        ctk.CTkLabel(self, text='History', font=font1).pack(padx=1, pady=5, anchor='w')
        ctk.CTkLabel(self, textvariable=string_var, font=font2).pack(pady=1)
        self.grid(column=4, row=row, rowspan=1, sticky=side, padx=10)


class HistoryLabel(ctk.CTkTextbox):
    def __init__(self, parent, side, font):
        super().__init__(master=parent, font=font, fg_color='transparent', state='disabled', wrap='none', padx=10)
        self.grid(column=4, row=1, rowspan=6, sticky=side, padx=0.5)


if __name__ == '__main__':
    Calculator()