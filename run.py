from interface import interface
import cv2
from serve_request import chang_size
from threading import Thread
import threading
import inspect
import ctypes
import numpy as np
import profile
import copy
import time
from serve_request import draw_area, draw_detectdata
from serve_request import set_img_infos, framedetectionfun

def countCameras():
    num_cameiras = 0
    i = 0
    while(True):
        videoCapture = cv2.VideoCapture(i)
        success, frame = videoCapture.read()
        if success:
            num_cameiras = num_cameiras + 1
            i = i + 1
        else:
            break
    return num_cameiras

def videofun():
    num_cameiras = profile.get_global_camera_num()
    videoCapturelist = []
    for i in range(num_cameiras):
        videoCapture = cv2.VideoCapture(i)
        videoCapturelist.append(videoCapture)
        success, frame = videoCapture.read()
        set_img_infos(i, frame)
    camera_ready = False
    while True:
        for i in range(num_cameiras):
            success, frame = videoCapturelist[i].read()
            frame, img_scale = chang_size(frame, 850.)
            profile.set_global_frame_dets(i, copy.deepcopy(frame))
            frame = draw_area(i, frame)
            frame = draw_detectdata(i, frame)
            profile.set_global_frames(i, frame)
        if not camera_ready:
            profile.set_global_camera_ready(True)
            camera_ready = True

def thread_start():
    thread_videofun.start()
    thread_framedetection.start()

def interfacefun(thread_videofun, thread_framedetection):
    interface(thread_videofun, thread_framedetection)

if __name__ == '__main__':
    num_cameiras = countCameras()
    profile.set_global_camera_num(num_cameiras)
    thread_videofun = Thread(target=videofun)
    thread_framedetection = Thread(target=framedetectionfun)
    thread_start()
    interfacefun(thread_videofun, thread_framedetection)
