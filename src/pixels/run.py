from colors import *
from time import sleep
from fonts import Font
from weather import Weather
from display_text import Text
from date_time import DateTime
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from random import randint, choice

# LED matrix configuration
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'
options.brightness = 50

matrix = RGBMatrix(options=options)

matrix_width = options.cols
matrix_height = options.rows

canvas = matrix.CreateFrameCanvas()
text = Text(canvas)
datetime = DateTime()
font = Font()
weather = Weather()

prev_day = ''
prev_month = ''
prev_year = ''
prev_hour = ''
prev_minute = ''
prev_weather_status = ['', '']

timer = {
        'default': 1,
        'default_max': 1,
        'weather': 600,
        'weather_max': 600,      # 10min
        }


def display(canvas, position, prev_str, new_str, char_size, color, pad=[0]*4):
    if prev_str != new_str:
        clear(position, len(prev_str), char_size, pad)
        prev_str = new_str
        text.display(position, new_str, font.file(char_size), color)
        canvas = matrix.SwapOnVSync(canvas)
    return prev_str

def clear(position, total_char, char_size, pad=[0]*4):
    # pad = [top, right, bottom, left]
    font_dict = font.features(char_size)
    font_x = font_dict['x']
    font_y = font_dict['y']
    
    corner_x = position[0] + pad[3]
    width = position[0] + total_char * font_x + pad[1]
    corner_y = position[1] - font_y + pad[0]
    height = position[1] + pad[2]
    # print(corner_x, width, corner_y, height)
    
    for x in range(corner_x, width, 1):
        for y in range(corner_y, height, 1):
            matrix.SetPixel(x, y, 0, 0, 0)

def display_day(canvas, position, size, color):
    global prev_day
    day = datetime.day()
    prev_day = display(canvas, position, prev_day, day, size, color, pad=[4, -1, 0, 0])

def display_month(canvas, position, size, color):
    global prev_month
    month = datetime.month()
    prev_month = display(canvas, position, prev_month, month, size, color, pad=[4, -1, 2, 0])

def display_year(canvas, position, size, color):
    global prev_year
    year = datetime.year()
    prev_year = display(canvas, position, prev_year, year, size, color, pad=[4, -1, 0, 0])

def display_hour(canvas, position, size, color):
    global prev_hour
    hour = datetime.hour()
    prev_hour = display(canvas, position, prev_hour, hour, size, color, pad=[4, 0, 0, 0])

def display_minute(canvas, position, size, color):
    global prev_minute
    minute = datetime.minute()
    prev_minute = display(canvas, position, prev_minute, minute, size, color, pad=[4, 0, 0, 0])

def display_dot(canvas, position, size, color):
    display(canvas, position, '', '.', size, color)

def display_colon(canvas, position, size, color):
    display(canvas, position, '|', ':', size, color, pad=[4, -2, 0, 1])

def display_weather_status(canvas, position, size, color):
    global prev_weather_status
    weather_status = weather.get_weather_status()
    weather_status = weather_status.split(' ') 
    position = [
            (position[0], position[1] - 10), 
            (position[0], position[1])
            ]
    for i in range(2):
        prev_weather_status[i] = display(canvas, position[i], 
                prev_weather_status[i], weather_status[i], 
                size, color, pad=[4, 0, 2, 0])

def run():
    global timer
    
    date_x, date_y = 1, 10
    time_x, time_y = 34, 24
    display_colon(canvas, (time_x + 12, time_y), 'xlargeb', blue)
    if timer['default'] >= timer['default_max']:    
        display_day(canvas, (date_x, date_y), 'xlargeb', blue)
        display_month(canvas, (date_x + 14, date_y), 'xlargeb', red)
        display_year(canvas, (date_x + 35, date_y), 'xlargeb', blue)

        display_hour(canvas, (time_x, time_y), 'xlargeb', blue)
        display_minute(canvas, (time_x + 17, time_y), 'xlargeb', red)
        timer['default'] = 0
    else:
        timer['default'] = timer['default'] + 1
     
    status_x, status_y = 0, 42
    if timer['weather'] >= timer['weather_max']:
        display_weather_status(canvas, (status_x, status_y), 'large', blue)
        timer['weather'] = 0
    else:
        timer['weather'] = timer['weather'] + 1
    

if __name__ == '__main__':
    try:
        while True:
            run()
            sleep(1)
    except KeyboardInterrupt:
        matrix.Clear()

