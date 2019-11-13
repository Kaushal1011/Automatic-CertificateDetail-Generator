"""Script to add text on certificates using data in csv file on a png"""

import cv2
import csv


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
            img = cv2.imread(filename)
            # Add Coordinates of image where left bottom  of first character of text will be placed
            # Coordinates can be found using simple software such as paint
            cv2.putText(img, row[0], (2458, 1260),
                        cv2.FONT_HERSHEY_SIMPLEX, 2.6, (0, 0, 0), 6)
            cv2.putText(img, row[1], (1530, 1413),
                        cv2.FONT_HERSHEY_SIMPLEX, 2.6, (0, 0, 0), 6)
            cv2.imwrite("Certificates/"+str(i)+row[0]
                        + ".png", img)
            print("Running " + str(i) + " Images Processed")
            i += 1


if __name__ == "__main__":
    main()
