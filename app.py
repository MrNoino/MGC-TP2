import part1, part2, part3, part4, part5
import utils
import sys

option = '1'

#enquanto opção diferente de '0'
while option != '0':

    #apresenta o menu e pede opção
    option = input('\tMenu\n\n5. PARTE V\n4. PARTE IV\n3. PARTE III\n2. PARTE II\n1. PARTE I\n0. Sair\nOpção: ')

    #se opção igual a '1'
    if option == '1':

        subOption = '1'

        #enquanto subopção diferente de '0'
        while subOption != '0':

            #apresenta o submenu e pede subopção
            subOption = input('\n\tPARTE I\n\n2. d) Converter uma imagem na escala cinzenta\n1. c) Imprimir a sombra cinzenta a cor RGB(154,50, 20)\n0. Voltar\nOpção: ')
            
            #se subopção igual a '1'
            if subOption ==  '1':
                
                #imprime o valor RGB (154,50, 20) em escala cinzenta
                print('\n(154,50, 20) para escala cinzeta:', str(part1.color2gray((154,50, 20))), '\n')

            #se não se subopção igual a '2'
            elif subOption == '2':

                #mostra a imagem pedida em escala cinzenta
                part1.image2gray(input('\nCaminho da imagem: '))

            #se não se subopção igual a '0'
            elif subOption == '0':

                print('\nA voltar...\n')

            #se não
            else:

                print('\nOpção inválida, tente novamente.\n')

    #se não se opção igual a '2'
    elif option == '2':

        subOption = '1'

        #enquanto a subopção diferente de '0'
        while subOption != '0':

            #apresenta o submenu e pede subopção
            subOption = input('\n\tPARTE II\n\n3. c) Imprimir o píxel com o valor RGB mais alto\n2. b) Atualizar o valor de um píxel \n1. a) Imprimir o valor médio do RGB de uma imagem\n0. Voltar\nOpção: ')

            #se subopção igual a '1'
            if subOption ==  '1':
                
                #calcula a média do valores RGB da imagem pedida
                avgR, avgG, avgB = part2.averageRGB(input('\nCaminho da imagem: '))

                #se houver médias
                if avgR != None and avgG != None and avgB != None:

                    #imprime as médias
                    print('As médias são:\nR:', avgR ,'\nG:', avgG, '\nB:', avgB, '\n')

            #se não se subopção igual a '2'
            elif subOption ==  '2':
                
                #pede o caminho da imagem
                imagePath = input('\nCaminho da imagem: ')

                #pede a posição x do pixel
                x = utils.getParsedInput('\nPosição x do píxel: ', 'int')

                #pede a posição y do pixel
                y = utils.getParsedInput('\nPosição y do píxel: ', 'int')

                #pede a quantidade de vermelho
                r = utils.getParsedInput('\nQuantidade de vermelho (0, 255): ', 'int')

                #pede a quantidade de verde
                g = utils.getParsedInput('\nQuantidade de verde (0, 255): ', 'int')

                #pede a quantidade de azul
                b = utils.getParsedInput('\nQuantidade de azul (0, 255): ', 'int')

                #imprime o valor RGB do pixel escolhido e atualiza o valor RGB
                part2.updatePixel(imagePath, x, y, (r, g, b))

            #se não se subopção igual a '3'
            elif subOption == '3':

                #imprime a localização e o valor RGB do pixel mais alto
                part2.highestPixel(input('\nCaminho da imagem: '))


            #se não se subopção igual a '0'
            elif subOption == '0':

                print('\nA voltar...\n')

            #se não
            else:

                print('\nOpção inválida, tente novamente.\n')

    #se não se opção igual a '3'
    elif(option == '3'):

        subOption = '1'

        #enquanto a subopção diferente de '0'
        while subOption != '0':

            #apresenta o submenu e pede subopção
            subOption = input('\n\tPARTE II\n\n2. b) Reduzir a imagem a um quarto do tamanho original\n1. a) Rodar uma imagem 90º no sentido dos ponteiros do relógio\n0. Voltar\nOpção: ')

            #se subopção igual a '1'
            if subOption ==  '1':
                
                #mostra a imagem pedida rodada 90 graus no sentido dos ponteiros do relógio
                part3.rotate90Clockwise(input('\nCaminho da imagem: '))

            #se não se subopção igual a '2'
            elif subOption == '2':

                #mostra a imagem pedida reduzida a um quarto do seu tamanho
                part3.reduceToQuarterImage(input('\nCaminho da imagem: '))

            #se não se subopção igual a '0'
            elif subOption == '0':

                print('\nA voltar...\n')

            #se não
            else:

                print('\nOpção inválida, tente novamente.\n')

    #se não se opção igual a '4'
    elif(option == '4'):

        subOption = '1'

        #enquanto a subopção diferente de '0'
        while subOption != '0':

            #apresenta o submenu e pede subopção
            subOption = input('\n\tPARTE IV\n\n1. Transformar a imagem\n0. Voltar\nOpção: ')

            #se subopção igual a '1'
            if subOption == '1':

                #pede o caminho da imagem
                imagePath = input('\nCaminho da imagem: ')

                #cria as cores e respetivos valores RGB
                colors = {'Vermelho': (255, 0, 0), 'Verde': (0, 255, 0), 'Azul': (0, 0, 255), 'Amarelo': (255, 255, 0), 'Cinzento': (128, 128, 128), 'Preto': (0, 0, 0)}

                
                msg = '\nInsere a cor de fundo da imagem:\nOpções: '

                # para cada chave do dicionário
                for key in colors.keys():

                    #adiciona a chave à string
                    msg += str(key) + ', '

                #remove o último ', '
                msg = msg[:len(msg) - 2]

                msg += ' -> '

                #pede a cor de fundo
                bgColor = input(msg)

                #capitaliza a string da cor
                bgColor = bgColor.capitalize()

                #enquanto a cor nao for uma chave do dicionario
                while bgColor not in colors:

                    #imprime msg de erro
                    print('\nCor inválida, tente novamente.')

                    #pede novamente a cor de fundo
                    bgColor = input(msg)

                    #capitaliza a string da cor
                    bgColor = bgColor.capitalize()

                #inicializa o tamanho
                size = ()

                print('\nIntroduza o tamanho da imagem')

                #pede a altura
                size = size + (utils.getParsedInput('\nAltura: ', 'int'),)
                #pede a largura
                size = size + (utils.getParsedInput('Largura: ', 'int'),)

                #pede os graus a rodar a imagem
                rotation = utils.getParsedInput('\nRotação da imagem (sentido dos ponteiros do relógio, em graus): ', 'int')

                #opções de inverter a imagem
                flipOptions = ['Nenhuma', 'Vertical', 'Horizontal']

                msg = '\nInverção de imagem:\nOpções: '

                #para indice e valor do array
                for i, f in enumerate(flipOptions):

                    #adiciona indice mais 1 e o valor à string
                    msg += str(i+1) + '-' + str(f) + ', '

                #remove o último ', '
                msg = msg[:len(msg) -2]

                msg += ' -> '

                #pede a inversão de imagem
                flip = utils.getParsedInput(msg, 'int')

                #enquanto a inversão de imagem não estiver dentro dos limites do array
                while flip < 1 or flip > len(flipOptions):

                    #imprime msg de erro
                    print('\nOpção inválida, tente novamente.')

                    #pede novamente a inversão de imagem
                    flip = utils.getParsedInput(msg, 'int')

                #inicializa o array para guardar o corte da imagem
                xyCrop = []

                print('\nIntroduza quantos píxeis devem ser cortados')

                #pede quantos pixeis devem ser cortados na vertical
                xyCrop.append(utils.getParsedInput('\nDe cima para baixo: ', type='int'))
                #pede quantos pixeis devem ser cortados na horizontal
                xyCrop.append(utils.getParsedInput('Da esquerda para a direita: ', type='int'))

                #opções de filtro
                filters = ['Nenhum', 'Gray', 'HSV', 'Gaussian', 'Sobel', 'Canny edge', 'Skeletonize']

                filter = ''

                msg = '\nEscolha um filtro\nOpções: '

                #para cada indice e valor do array
                for i, f in enumerate(filters):

                    #adiciona o indice mais 1 e o valor à string
                    msg += str(i+1) + '-' + str(f) + ', '

                #remove o último ', '
                msg = msg[:len(msg)-2]

                msg += ' -> '

                #pede o filtro
                filter = utils.getParsedInput(msg, 'int')

                #enquanto o filtro não estiver dentro dos limites do array
                while filter < 1 or filter > len(filters):

                    #imprime msg de erro
                    print('\nFiltro inválido, tente novamente.')

                    #pede novamente o filtro
                    filter = utils.getParsedInput(msg, 'int')

                #transforma a imagem de acordo com as configurações que o utilizador escolheu e mostra-a
                part4.transformImage(imagePath, colors[bgColor], size, rotation, flipOptions[flip-1], xyCrop, filters[filter-1])


            #se não se subopção igual a '0'
            elif subOption == '0':

                print('\nA voltar...\n')

            #se não
            else:

                print('\nOpção inválida, tente novamente.\n')

    #se não se opção igual a '5'
    elif(option == '5'):

        subOption = '1'

        #enquanto a subopção diferente de '0'
        while subOption != '0':

            #apresenta o submenu e pede subopção
            subOption = input('\n\tPARTE V\n\n4. c) Pokemon in real-time\n3. b) Detetar círculos de uma determinada cor\n2. a) Pokemon\n1. a) Reconhecer uma matrícula a partir de uma foto\n0. Voltar\nOpção: ')

            #se subopção igual a '1'
            if subOption == '1':

                #deteta uma matricula a partir de uma imagem dada
                part5.detectPlate(input('\nCaminho da imagem: '))

            #se não se subopção igual a '2'
            elif subOption == '2':

                #transforma a imagem com círculos da cor desejada pelo utilizador no pokemon correspondente
                part5.detectPokemonFromFile(input('\nCaminho da imagem: '), utils.askColorLimit('\nEscolhe a cor para subsituir pelo pokemon\nOpções: '))

            #se não se subopção igual a '3'
            elif subOption == '3':

                #pede o caminho da imagem
                imagePath = input('\nCaminho da imagem: ')

                #pede a cor do círculo
                colorLimit = utils.askColorLimit('\nEscolhe a cor para detetar os círculos\nOpções: ')

                #imprime o número de círculos da cor escolhida pelo utilizador
                print('\nO número de círculos "' + colorLimit['color'] + '" é:', part5.detectNumberColoredCircles(imagePath, colorLimit))

            #se não se subopção igual a '4'
            elif subOption == '4':

                #pede a cor do círculo
                colorLimit = utils.askColorLimit('\nEscolhe a cor para subsituir pelo pokemon\nOpções: ')

                #transforma o vídeo da câmara com círculos da cor desejada pelo utilizador no pokemon correspondente
                part5.detectPokemonFromCam(colorLimit)

            #se não se subopção igual a '0'
            elif subOption == '0':

                print('\nA voltar...\n')

            #se não se subopção igual a '0'
            else:

                print('\nOpção inválida, tente novamente.\n')

    #se não se opção igual a '0'
    elif(option == '0'):

        print('\nPrograma encerrado.\n')

    #se não
    else:

        print('\nOpção inválida, tente novamente.\n')