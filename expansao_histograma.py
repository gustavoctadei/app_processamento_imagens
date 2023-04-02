import numpy as np
import cv2

def expansao_histograma(img):
    img_out = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    return img_out.astype(np.uint8)