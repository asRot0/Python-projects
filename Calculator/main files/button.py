from customtkinter import CTkButton
import settings


class Button(CTkButton):
    def __init__(self, parent, text, func,  col, row, font, color='dark-gray'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=settings.styling['corner_radius'],
            font=font,
            fg_color=settings.COLORS[color]['fg'],
            hover_color=settings.COLORS[color]['hover'],
            text_color=settings.COLORS[color]['text'])
        self.grid(column=col, row=row, sticky='nsew', padx=settings.styling['gap'], pady=settings.styling['gap'])


class NumButton(Button):
    def __init__(self, parent, text, func,  col, row, font, color='light-gray'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(text),
            col=col,
            row=row,
            font=font,
            color=color)


class MathButton(Button):
    def __init__(self, parent, text, operator, func,  col, row, font, color='orange'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(operator),
            col=col,
            row=row,
            font=font,
            color=color)


class ImageButton(CTkButton):
    def __init__(self, parent, func,  col, row, image, text='', color='dark-gray'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            image=image,
            corner_radius=settings.styling['corner_radius'],
            fg_color=settings.COLORS[color]['fg'],
            hover_color=settings.COLORS[color]['hover'],
            text_color=settings.COLORS[color]['text'])
        self.grid(column=col, row=row, sticky='nsew', padx=settings.styling['gap'], pady=settings.styling['gap'])


class MathImageButton(ImageButton):
    def __init__(self, parent, operator, func, col, row, image, color='orange'):
        super().__init__(
            parent=parent,
            func=lambda: func(operator),
            col=col,
            row=row,
            image=image,
            color=color)