import cv2
import numpy as np

# aplica alto contraste
def apply_contrast(img: np.ndarray, factor: float = 1.5) -> np.ndarray:
    contrasted = cv2.convertScaleAbs(img * factor)
    return contrasted
