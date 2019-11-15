"""Script to add text on certificates using data in csv file on a png"""

import csv
from PIL import Image, ImageDraw, ImageFont


def main():
    """
    Reads Names.csv and certi.png and adds names and project title in certificate based on
    coordinates specified
    """
    with open('Names.csv', 'rt')as f:
        data = csv.reader(f)
        filename = "certi.png"

        i = 1
        for row in data:
            img = Image.open(filename)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('LIB_IT.ttf', 90) # write the path of the font which you want to select
            draw.text((1370, 1030), row[0], (0, 0, 0), font=font)
            """
            first parameter is the location in pixel at which you want to write the text.
            second parameter is the text you want to write.
            if you want to add extra paramter change the .csv as per you requirement and write this code again.
            """
            img.save("Certificates/" + row[0] + ".png")
            print(str(i) + " Images Processed")

            i += 1

if __name__ == "__main__":
    main()
