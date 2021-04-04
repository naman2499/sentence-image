import urllib
import urllib.request
import cv2
import numpy as np

def show_url(url):
    # url = 'https://vision.cs.uiuc.edu/pascal-sentences/aeroplane/2008_001227.jpg'

    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    cv2.imshow('lalala', img)
    cv2.waitKey(0)