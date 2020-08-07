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

def parse_duration(str):
    if str.endswith('ms'):
        return int(str[0:-2])
    elif str.endswith('s'):
        return int(str[0:-1]) * 1000
    elif str.endswith('m'):
        return int(str[0:-1]) * 1000 * 60
    elif str.endswith('h'):
        return int(str[0:-1]) * 1000 * 60 * 60
    elif str.endswith('d'):
        return int(str[0:-1]) * 1000 * 60 * 60 * 24
    elif str.endswith('w'):
        return int(str[0:-1]) * 1000 * 60 * 60 * 24 * 7
    else:
        return int(str)