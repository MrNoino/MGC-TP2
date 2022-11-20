import matplotlib.pyplot as plt
import numpy as np
import utils

#função que roda uma imagem 90 graus no sentido dos ponteiro do relogio
def rotate90Clockwise(imagePath):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        #obtem a altura, largura e cor da imagem
        height, width, color  = image.shape[0], image.shape[1], image.shape[2]

        #cria um array de zeros com a altura igual à largura da imagem original e com a largura igual à altura da imagem original
        rotatedImage = np.uint8(np.zeros((width, height, color)))

        #para cada coluna da imagem original
        for c in range(width):

            #para cada linha da imagem original
            for l in range(height):

                #atribui o pixel da imagem original na imagem nova
                rotatedImage[c, l] =  image[height -1 - l, c] 
                
        #mostra a imagem
        utils.showImage(imagePath, rotatedImage)

    #caso a imagem não seja encontrada
    except FileNotFoundError as e:

        #imprime msg de erro
        print('\nFicheiro não encontrado\n')

        #escreve um log com a exceção
        utils.saveLog(e)

    #caso ocorra uma exceção
    except Exception as e:

        #imprime msg de erro
        print('\nAlgo correu mal ao ler a imagem\n')

        #escreve um log com a exceção
        utils.saveLog(e)

#função que reduz em um quarto a imagem 
def reduceToQuarterImage(imagePath):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        l1, l2 = 0, 0

        #cria um array de zeros com metade da altura e da largura original
        reducedImage = np.zeros((int(image.shape[0] / 2), int(image.shape[1] / 2), image.shape[2]))

        #enquanto não chegar ao fim das linhas da imagem original e a nova
        while l1 < image.shape[0] and l2 < reducedImage.shape[0]:

            c1, c2 = 0, 0

            #enquanto não chegar ao fim das colunas da imagem original e a nova
            while c1 < image.shape[1] and c2 < reducedImage.shape[1]:

                #atribui à imagem nova o pixel mais a baixo e à direita do cojunto de 4 pixeis
                reducedImage[l2, c2] = image[l1 + 1, c1 + 1]

                c1 += 2
                c2 += 1

            l1 += 2
            l2 += 1

        #mostra a imagem
        utils.showImage(imagePath, reducedImage)
    

    #caso a imagem não exista
    except FileNotFoundError as e:

        #imprime msg de erro
        print('\nFicheiro não encontrado\n')

        #escreve um log com a exceção
        utils.saveLog(e)

    #caso ocorra uma exceção
    except Exception as e:

        #imprime msg de erro
        print('\nAlgo correu mal ao ler a imagem\n')

        #escreve um log com a exceção
        utils.saveLog(e)    