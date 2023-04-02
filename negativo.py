import numpy as np

def negativo(img):
    altura, largura, canais = img.shape
    img_out = np.zeros((altura, largura, canais), np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            for c in range(canais):
                img_out[i,j,c] = 255 - img[i,j,c]
    
    return img_out