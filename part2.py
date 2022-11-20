import matplotlib.pyplot as plt
import utils
import numpy as np

#função que calcula o valor RGB médio de uma imagem
def averageRGB(imagePath):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        #obtem o número de pixeis totais+
        numberPixels = image.shape[0] + image.shape[1]

        #retorna o somatorio dos valores R a dividir pelo número de pixeis, o somatorio dos valores G a dividir pelo número de pixeis, o somatorio dos valores B a dividir pelo número de pixeis
        return round(sum(sum(image[:,:,0]))/numberPixels, 2), round(sum(sum(image[:,:,1]))/numberPixels, 2), round(sum(sum(image[:,:,2]))/numberPixels, 2)

    #caso a imagem não exista
    except FileNotFoundError as e:

        #imprime msg de erro
        print('\nFicheiro não encontrado\n')

        #escreve um log com a exceção
        utils.saveLog(e)

        #devolve 3 valores nulos
        return None, None, None

    except Exception as e:

        #imprime msg de erro
        print('\nAlgo correu mal ao ler a imagem\n')

        #escreve um log com a exceção
        utils.saveLog(e)

        #devolve 3 valores nulos
        return None, None, None

#função que mostra o valor RGB de um pixel na posição x,y e atualiza o valor RGB
def updatePixel(imagePath, x, y, color):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        #se as posições saem fora do limite da imagem ou se o valor RGB nao esta correto
        if(x == None or x not in range(image.shape[0])) or (y == None or y not in range(image.shape[1])) or (color == None or color[0] not in range(256) or color[1] not in range(256) or color[2] not in range(256)):
            #termina a função
            return

        #imprime o valor RGB do pixel da posição x,y
        print('\nPíxel ' + str(x) + ',' + str(y), ':', str(image[x][y]), '\n')

        #cria uma copia da imagem
        newImage = np.array(image)

        #atribui o novo valor RGB na posição x,y
        newImage[x][y] = color

        #mostra imagem
        utils.showImage(imagePath, newImage)

    #caso a imagem não exista
    except FileNotFoundError as e:

        #imprime msg de erro
        print('\nFicheiro não encontrado\n')

        #escreve um log com a exceção
        utils.saveLog(e)

    except Exception as e:

        #imprime msg de erro
        print('\nAlgo correu mal ao ler a imagem\n')

        #escreve um log com a exceção
        utils.saveLog(e)

#função que encontra o pixel com valor RGb mais alto
def highestPixel(imagePath):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        #define o primeiro pixel como o mais alto
        higher = int(image[0][0][0]) + int(image[0][0][1]) + int(image[0][0][2])

        #define a posição da linha como a mais alta
        higherL = 0

        #define a posição da coluna como a mais alta
        higherC = 0

        #para cada linha da imagem
        for l in range(image.shape[0]):

            #para cada coluna da imagem
            for c in range(image.shape[1]):

                #se o valor RGB mais alto for meno que o valor RGB do pixel atual
                if higher < (int(image[l][c][0]) + int(image[l][c][1]) + int(image[l][c][2])):

                    #substitui o valor mais alto
                    higher = int(image[l][c][0]) + int(image[l][c][1]) + int(image[l][c][2])

                    #define a posição atual da linha como mais alta
                    higherL = l

                    #define a posição atual da coluna como mais alta
                    higherC = c

        #imprime a posição do píxel com maior valor RGB e respetivo valor
        print('\nA posição do píxel com o maior valor RGB é:', str(higherL) + ',' + str(higherC), 'com valor RGB de', str(image[higherL][higherC]))
                
    #caso a imagem não exista
    except FileNotFoundError as e:

        #imprime msg de erro
        print('\nFicheiro não encontrado\n')

        #escreve um log com a exceção
        utils.saveLog(e)

    except Exception as e:

        #imprime msg de erro
        print('\nAlgo correu mal ao ler a imagem\n')

        #escreve um log com a exceção
        utils.saveLog(e)
