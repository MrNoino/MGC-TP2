
import matplotlib.pyplot as plt

def color2gray(color):

    return (0.2126 * color[0], 0.7152 * color[1], 0.0722 * color[2])


def image2gray(imagePath):

    image = plt.imread(imagePath)

    print(image)

