#!/usr/bin/env python3
"""Script to add text on certificates using data in csv file on a png"""

import csv
from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    """
    Reads names.csv and certi.png and adds names and project title in certificate
    based on coordinates specified
    """
    with open('names.csv', 'rt') as f:
        data = csv.reader(f)

        # Following can be used to make a bounding box in the certificate
        # in order to make it look proper and can insert text based on the
        # bouding box. In order to fetch the perfect coordinates run
        # drawrectangle.py which will help in creating a bounding box at
        # whatever coordinates you want by drawing a rectangle on the image
        # and will also provide the coordinates of the rectangle for the left
        # top and right bottom corner of the rectangle.
        bounding_box = [580, 1185, 2920, 1356]
        x1, y1, x2, y2 = bounding_box


        for idx, row in enumerate(data):
            name, project = row
            filename = f"{name}.png"
            img = Image.open(filename)
            draw = ImageDraw.Draw(img)

            # NOTE: The fonts can be downloaded from google fonts and any other
            # open source font providing website.
            # replace 'timr45w.ttf' with the path of the font which you want
            # to select
            font = ImageFont.truetype('timr45w.ttf', 150)

            # center align in particlar box section defined in order to
            # select the font size of the text to be inserted
            w,h = font.getsize(name)


            # To start the text at the center of the bounding box which we
            # created we need to get the x & y position of the certificate
            # at which the text will get center aligned
            # x position = (x pos of the right lower of the bounding box
            # - x pos of the left upper of the bouding box - width of the text) / 2
            # + x pos of the left upper of the bouding box makes the varaible x
            # as the x position of the text to be inserted inside the bouding box
            # center aligned. Similar for the y position

            x = (x2 - x1 - w)/2 + x1
            y = (y2 - y1 - h)/2 + y1

            # first parameter is the location in pixel at which you want to write the text.
            # second parameter is the text you want to write.
            # if you want to add extra paramter change the .csv as per you requirement & make
            # changes in the code accordingly.
            draw.text((x, y), name, (152, 141, 100), font=font)


            #The following code you can use that where is the bouding box drawn in the certificate
            #Code : draw.rectangle(bounding_box,outline="#111")
            img.save(f"{project}/{name}.png")
            print(f"{idx} Images Processed")

            # Ported From CV2 to Pillow

            #############################################################
            #  cv2.putText(img, row[0], (2458, 1260),                   #
            #           cv2.FONT_HERSHEY_SIMPLEX, 2.6, (0, 0, 0), 6)    #
            #  cv2.putText(img, row[1], (1530, 1413),                   #
            #           cv2.FONT_HERSHEY_SIMPLEX, 2.6, (0, 0, 0), 6)    #
            #  cv2.imwrite("Certificates/"+str(i)+row[0]                #
            #           + ".png", img)                                  #
            #############################################################

            # For future use with cv2 and any font connect pillow and cv2


if __name__ == "__main__":
    main()
