import numpy as np

def convolucao(img, input_mascara, offset):
    altura, largura, canais = img.shape
    
    mascara = np.matrix(input_mascara)
    lin_mascara, col_mascara = mascara.shape
    
    img_conv = np.zeros((altura, largura, canais), np.uint8)
    
    for i in range(lin_mascara//2, altura - lin_mascara//2):
        for j in range(col_mascara//2, largura - col_mascara//2):
            for c in range(canais):
                result = 0
                for mi in range(-lin_mascara//2, lin_mascara//2+1):
                    for mj in range(-col_mascara//2, col_mascara//2+1):
                        if i+mi < 0 or i+mi >= altura or j+mj < 0 or j+mj >= largura:
                            continue
                        result += img[i+mi,j+mj,c] * mascara[lin_mascara//2+mi,col_mascara//2+mj]
                img_conv[i,j,c] = np.clip(result + offset, 0, 255)

    return img_conv