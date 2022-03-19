from PIL import Image, ImageDraw, ImageFont

## Testing things
OUTPUT_FILE = "output/generated_image.png"

## Parameters
FONT_FILE = "fonts/DejaVuSans.ttf"
FONT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

## Create new image, draw text
image = Image.new(
    mode = "RGB",
    size =  (600, 800),
    color=BACKGROUND_COLOR
)
draw = ImageDraw.Draw(image)

def drawCityName(drawing, city_name):
    drawing.text(
        (140, 30),
        city_name,
        font=ImageFont.truetype(FONT_FILE, 40),
        fill = FONT_COLOR
    )
    return drawing

def drawCurrentTemp(drawing, current_temp):
    drawing.text(
        (20, 100),
        current_temp + "°F",
        font=ImageFont.truetype(FONT_FILE, 140),
        fill = FONT_COLOR
    )
    return drawing

def drawMinMax(drawing, temp_min, temp_max):
    drawing.text(
        (30, 250),
        'Min: ' + temp_min + "°F, Max: " + temp_max + "°F", 
        font=ImageFont.truetype(FONT_FILE, 35),
        fill = FONT_COLOR
    )
    return drawing

draw = drawCityName(draw, 'BLOOMINGTON')
draw = drawCurrentTemp(draw, '68.2')
draw = drawMinMax(draw, '60.2', '70.2')

## Save to disk
image.save(OUTPUT_FILE)

