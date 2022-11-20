import matplotlib.pyplot as plt
import utils

#função que transforma valores RGB na escala de cinza
def color2gray(color):

    #retorna a forumla que transforma valores RGB na escala cinzenta
    return 0.2126 * color[0] + 0.7152 * color[1] + 0.0722 * color[2]


#função que transforma uma imagem na escala de cinza
def image2gray(imagePath):

    #tenta
    try:

        #le a imagem
        image = plt.imread(imagePath)

        #converte a imagem na escala cinzenta
        grayImage = color2gray((image[:,:,0], image[:,:,1], image[:,:,2]))

        #mostra a imagem
        utils.showImage(imagePath, grayImage, 'gray')
    
    #caso a imagem não foi encontrada
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



