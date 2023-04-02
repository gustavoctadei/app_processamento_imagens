def ler_mascara_de_arquivo_texto():
    arquivo = open('mascara.txt', 'r')
    mascara = arquivo.read()

    return mascara