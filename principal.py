from image_util import *
from rgb_to_yiq import *
from yiq_to_rgb import *
from negativo import *
from filtro_media import *

opcao_menu = 1

path_img = input("Digite o Caminho da Imagem: ")
path_img = "img/lena_color_256.tif" # Para teste
img = carregar_imagem(path_img)

while opcao_menu != 0:
    print("Selecione a opcao desejada")
    print("1 - Carregar outra Imagem")
    print("2 - Conversao RGB-YIQ-RGB")
    print("3 - Negativo da Imagem")
    print("4 - Filtro de Media de ordem n x n")
    print("5 - Filtro de Mediana de ordem n x n")
    print("6 - Expansao de Histograma")
    print("7 - Equalizacao de Histograma")
    print("8 - Controle de Contraste Adaptativo")
    print("9 - Gradiente de Sobel")
    print("10 - Convolucao Imagem x Mascara")
    print("0 - Sair")
    opcao_menu = int( input("Digite a sua opção: ") )

    if opcao_menu == 1:
        path_img = input("Digite o Caminho da Imagem: ")
        img = carregar_imagem(path_img)

    if opcao_menu == 2:
        img_yiq = rgb_to_yiq(img)
        img_rgb = yiq_to_rgb(img_yiq)
        exibir_imagem(img_rgb)

    elif opcao_menu == 3:
        img_neg = negativo(img)
        exibir_imagem(img_neg)

    elif opcao_menu == 4:
        n = int( input("Digite o valor de n: ") )
        img_filtro = filtro_media(img, n)
        exibir_imagem(img_filtro)

    elif opcao_menu == 5:
        print("Em desenvolvimento")

    elif opcao_menu == 6:
        print("Em desenvolvimento")

    elif opcao_menu == 7:
        print("Em desenvolvimento")

    elif opcao_menu == 8:
        print("Em desenvolvimento")

    elif opcao_menu == 9:
        print("Em desenvolvimento")

    elif opcao_menu == 10:
        print("Em desenvolvimento")

    elif opcao_menu == 0:
        print("Saindo...")

    elif opcao_menu < 0 or opcao_menu > 5:
        print("Opcao Invalida. Favor, tente novamente")