import graphics as gph

WIN_WIDTH = 500
WIN_HEIGHT = 700

win = gph.GraphWin('CalcM', WIN_WIDTH, WIN_HEIGHT)

initial_pad_x_pos = 145
gap = 8
num_button_width = 50
num_button_height = 50
button_x_pos = initial_pad_x_pos
button_y_pos = 250

buttons = {
    'AC': {'width': 60, 'height': 30},
    '(': {'width': 60, 'height': 30},
    ')': {'width': 60, 'height': 30},
    'Del': {'width': 60, 'height': 30},
    '7': {'width': 60, 'height': 30},
    '8': {'width': 60, 'height': 30},
    '9': {'width': 60, 'height': 30},
    '+': {'width': 60, 'height': 30},
    '4': {'width': 60, 'height': 30},
    '5': {'width': 60, 'height': 30},
    '6': {'width': 60, 'height': 30},
    '-': {'width': 60, 'height': 30},
    '1': {'width': 60, 'height': 30},
    '2': {'width': 60, 'height': 30},
    '3': {'width': 60, 'height': 30},
    '/': {'width': 60, 'height': 30},
    '0': {'width': 60, 'height': 30},
    '=': {'width': 60, 'height': 30},
    'x': {'width': 60, 'height': 30}
}

calc_width = 0

for i in range(4):

    print(buttons[i])
    if i != 4:
        calc_width += buttons[i]['width'] + gap
    calc_width += buttons[i]['width']

c = 0

for key, button in buttons.items():
    if c % 4 == 0 and c > 0:
        button_x_pos = initial_pad_x_pos
        button_y_pos += button['height'] + gap
    p1 = gph.Point(button_x_pos, button_y_pos)
    p2 = gph.Point(button_x_pos+button['width'], button_y_pos+button['height'])

    key_button = gph.Rectangle(p1,p2)
    key_button.draw(win)
    button_x_pos += button['width'] + gap

    c += 1

win.getMouse()