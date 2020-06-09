import numpy as np
import cv2

def from_bstring_to_mat(bstr):
    nparr = np.frombuffer(bstr, dtype='uint8')
    return cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
