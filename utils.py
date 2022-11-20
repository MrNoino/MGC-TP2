from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

#funcao que mostra uma imagem
def showImage(title, image, cmap= None):

    #cria a figura
    plt.figure()
    #define o título
    plt.title(title)

    #se o cmap foi definido
    if cmap != None:

        #cria o grafico com a imagem e com o cmap
        plt.imshow(image.astype(np.uint8), cmap= cmap)

    #se nao
    else:

        #cria o grafico com a imagem
        plt.imshow(image.astype(np.uint8))

    #mostra a imagem
    plt.show()

#função que pede valores de entrada convertidos em tipos de dados
def getParsedInput(msg, exceptionMsg = '\nValor inválido, tente novamente.\n', type = 'int'):

    #tenta
    try:

        #se o tipo é int
        if type == 'int':

            #pede e retorna um valor convertido em inteiro
            return int(input(msg))

        #se nao se o tipo é float
        elif type == 'float':

            #pede e retorna um valor convertido em float
            return float(input(msg))

        #se nao
        else:

            #imprime msg de erro
            print('\nTipo inválido.\n')

    #caso o valor pedido não é convertivel pelo tipo de dados escolhido
    except ValueError as e:

        #imprime msg de erro
        print(exceptionMsg)

        #escreve um log com a exceção
        saveLog(e)

        #returna nulo
        return None

#função para gravar um log com exceções
def saveLog(text):

    #tenta
    try:

        #abrir o ficheiro log.txt para acrescentar 
        f = open("log.txt", "a")

        #escreve a mensagem desejada com a data e hora 
        f.write("\n" + str(text) + '\t' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")

        #fecha o documento
        f.close()

        #retorna verdadeiro em conforme foi guardado o log
        return True

    #em caso de exceção
    except: 

        #retorna false em conforme não foi guardado o log
        return False

#função que pede a cor do círculo
def askColorLimit(msg):

    #define as cores e respetivos limites em HSV
    colorLimits = [
                    {'color': 'Amarelo', 'lower': (28,0, 0), 'upper': (32,255,255)},
                    {'color': 'Vermelho', 'lower': (155,25,0), 'upper': (179,255,255)},
                    {'color': 'Azul', 'lower': (90, 0, 0), 'upper': (130, 255, 255)},
                    {'color': 'Verde', 'lower': (36,0,0), 'upper': (86,255,255)}
                ]

    #para cada indice e valor do array
    for i, item in enumerate(colorLimits):

        #adiciona à string o indice mais 1 e o valor da cor
        msg += str(i+1) + '-' + item['color'] + ', '

    #remove o último ', '
    msg = msg[:len(msg) -2]

    msg += ' -> '

    #pede a cor
    colorLimit = getParsedInput(msg, 'int')

    #se a cor está fora dos limites do array
    while colorLimit < 1 or colorLimit > len(colorLimits):

        #imprime msg de erro
        print('\nOpção inválida, tente novamente.')

        #pede novamente a cor
        colorLimit = getParsedInput(msg, 'int')

    #retorna a cor
    return colorLimits[colorLimit-1]