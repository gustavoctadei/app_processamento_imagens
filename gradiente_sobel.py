import cv2

def gradiente_sobel(image):
    img_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    sobelx = cv2.Sobel(img_cinza, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img_cinza, cv2.CV_64F, 0, 1, ksize=3)
    
    magnitude = cv2.magnitude(sobelx, sobely)
    img_out = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    
    return img_out