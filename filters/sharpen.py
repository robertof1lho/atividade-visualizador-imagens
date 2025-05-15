import cv2
import numpy as np

def apply_sharpen(img: np.ndarray, strength: float = 1.5, ksize: int = 3) -> np.ndarray:
    ksize = int(ksize)
    if ksize < 3:
        ksize = 3
    if ksize % 2 == 0:
        ksize += 1
    # Aplicar Gaussian Blur para obter versão suavizada
    blurred = cv2.GaussianBlur(img, (ksize, ksize), sigmaX=0)
    # Mistura entre imagem original e diferenca para nitidez
    sharpened = cv2.addWeighted(src1=img, alpha=1.0 + strength, src2=blurred, beta=-strength, gamma=0)
    return sharpened
