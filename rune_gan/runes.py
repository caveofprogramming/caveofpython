from PIL import Image, ImageDraw, ImageFont
import os

# Use this font to draw the runes.
FONT = "./beorc-gothic-font/BeorcGothicRegular-Bew8.ttf"

# Directory where output is placed
OUTPUT_DIR = "./runes"

# The first index in the unicode character set
# that is a rune
UNICODE_RUNE_INDEX = 5792

# How many different runes do we have?
NUMBER_RUNES = 80

def create_runes(size):

    if not os.path.isfile(FONT):
        raise FileNotFoundError(FONT, 'is missing')
    
    if not os.path.isdir(OUTPUT_DIR):
        raise FileNotFoundError(OUTPUT_DIR, "output directory doesn't exist")

    # Load the rune font
    fnt = ImageFont.truetype(FONT, size)

    # Iterate over all runes in Unicode
    # that are actually in the font.
    for i in range(NUMBER_RUNES):

        # print the symbol, just to check
        print(chr(i + UNICODE_RUNE_INDEX), end="")

        # Create an image to draw on.
        img = Image.new('RGB', (size, size))

        # Get a drawing context to draw on
        draw = ImageDraw.Draw(img)

        # Draw the symbol onto the image.
        draw.text((0, 0), chr(i + UNICODE_RUNE_INDEX), fill=(255, 0, 0), font=fnt)

        # Turn the pixels into a numpy array.
        # We'll only use the first of the 
        # red-green-blue pixel triplet.
        pixels = [x[0] for x in img.getdata()]

        path = os.path.join(OUTPUT_DIR, f"rune{i}.png")

        img.save(path, format='png')

if __name__ == "__main__":
    create_runes(20)

    print(f"\nCreated {NUMBER_RUNES} runes in directory '{OUTPUT_DIR}'")