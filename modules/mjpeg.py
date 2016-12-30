"""File is used to stream the mjpeg stream to the display"""

from time import sleep

import cv2

import gvars
from bottle import route, response

CRLF = "\r\n"
BOUNDARY = "arflebarfle"

class MJPEG(object):

    counter = 0

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        sleep(30.0 / 1000)

        #print(gvars.streamImage)
        r, streamFrame = cv2.imencode(".jpg", gvars.streamImage)
        data = bytearray(streamFrame)

        self.counter += 1

        # Add the frame boundary to the output
        out = "--" + BOUNDARY + CRLF

        # Add the jpg frame header
        out += "Content-type: image/jpeg" + CRLF

        # Add the frame content length
        out += "Content-length: " + str(len(data)) + CRLF + CRLF

        # Add the actual binary jpeg frame data
        return str.encode(out) + data

    def stop(self):
        pass


@route('/mjpg')
def mjpg():
    response.content_type = "multipart/x-mixed-replace;boundary=" + BOUNDARY
    return iter(MJPEG())

@route('/live.jpg')
def livejpg():
    data = ""
    try:
        response.set_header('Content-type', 'image/jpeg')
        r, streamFrame = cv2.imencode(".jpg", gvars.streamImage)
        imageData = bytearray(streamFrame)
        data = str.encode("") + imageData
    except:
        pass
    return data