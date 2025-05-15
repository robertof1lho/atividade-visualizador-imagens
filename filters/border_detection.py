import cv2
import numpy as np

def apply_edge(img: np.ndarray, ksize: int = 3) -> np.ndarray:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Uso de profundidade maior para evitar estouro de valores
    ddepth = cv2.CV_16S
    
    ksize = int(ksize)
    if ksize < 3:
        ksize = 3
    if ksize % 2 == 0:
        ksize += 1
        
    # Derivada primeira ordem em X e Y
    grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=ksize)
    grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=ksize)
    # Valor absoluto e conversão para uint8
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    # Combinação das derivadas
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    # Converte de volta para BGR
    edge_bgr = cv2.cvtColor(grad, cv2.COLOR_GRAY2BGR)
    return edge_bgr
