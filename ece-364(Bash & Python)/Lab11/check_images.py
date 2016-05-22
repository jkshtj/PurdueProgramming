import sys
import numpy as np
from numpy import ndarray as nmat
from scipy.misc import *

def areImagesEqual(img1, img2):
    if not isinstance(img1, nmat) or not isinstance(img2, nmat) :
        return False

    if img1.shape != img2.shape:
        return False

    if not np.all(img1 == img2):
        return False

    return True

if __name__ == "__main__":
    filePaths = sys.argv

    if len(filePaths) < 3:
        print("Missing arguments.")

    img1 = imread(filePaths[1])
    img2 = imread(filePaths[2])

    isEqual = areImagesEqual(img1, img2)

    result = "are" if isEqual else "are NOT"
    print("Results {0} equal.".format(result))
