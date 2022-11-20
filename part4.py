import matplotlib.pyplot as plt
import skimage.io as skio
import skimage
import numpy as np
import utils

def transformImage(imagePath, bgColor, size, rotation, flip, xyCrop, filter):

    try:

        image = skio.imread(imagePath)

        image = skimage.transform.resize(image, size)

        image = 255 * image

        image = image.astype(np.uint8)

        image = image[xyCrop[0]:image.shape[0], xyCrop[1]:image.shape[1]]  

        newImage = np.zeros((image.shape[0], image.shape[1], image.shape[2]))

        for l in range(image.shape[0]):

            for c in range(image.shape[1]):

                if image[l, c, 0] >= 230 and image[l, c, 1] >= 230 and image[l, c, 2] >= 230:

                    newImage[l, c] = bgColor

                else:

                    newImage[l, c] = image[l, c]

        newImage = skimage.transform.rotate(newImage, angle= rotation)

        if flip == 'Horizontal':

            newImage = np.fliplr(newImage)

        elif flip == 'Vertical':

            newImage = np.flipud(newImage)

        if filter == 'Gray' or filter == 'Canny edge' or filter == 'Skeletonize':

            newImage = skimage.color.rgb2gray(newImage)

            if filter == 'Canny edge':

                newImage = skimage.filters.gaussian(newImage, sigma=1)
                newImage = skimage.feature.canny(newImage, sigma=1)

            elif filter == 'Skeletonize':

                thresh = skimage.filters.threshold_otsu(newImage)
                binary = newImage > thresh
                newImage = skimage.morphology.skeletonize(binary)

            utils.showImage(imagePath, newImage, cmap= 'gray')

        elif filter == 'HSV':

            newImage = skimage.color.rgb2hsv(newImage)

            utils.showImage(imagePath, newImage)

        elif filter == 'Gaussian':

            newImage = skimage.filters.gaussian(newImage, sigma=3)

            utils.showImage(imagePath, newImage)

        elif filter == 'Sobel':

            newImage = skimage.filters.sobel(newImage)

            utils.showImage(imagePath, newImage)

        else:

            utils.showImage(imagePath, newImage)
    

    except FileNotFoundError as e:

        print('\nFicheiro não encontrado\n')

        utils.saveLog(e)

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)



