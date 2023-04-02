import numpy as np
import cv2

def contraste_adaptativo(image, c, n):
    img_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    altura, largura = img_cinza.shape
    
    img_out = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            
            inicio_i = max(0, i - n//2)
            fim_i = min(altura, i + n//2 + 1)
            inicio_j = max(0, j - n//2)
            fim_j = min(largura, j + n//2 + 1)
            vizinhanca = img_cinza[inicio_i:fim_i, inicio_j:fim_j]
            
            media = np.mean(vizinhanca)
            desvio_padrao = np.std(vizinhanca)
            
            if desvio_padrao > 0:
                img_out[i, j] = np.clip(img_cinza[i, j] - c*media/desvio_padrao, 0, 255)
            else:
                img_out[i, j] = img_cinza[i, j]

    return img_out