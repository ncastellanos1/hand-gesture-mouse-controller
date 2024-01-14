import os
import cv2


def load_cascade(file):
    """Load a cascade classifier from a file"""
    if not os.path.isfile(file):
        raise ValueError(f'Cascade classifier file not found: {file}')
    return cv2.CascadeClassifier(file)
