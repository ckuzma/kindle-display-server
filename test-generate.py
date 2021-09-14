from PIL import Image, ImageDraw, ImageFont

## Testing things
OUTPUT_TEXT = "Hello world!"
OUTPUT_FILE = "output/generated_image.png"

## Parameters
FONT_FILE = "fonts/DejaVuSans.ttf"
FONT_SIZE = 15
FONT_COLOR = (0, 0, 0)
FONT_PLACEMENT = (10, 10)
BACKGROUND_COLOR = (255, 255, 255)

## Create new image, draw text
image = Image.new(
    mode = "RGB",
    size =  (600, 800),
    color=BACKGROUND_COLOR
)
draw = ImageDraw.Draw(image)
draw.text(
    FONT_PLACEMENT,
    OUTPUT_TEXT,
    font=ImageFont.truetype(FONT_FILE, FONT_SIZE),
    fill = FONT_COLOR
)

## Save to disk
image.save(OUTPUT_FILE)