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
        
        # Following can be used to make a bounding box in the certificate in order to make it look proper and can insert text based on the bouding box
        bounding_box = [580, 1185, 2920, 1356]
        x1, y1, x2, y2 = bounding_box


        i = 1
        for row in data:
            if row[1] == "PQ":
                filename = f"{row[1]}.png"
                img = Image.open(filename)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('timr45w.ttf', 150) # write the path of the font which you want to select
                
                # center align in particlar box section defined
                w,h = font.getsize(row[0]) # This can be used to selected the font size of the text to be inserted in the box created

                """
                To start the text at the center of the bounding box which we created we need to get the x & y position of the certificate at which the text will get center aligned
                x position = (x pos of the right lower of the bounding box - x pos of the left upper of the bouding box - width of the text)/2 + x pos of the left upper of the bouding box makes the varaible x as the x position of the text to be inserted inside the bouding box center aligned
                Similary we can do for the y position
                """
                x = (x2 - x1 - w)/2 + x1 #  
                y = (y2 - y1 - h)/2 + y1

                draw.text((x, y), row[0], (152, 141, 100), font=font)
                """
                first parameter is the location in pixel at which you want to write the text.
                second parameter is the text you want to write.
                if you want to add extra paramter change the .csv as per you requirement and write this code again.
                """

                """
                The following code you can use that where is the bouding box drawn in the certificate
                Code : draw.rectangle(bounding_box,outline="#111")
                """
                img.save(f"{row[1]}/{row[0]}.png")
                print(str(i) + " Images Processed")

                i += 1

if __name__ == "__main__":
    main()
