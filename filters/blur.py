import cv2
import numpy as np

def apply_blur(img: np.ndarray, ksize: int = 5) -> np.ndarray:
    # Garantir ksize inteiro >= 3
    ksize = int(ksize)
    if ksize < 3:
        ksize = 3
    # Garantir que o kernel seja ímpar
    if ksize % 2 == 0:
        ksize += 1
    # Aplicar Blur
    blurred = cv2.blur(img,(ksize,ksize))
    return blurred
