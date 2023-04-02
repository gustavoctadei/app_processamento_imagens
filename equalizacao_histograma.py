
import cv2

def equalizacao_histograma(image):
    imagem_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    imagem_equalizada = cv2.equalizeHist(imagem_cinza)
    
    return imagem_equalizada