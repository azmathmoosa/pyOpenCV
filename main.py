'''
The main file which runs all the thread and genreated the gui
'''

import logging
import sys
import threading
import time
import webbrowser
import cv2
import gvars
import modules.video as video
import modules.mjpeg as mjpeg
from bottle import route, run, template, static_file, request

root = logging.getLogger()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)



logging.info("Starting Python CV")

# Static Routes for media
@route('/webroot/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='webroot/')


@route('/webroot/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='webroot/')


@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='webroot/img')


@route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='webroot/fonts')


@route('/')
def home():
    return template('templates/index', host=request.get_header('host'), allcv=gvars.allcv)


def launch_server():
    run(host='localhost', port=3000, debug=True, quiet=True)

def launch_browser():
    time.sleep(2)
    url = "http://localhost:3000"
    webbrowser.open(url, new=2)

def init_gvars_cv2():
    all = dir(cv2)
    gvars.allcv = [all[i] for i in range(len(all)) if '_' not in all[i]]
    print(gvars.allcv)

# reloader is to monitor file changes
# run(server='waitress', host='localhost', port=80, debug=True)

init_gvars_cv2()
gvars.shutDown = False

video.start()


#run(server='waitress', host='0.0.0.0', port=80, debug=True, quiet=True)
serve = threading.Thread(target=launch_server)
serve.start()


launch_browser()

#time.sleep(10)
#gvars.shutDown = True

logging.info("Exiting Kyloren")
time.sleep(2)