import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageOps, ImageEnhance


picture = Image.open("/home/aleksandar/PycharmProjects/Course/CourseHomework/work_with_images/panda.jpg")


operation=input('Operation: ')

if operation == "left":
    picture = picture.transpose(Image.ROTATE_90)
    picture.show()

elif operation == "rotate_right":
    picture = picture.transpose(Image.ROTATE_270)
    picture.show()
elif operation == "invert":
    picture =ImageOps.invert(picture)
    picture.show()
elif operation == "lighten":
    coeficent = float(input('coeficent number: '))
    picture = ImageEnhance.Contrast(picture).enhance(coeficent)
    picture.show()
elif operation == "darken":
    coeficent = float(input('coeficent number: '))
    picture = ImageEnhance.Brightness(picture).enhance(coeficent)
    picture.show()
elif operation == "create_histogram":
    picture_graph = cv2.imread('panda.jpg')
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histogram = cv2.calcHist([picture_graph], [i], None, [256], [0, 256])
        plt.plot(histogram, color=col)
        plt.xlim([0, 256])
    plt.show()
