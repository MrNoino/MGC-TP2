import pytesseract
import cv2
import utils
import re
import numpy as np

def detectPlate(imagePath):

    try:

        image = cv2.imread(imagePath)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(gray, (3,3), 0)

        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

        invert = 255 - opening

        edges = cv2.Canny(invert, threshold1=30, threshold2=100)

        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)

        if lines is not None:

            for line in lines:

                for x1, y1, x2, y2 in line:

                    cv2.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)

        data = pytesseract.image_to_string(invert, lang='eng', config ='--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ')
        
        x = re.search('[A-Z0-9]{2}[\s-]{1}[A-Z0-9]{2}[\s-]{1}[A-Z0-9]{2}', data)

        if x:
            
            data = data[x.start() : x.end()]

        elif len(data) >= 6:

            data = data[len(data)-7:]

        image = cv2.putText(image, data, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA) 

        cv2.imshow('Matricula', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)

def contours(image, colorLimits):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, colorLimits['lower'], colorLimits['upper'])

    res = cv2.bitwise_and(image, image, mask=mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    _,thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    return cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

def pokemon(image, colorLimits):

    try:

        cts, hierarchy = contours(image, colorLimits)

        if colorLimits['color'] == 'Amarelo':

            pokemonImage = cv2.imread('Pikachu.png')

        elif colorLimits['color'] == 'Vermelho':

            pokemonImage = cv2.imread('Charmander.png')

        elif colorLimits['color'] == 'Verde':

            pokemonImage = cv2.imread('Bulbasaur.png')

        elif colorLimits['color'] == 'Azul':

            pokemonImage = cv2.imread('Squirtle.png')

        for c in cts:

            perimeter = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

            if len(approx) > 5:

                startLeft, endLeft = int(min(c[:, :, 0])), int(max(c[:, :, 0])) +1
                startTop, endTop = int(min(c[:, :, 1])), int(max(c[:, :, 1])) +1

                pokemonImage = cv2.resize(pokemonImage, (endLeft - startLeft, endTop - startTop))

                image[startTop : endTop, startLeft : endLeft] = pokemonImage

        return image

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)

def detectPokemonFromFile(imagePath, colorLimits):

    try:

        image = cv2.imread(imagePath)

        image = pokemon(image, colorLimits)

        cv2.imshow('Pokemon', image)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)

def detectNumberColoredCircles(imagePath, colorLimits):

    try:

        image = cv2.imread(imagePath)

        cts, hierarchy = contours(image, colorLimits)

        count = 0

        for c in cts:

            perimeter = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

            if len(approx) > 5:

                count += 1

        return count

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)


def detectPokemonFromCam(colorLimits):

    vid = cv2.VideoCapture(0)

    try:

        while cv2.waitKey(1) == -1:

            ret, image = vid.read()

            image = pokemon(image, colorLimits)

            cv2.imshow('Pokemon', image)

        cv2.destroyAllWindows()

    except Exception as e:

        print('\nAlgo correu mal ao ler a imagem\n')

        utils.saveLog(e)
