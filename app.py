import part1

option = '1'

while option != '0':

    option = input('\tMenu\n\n5. PARTE V\n4. PARTE IV\n3. PARTE III\n2. PARTE II\n1. PARTE I\n0. Sair\nOpção: ')

    if option == '1':

        subOption = '1'
        while subOption != '0':

            subOption = input('\tPARTE I\n\n2. d) Converter uma imagem na escala cinzenta\n1. c) Imprimir a sombra cinzenta a cor RGB(154,50, 20)\n0. Voltar\nOpção: ')

            if subOption == '2':

                part1.image2gray('imagem.jpg')
            
            elif subOption ==  '1':
                
                print('\n(154,50, 20) para escala cinzeta:', str(part1.color2gray((154,50, 20))), '\n')

            elif subOption == '2':

                print()

            elif subOption == '0':

                print('\nA voltar...\n')

            else:

                print('\nOpção inválida, tente novamente.\n')

    elif option == '2':

        subOption = '1'
        while subOption != '0':

            subOption = input('\tPARTE II\n\n3. c) Imprimir o valor médio do RGB de uma imagem\n2. b) Atualizar o valor de um píxel \n1. a) Imprimir o píxel com o valor RGB mais alto\n0. Voltar\nOpção: ')

            if subOption ==  '1':
                
                print()

            elif subOption ==  '2':
                
                print()

            elif subOption == '3':

                print()

            elif subOption == '0':

                print('\nA voltar...\n')

            else:

                print('\nOpção inválida, tente novamente.\n')

    elif(option == '3'):

        subOption = '1'
        while subOption != '0':

            subOption = input('\tPARTE II\n\n2. b) Rodar uma imagem 90º no sentido dos ponteiros do relógio \n1. a) Reduzir a imagem a um quarto do tamanho original\n0. Voltar\nOpção: ')

            if subOption ==  '1':
                
                print()

            elif subOption == '2':

                print()

            elif subOption == '0':

                print('\nA voltar...\n')

            else:

                print('\nOpção inválida, tente novamente.\n')

    elif(option == '4'):

        subOption = '1'
        while subOption != '0':

            subOption = input('\tPARTE IV\n\n1. Transformar a imagem\n0. Voltar\nOpção: ')

            if subOption == '1':

                print()

            elif subOption == '0':

                print('\nA voltar...\n')

            else:

                print('\nOpção inválida, tente novamente.\n')

    elif(option == '5'):

        subOption = '1'
        while subOption != '0':

            subOption = input('\tPARTE V\n\n\n0. Voltar\nOpção: ')

            if subOption == '1':

                print()

            elif subOption == '0':

                print('\nA voltar...\n')

            else:

                print('\nOpção inválida, tente novamente.\n')

    elif(option == '0'):

        print('\nPrograma encerrado.\n')

    else:

        print('\nOpção inválida, tente novamente.\n')