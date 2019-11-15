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
