# size
app_size = (900, 650)
alpha = 0.95
title_ico = '../pic/line.ico'

# text
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 50
NORMAL_FONT_SIZE = 20

styling = {
    'gap': 0.5,
    'corner_radius':  0}

NUM_POSITIONS = {
    '.': {'col': 2, 'row': 6, 'span': 1},
    0: {'col': 1, 'row': 6, 'span': 1},
    1: {'col': 0, 'row': 5, 'span': 1},
    2: {'col': 1, 'row': 5, 'span': 1},
    3: {'col': 2, 'row': 5, 'span': 1},
    4: {'col': 0, 'row': 4, 'span': 1},
    5: {'col': 1, 'row': 4, 'span': 1},
    6: {'col': 2, 'row': 4, 'span': 1},
    7: {'col': 0, 'row': 3, 'span': 1},
    8: {'col': 1, 'row': 3, 'span': 1},
    9: {'col': 2, 'row': 3, 'span': 1}}

MATH_POSITIONS = {
    '/': {'col': 3, 'row': 2, 'character': '', 'image path': '../pic/division.png'},
    '*': {'col': 3, 'row': 3, 'character': 'x', 'image path': '../pic/multiplication.png'},
    '-': {'col': 3, 'row': 4, 'character': '-', 'image path': '../pic/minus.png'},
    '=': {'col': 3, 'row': 6, 'character': '=', 'image path': '../pic/equal.png'},
    '+': {'col': 3, 'row': 5, 'character': '+', 'image path': None}}

OPERATORS = {
    'clear': {'col': 1, 'row': 2, 'text': 'C', 'image path': None},
    'invert': {'col': 0, 'row': 6, 'text': '', 'image path': '../pic/invert.png'},
    'percent': {'col': 0, 'row': 2, 'text': '%', 'image path': None},
    'back': {'col': 2, 'row': 2, 'text': '', 'image path': '../pic/back.png'}}

COLORS = {
    'light-gray': {'fg': '#D4D4D2', 'hover': '#efefed', 'text': 'black'},
    'dark-gray': {'fg': '#505050', 'hover': '#686868', 'text': 'white'},
    'orange': {'fg': "#FF9500", "hover": '#ffb143', 'text': 'white'},
    'orange-highlight': {'fg': 'white', 'hover': 'white', 'text': ('black', '#FF9500')}}
