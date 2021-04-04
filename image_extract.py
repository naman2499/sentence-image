import urllib
import urllib.request
import cv2
import numpy as np

def show_url(url):

    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    cv2.imshow('lalala', img)
    cv2.waitKey(0)