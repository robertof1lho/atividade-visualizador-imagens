import cv2
import numpy as np

def apply_invert(img: np.ndarray, intensity: float = 1.0) -> np.ndarray:
    # Imagem invertida total
    inverted = cv2.bitwise_not(img)
    # Mistura proporcional entre original e invertida
    result = cv2.addWeighted(src1=img, alpha=(1 - intensity), src2=inverted, beta=intensity, gamma=0)
    return result