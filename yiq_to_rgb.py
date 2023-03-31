import cv2
import numpy as np

def yiq_to_rgb(img):
    altura, largura, _ = img.shape
    
    R = np.zeros((altura, largura), np.uint8)
    G = np.zeros((altura, largura), np.uint8)
    B = np.zeros((altura, largura), np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            Y, I, Q = img[i,j]
            R[i,j] = Y + 0.956*I + 0.621*Q
            G[i,j] = Y - 0.272*I - 0.647*Q
            B[i,j] = Y - 1.106*I + 1.703*Q
    
    R = np.clip(R, 0, 255).astype(np.uint8)
    G = np.clip(G, 0, 255).astype(np.uint8)
    B = np.clip(B, 0, 255).astype(np.uint8)
    
    return cv2.merge((R, G, B))