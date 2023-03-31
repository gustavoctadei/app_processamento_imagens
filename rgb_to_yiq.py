import cv2
import numpy as np

def rgb_to_yiq(img):
    altura, largura, _ = img.shape
    
    Y = np.zeros((altura, largura), np.uint8)
    I = np.zeros((altura, largura), np.uint8)
    Q = np.zeros((altura, largura), np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            
            R, G, B = img[i,j]
            Y[i,j] = 0.299*R + 0.587*G + 0.114*B
            I[i,j] = 0.596*R - 0.274*G - 0.322*B
            Q[i,j] = 0.211*R - 0.523*G + 0.312*B
    
    return cv2.merge((Y, I, Q))