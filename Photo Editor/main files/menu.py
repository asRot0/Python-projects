import customtkinter as ctk
from panels import SliderPanel, SegmentedPanel, SwitchPanel, FileNamePanel, FilePathPanel,\
    DropDownPanel, RevertButton, SaveButton
import settings


class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars, export_image):
        super().__init__(master=parent, fg_color=settings.MENU_BG, segmented_button_selected_color=settings.BUTTON_BG,
                         segmented_button_selected_hover_color=settings.BUTTON_BG_HOVER,
                         segmented_button_unselected_hover_color=settings.BUTTON_BG_HOVER)
        self.grid(row=0, column=0, sticky='nsew', padx=5, pady=10)

        # tabs
        self.add('Position')
        self.add('Color')
        self.add('Effects')
        self.add('Export')

        # widgets
        PositionFrame(self.tab('Position'), pos_vars)
        ColorFrame(self.tab('Color'), color_vars)
        EffectFrame(self.tab('Effects'), effect_vars)
        ExportFrame(self.tab('Export'), export_image)


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Rotation', pos_vars['rotate'], 0, 360)
        SliderPanel(self, 'Zoom', pos_vars['zoom'], 0, 200)
        SegmentedPanel(self, 'Invert', pos_vars['flip'], settings.FLIP_OPTIONS)
        RevertButton(self, (pos_vars['rotate'], settings.ROTATE_DEFAULT),
                     (pos_vars['zoom'], settings.ZOOM_DEFAULT),
                     (pos_vars['flip'], settings.FLIP_OPTIONS[0]))


class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SwitchPanel(self, (color_vars['grayscale'], 'B/W'), (color_vars['invert'], 'Invert'))
        SliderPanel(self, 'Brightness', color_vars['brightness'], 0, 5)
        SliderPanel(self, 'Vibrance', color_vars['vibrance'], 0, 5)
        RevertButton(self, (color_vars['brightness'], settings.BRIGHTNESS_DEFAULT),
                     (color_vars['grayscale'], settings.GRAYSCALE_DEFAULT),
                     (color_vars['invert'], settings.INVERT_DEFAULT),
                     (color_vars['vibrance'], settings.VIBRANCE_DEFAULT))


class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        DropDownPanel(self, effect_vars['effect'], settings.EFFECT_OPTIONS)
        SliderPanel(self, 'Blur', effect_vars['blur'], 0, 10)
        SliderPanel(self, 'Contrast', effect_vars['contrast'], 0, 10)
        RevertButton(self, (effect_vars['blur'], settings.BLUR_DEFAULT),
                     (effect_vars['contrast'], settings.CONTRAST_DEFAULT),
                     (effect_vars['effect'], settings.EFFECT_OPTIONS[0]))


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        # data
        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value='jpg')
        self.path_string = ctk.StringVar()

        # widgets
        FileNamePanel(self, self.name_string, self.file_string)
        FilePathPanel(self, self.path_string)
        SaveButton(self, export_image, self.name_string, self.file_string, self.path_string)
