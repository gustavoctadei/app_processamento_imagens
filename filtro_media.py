import numpy as np

def filtro_media(img, n):
    altura, largura, canais = img.shape
    img_filtro = np.zeros((altura, largura, canais), np.uint8)
    
    for i in range(n//2, altura - n//2):
        for j in range(n//2, largura - n//2):
            for c in range(canais):
                img_filtro[i,j,c] = np.median(img[i-n//2:i+n//2+1, j-n//2:j+n//2+1, c])
    
    return img_filtro