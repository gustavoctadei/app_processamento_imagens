import cv2
import sys

def carregar_imagem(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    return img

def exibir_imagem(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()