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
            text_color=settings.COLORS[color]['text']
        )
        self.grid(column=col, row=row, sticky='nsew', padx=settings.styling['gap'], pady=settings.styling['gap'])


class ImageButton(CTkButton):
    def __init__(self, parent, text, func,  col, row, image, color='dark-gray'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            image=image,
            corner_radius=settings.styling['corner_radius'],
            fg_color=settings.COLORS[color]['fg'],
            hover_color=settings.COLORS[color]['hover'],
            text_color=settings.COLORS[color]['text']
        )
        self.grid(column=col, row=row, sticky='nsew', padx=settings.styling['gap'], pady=settings.styling['gap'])
