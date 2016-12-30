"""This module is for processing data from the webcam.
    Incase of no Webcam is found it will try to locate video.mp4 in
    the samples directory and process them
    """

import logging
import threading

import cv2

import gvars
from time import sleep

def process():
    logging.info("Video Thread")
    # Open Video
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        logging.warning("Failed to open!")
        exit(0)


    # Process Video
    while not gvars.shutDown:

        ret, frame = cap.read()
        #cv2.imshow("prev", frame)
        #cv2.waitKey(100)

        gvars.streamImage = frame
        k = (cv2.waitKey(30) & 255)

        if k == ord('q'):
            gvars.shutDown = True


    # Exit Gracefully

    cap.release()
    # cv2.destroyAllWindows()

    logging.info("Exiting Video Thread")


def start():
    logging.info("Starting Video Thread")
    t = threading.Thread(target=process)
    t.start()
