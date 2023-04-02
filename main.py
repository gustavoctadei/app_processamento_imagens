from image_util import *
from rgb_to_yiq import *
from yiq_to_rgb import *
from negativo import *
from filtro_media import *
from filtro_mediana import *
from convolucao import *
from expansao_histograma import *
from equalizacao_histograma import *
from contraste_adaptativo import *
from gradiente_sobel import *
from arquivo_util import *

opcao_menu = 1

path_img = input("Digite o Caminho da Imagem (Ex: img/lena_color_256.tif): ")
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
    print("10 - Convolucao Imagem x Mascara (definida no arquivo mascara.txt)")
    print("")
    print("0 - Sair")
    opcao_menu = int( input("Digite a sua opção: ") )

    if opcao_menu == 1:
        path_img = input("Digite o Caminho da Imagem (Ex: img/lena_color_256.tif): ")
        img = carregar_imagem(path_img)

    if opcao_menu == 2:
        img_yiq = rgb_to_yiq(img)
        img_out = yiq_to_rgb(img_yiq)

    elif opcao_menu == 3:
        img_out = negativo(img)

    elif opcao_menu == 4:
        n = int( input("Digite o valor de n: ") )
        img_out = filtro_media(img, n)

    elif opcao_menu == 5:
        n = int( input("Digite o valor de n: ") )
        img_out = filtro_mediana(img, n)

    elif opcao_menu == 6:
        img_out = expansao_histograma(img)

    elif opcao_menu == 7:
        img_out = equalizacao_histograma(img)

    elif opcao_menu == 8:
        c = int( input("Digite o valor de c: ") )
        n = int( input("Digite o valor de n: ") )
        img_out = contraste_adaptativo(img, c, n)

    elif opcao_menu == 9:
        img_out = gradiente_sobel(img)

    elif opcao_menu == 10:
        input_mascara = ler_mascara_de_arquivo_texto()
        offset = int( input("Insira o Offset: ") )
        img_out = convolucao(img, input_mascara, offset)

    elif opcao_menu == 0:
        print("Saindo...")

    elif opcao_menu < 0 or opcao_menu > 5:
        print("Opcao Invalida. Favor, tente novamente")

    if opcao_menu != 1 and opcao_menu != 0 and not ( opcao_menu < 0 or opcao_menu > 10 ):
        print("Exibindo a imagem resultante...")
        exibir_imagem(img_out)