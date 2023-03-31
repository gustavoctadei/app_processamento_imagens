import numpy as np

def negativo(img):
    altura, largura, canais = img.shape
    negativo = np.zeros((altura, largura, canais), np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            for c in range(canais):
                negativo[i,j,c] = 255 - img[i,j,c]
    
    return negativo