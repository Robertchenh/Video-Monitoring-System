from interface import interface
import cv2
from serve_request import chang_size
from threading import Thread
import threading
import inspect
import ctypes
import numpy as np
import profile
import time
from serve_request import draw_area, draw_detectdata
from serve_request import set_img_info, framedetectionfun





def videofun():
    videoCapture = cv2.VideoCapture(1)
    success, frame = videoCapture.read()
    set_img_info(frame)
    while success:
        frame, img_scale = chang_size(frame)
        profile.set_global_frame_det(frame)
        frame = draw_area(frame)
        frame = draw_detectdata(frame)
        # cv2.imshow('test', frame)
        # cv2.waitKey(1)
        profile.set_global_frame(frame)
        success, frame = videoCapture.read()





# def _async_raise(tid, exctype):
#     """raises the exception, performs cleanup if needed"""
#     tid = ctypes.c_long(tid)
#     if not inspect.isclass(exctype):
#         exctype = type(exctype)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         # """if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
#
#
# def stop_thread(thread):
#     _async_raise(thread.ident, SystemExit)


def thread_start():
    thread_videofun.start()
    # thread_interfacefun.start()
    thread_framedetection.start()



# def thread_off():
#     stop_thread(thread_videofun)
#     # stop_thread(thread_interfacefun)
#     stop_thread(thread_framedetection)

def interfacefun(thread_videofun, thread_framedetection):
    interface(thread_videofun, thread_framedetection)

if __name__ == '__main__':
    thread_videofun = Thread(target=videofun)
    # thread_interfacefun = Thread(target=interfacefun)
    thread_framedetection = Thread(target=framedetectionfun)
    thread_start()

    interfacefun(thread_videofun, thread_framedetection)

    # thread_off()





    # print('+++++++++++++')
    #


    # videofun()



    # class Tkwin:
    #     def __init__(self, root):
    #         self.root = root
    #         self.frame = Tkinter.Frame(root, bd=2)
    #         self.edit = Tkinter.Text(self.frame, width=96, height=32)
    #         self.edit.pack(side=Tkinter.LEFT)
    #         self.frame.place(y=10)
    #         self.edit.bind('<Button-1>', self.action)
    #
    #
    #     def action(self, event):
    #         self.edit.insert(Tkinter.END, u"x:%d y:%d\n" % (event.x, event.y))
    #         self.edit.insert(Tkinter.END, u"x:%d y:%d\n" % (event.x_root, event.y_root))
    #
    # root = Tkinter.Tk()
    # window = Tkwin(root)
    # root.minsize(600, 480)
    # root.maxsize(600, 480)
    # root.mainloop()