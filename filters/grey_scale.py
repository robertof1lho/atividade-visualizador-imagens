import cv2
import numpy as np

def apply_grayscale(img: np.ndarray, intensity: float = 1.0) -> np.ndarray:
    # Converte para escala de cinza e volta para BGR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    # Mistura proporcional entre colorido e cinza
    result = cv2.addWeighted(src1=img, alpha=(1 - intensity), src2=gray_bgr, beta=intensity, gamma=0)
    return result
