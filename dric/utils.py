import numpy as np
import cv2
from collections import namedtuple

def current_millis():
    import time
    return int(round(time.time() * 1000))

def from_bstring_to_mat(bstr):
    nparr = np.frombuffer(bstr, dtype='uint8')
    return cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

def to_bstring_from_mat(mat):
    bstr = mat.tobytes()
    return bstr