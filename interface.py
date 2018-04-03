from Tkinter import *
from profile import def_val
from serve_request import chang_size
import Image, ImageTk
import cv2
import numpy as np
import profile
import time
from threading import Thread
import copy
import sys
import os

import threading
import inspect
import ctypes

def center_window(w, h, root):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    profile.set_global_root_xy(copy.deepcopy([x, y]))
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def major_interface(root):
    topframe = Frame(width=def_val.topframe_width, height=def_val.topframe_height, bg=def_val.topframe_bg)
    topframe.grid(row=0, column=0, rowspan=1, columnspan=9, ipadx=0, ipady=0, sticky=NW)
    topframe.grid_propagate(0)

    lframe = Frame(width=def_val.lframe_width, height=def_val.lframe_height, bg=def_val.lframe_bg)
    lframe.grid(row=1, column=0, rowspan=3, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    lframe.grid_propagate(0)

    t1frame = Frame(width=def_val.t1frame_width, height=def_val.t1frame_height, bg=def_val.t1frame_bg)
    t1frame.grid(row=1, column=1, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t1frame.grid_propagate(0)
    t2frame = Frame(width=def_val.t2frame_width, height=def_val.t2frame_height, bg=def_val.t2frame_bg)
    t2frame.grid(row=1, column=2, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t2frame.grid_propagate(0)
    t3frame = Frame(width=def_val.t3frame_width, height=def_val.t3frame_height, bg=def_val.t3frame_bg)
    t3frame.grid(row=1, column=3, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t3frame.grid_propagate(0)
    t4frame = Frame(width=def_val.t4frame_width, height=def_val.t4frame_height, bg=def_val.t4frame_bg)
    t4frame.grid(row=1, column=4, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t4frame.grid_propagate(0)
    t5frame = Frame(width=def_val.t5frame_width, height=def_val.t5frame_height, bg=def_val.t5frame_bg)
    t5frame.grid(row=1, column=5, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t5frame.grid_propagate(0)
    t6frame = Frame(width=def_val.t6frame_width, height=def_val.t6frame_height, bg=def_val.t6frame_bg)
    t6frame.grid(row=1, column=6, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t6frame.grid_propagate(0)
    t7frame = Frame(width=def_val.t7frame_width, height=def_val.t7frame_height, bg=def_val.t7frame_bg)
    t7frame.grid(row=1, column=7, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    t7frame.grid_propagate(0)

    cframe = Frame(width=def_val.cframe_width, height=def_val.cframe_height, bg=def_val.cframe_bg)
    cframe.grid(row=2, column=1, rowspan=2, columnspan=7,ipadx=0, ipady=0, sticky=NW)
    cframe.grid_propagate(0)

    r1frame = Frame(width=def_val.r1frame_width, height=def_val.r1frame_height, bg=def_val.r1frame_bg)
    r1frame.grid(row=1, column=8, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    r1frame.grid_propagate(0)

    r2frame = Frame(width=def_val.r2frame_width, height=def_val.r2frame_height, bg=def_val.r2frame_bg)
    r2frame.grid(row=2, column=8, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    r2frame.grid_propagate(0)

    r3frame = Frame(width=def_val.r3frame_width, height=def_val.r3frame_height, bg=def_val.r3frame_bg)
    r3frame.grid(row=3, column=8, rowspan=1, columnspan=1,ipadx=0, ipady=0, sticky=NW)
    r3frame.grid_propagate(0)
    return topframe, lframe, t1frame, t2frame, t3frame, t4frame, t5frame, t6frame, t7frame, cframe, r1frame, r2frame, r3frame

def topframe_items(topframe):
    pass

def OFF_fun():
    # thread_off(thread_videofun, thread_framedetection)
    # exit()
    # sys.exit()
    # os._exit()
    pass

def RESET_fun():
    profile.clear_global_detect_areas()




# def ADD_fun():
#     if profile.get_global_add_area():
#         detect_area = profile.get_global_detect_area()
#         detect_area_len = len(detect_area)
#         global_temvar = copy.deepcopy(profile.get_global_temvar())
#         area_dict = {str(detect_area_len + 1): global_temvar}
#         print(type(area_dict))
#         profile.set_global_detect_area(area_dict)
#         profile.clear_global_temvar()
#         profile.set_global_add_area(False)


def DELETE_fun(img_canvas):
    pass


def CLS_fun():
    # pass
    profile.clear_global_temvar()

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

# def thread_off(thread_videofun, thread_framedetection):
#     stop_thread(thread_videofun)
#     # stop_thread(thread_interfacefun)
#     stop_thread(thread_framedetection)


class MyButton:
    def __init__(self, name, father, width, height, x, y, fun):
        self.name = name
        self.father = father
        self.fun = fun
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.button = Button(self.father, text=self.name, width=self.width, height=self.height, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
        self.button.place(x=self.x, y=self.y, anchor=CENTER)
        self.button.bind('<Button-1>', self.action)
    def action(self, event):
        self.fun()


class MyText:
    def __init__(self, father, width, height):
        self.father = father
        self.width = width
        self.height = height
        self.messagelist = []
        self.labellist = []
        for m in range(100, 118):
            self.m = StringVar()
            self.messagelist.append(self.m)
        self.info_tittle = Label(self.father, text='Detecting Message Logging', width=110, height=1, fg='#000000', bg='#00FF00')
        self.info_tittle.grid(row=0, column=0)
        for l in range(18):
            self.l = Label(self.father, textvariable = self.messagelist[l], width=110, height=1, fg='#000000', bg='#00FF00')
            self.l.grid(row=l + 1, column=0)
            self.labellist.append(self.l)

        # self.action()
    def action(self):
        message_log = profile.get_global_message_log()
        # print message_log
        info_len = len(message_log)
        if info_len < 18:
            for i in range(info_len):
                self.messagelist[i].set(message_log[i])
                if message_log[i].find("abnormal") != -1:
                    self.labellist[i]['fg'] = '#FF0000'
                else:
                    self.labellist[i]['fg'] = '#000000'
        else:
            for i in range(18):
                self.messagelist[i].set(message_log[(i - 18)])
                if message_log[(i - 18)].find("abnormal") != -1:
                    self.labellist[i]['fg'] = '#FF0000'
                else:
                    self.labellist[i]['fg'] = '#000000'

        # self.after(10, self.action())

def t1frame_items(frame):
    LAST_button = Button(frame, text='LAST', width=2, height=8, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
    LAST_button.place(x=25, y=75, anchor=CENTER)

def t7frame_items(frame):
    NEXT_button = Button(frame, text='NEXT', width=2, height=8, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
    NEXT_button.place(x=25, y=75, anchor=CENTER)

def mouse_motion_fun(event):
    # draw_mouse()
    show_id = profile.get_global_camera_show_id()
    img_info = profile.get_global_img_infos(show_id)
    # print (event.x, event.y)
    if img_info[2] < event.y and event.y < img_info[3]:
        profile.set_global_mouse_xy(copy.deepcopy([event.x -2, event.y - img_info[2] -2]))
        # print([event.x -2, event.y - img_info[2] -2])
        profile.set_global_temvar(profile.get_global_mouse_xy()[0], profile.get_global_mouse_xy()[1])
        # print profile.get_global_temvar()


def mouse_in_fun(event):
    profile.set_global_mousein(True)
    print("mouse in")


def mouse_out_fun(event):
    profile.set_global_mousein(False)
    print("mouse out")

def add_point_fun(event):

    mousexy = profile.get_global_mouse_xy()
    temvar = profile.get_global_temvar()

    if len(temvar) > 0:
        distance = np.sqrt(np.square(mousexy[0] - temvar[0][0]) + np.square(mousexy[1] - temvar[0][1]))
        if distance > 10:
            profile.get_global_temvar().append(profile.get_global_mouse_xy())
        else:
            profile.set_global_add_area(True)

        print("add a point")
        print(profile.get_global_temvar())
    else:
        profile.get_global_temvar().append(profile.get_global_mouse_xy())


def add_point_fun01(event):
    show_id = profile.get_global_camera_show_id()
    img_info = profile.get_global_img_infos(show_id)
    # print (event.x, event.y)
    if img_info[2] < event.y and event.y < img_info[3]:
        profile.clear_global_temvar()
        profile.set_global_temvar(copy.deepcopy(event.x - 2), copy.deepcopy(event.y - img_info[2] - 2))
    # print('+++++++++++++++++')

def interface(thread_videofun, thread_framedetection):
    while True:
        camera_ready = profile.get_global_camera_ready()
        print("cameras is readying, please waiting!\n")
        if camera_ready:
            break
    camera_num = profile.get_global_camera_num()
    while True:
        if not camera_num:
            print("no camera")
        else:
            break
    root = Tk()
    center_window(def_val.root_width, def_val.root_height, root)
    root.resizable(def_val.root_resizable, def_val.root_resizable)
    # root.wm_attributes('-type', 'splash')
    topframe, lframe, t1frame, t2frame, t3frame, t4frame, t5frame, t6frame, t7frame, cframe, r1frame, r2frame, r3frame = major_interface(root)
    img_canvas = Canvas(cframe, width=def_val.cframe_width, height=def_val.cframe_height, bg='#000000')
    img_canvas.grid()
    img_canvas.grid_propagate(0)
    topframe_items(topframe)
    softwarename = Label(topframe, text='Video Monitoring System',  font=('Times', 12), height=1, fg='#FF0000', bg='#000000')
    softwarename.grid()

    OFF_button = Button(lframe, text='OFF', width=7, height=3, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
    OFF_button.place(x=50, y=180, anchor=CENTER)

    RESET_button = MyButton('RESET', lframe, 7, 3, 50, 270, RESET_fun)
    info_show = MyText(r2frame, 800, 350)

    LAST_button = Button(t1frame, text='LAST', width=2, height=8, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
    LAST_button.place(x=25, y=75, anchor=CENTER)
    NEXT_button = Button(t7frame, text='NEXT', width=2, height=8, fg='#FF0000', bg='#D3D3D3', bd=3, relief='groove')
    NEXT_button.place(x=25, y=75, anchor=CENTER)

    label_img = Label(img_canvas, width=def_val.cframe_width, height=def_val.cframe_height, bg='#EEDFCC')
    label_img.place(x=425, y=425, anchor=CENTER)


    label_t2 = Frame(t2frame, width=146, height=150, bg=def_val.top_image_notshow_bg)
    label_t2.place(x=75, y=75, anchor=CENTER)
    label_t3 = Frame(t3frame, width=146, height=150, bg=def_val.top_image_notshow_bg)
    label_t3.place(x=75, y=75, anchor=CENTER)
    label_t4 = Frame(t4frame, width=146, height=150, bg=def_val.top_image_notshow_bg)
    label_t4.place(x=75, y=75, anchor=CENTER)
    label_t5 = Frame(t5frame, width=146, height=150, bg=def_val.top_image_notshow_bg)
    label_t5.place(x=75, y=75, anchor=CENTER)
    label_t6 = Frame(t6frame, width=146, height=150, bg=def_val.top_image_notshow_bg)
    label_t6.place(x=75, y=75, anchor=CENTER)
    lable_ts = [label_t2, label_t3, label_t4, label_t5, label_t6]


    showlabel_t2 = Label(label_t2, width=146, height=146, bg=def_val.top_image_notshow_bg)
    showlabel_t2.place(x=73, y=73, anchor=CENTER)
    showlabel_t3 = Label(label_t3, width=146, height=146, bg=def_val.top_image_notshow_bg)
    showlabel_t3.place(x=73, y=73, anchor=CENTER)
    showlabel_t4 = Label(label_t4, width=146, height=146, bg=def_val.top_image_notshow_bg)
    showlabel_t4.place(x=73, y=73, anchor=CENTER)
    showlabel_t5 = Label(label_t5, width=146, height=146, bg=def_val.top_image_notshow_bg)
    showlabel_t5.place(x=73, y=73, anchor=CENTER)
    showlabel_t6 = Label(label_t6, width=146, height=146, bg=def_val.top_image_notshow_bg)
    showlabel_t6.place(x=73, y=73, anchor=CENTER)
    showlable_ts = [showlabel_t2, showlabel_t3, showlabel_t4, showlabel_t5, showlabel_t6]

    def show_topframe(label, id):
        frame = profile.get_global_frame_dets(id)
        frame, _ = chang_size(frame, 146.)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)

    def change_bg(id):
        for i in range(5):
            lable_ts[i]['bg'] = def_val.top_image_notshow_bg
        lable_ts[id]['bg'] = def_val.top_image_show_bg


    def show_topframes():
        camera_num = profile.get_global_camera_num()
        show_id = profile.get_global_camera_show_id()
        if camera_num < 5:
            for i in range(camera_num):
                show_topframe(showlable_ts[i], i)
            change_bg(show_id)

        else:
            if show_id < 5:
                for i in range(5):
                    show_topframe(showlable_ts[i], i)
                    change_bg(show_id)
            else:
                for i in range(5):
                    show_topframe(showlable_ts[4 - i], show_id - i)

    def LAST_fun(event):
        show_id = profile.get_global_camera_show_id()
        if show_id > 0:
            show_id = show_id - 1
            profile.set_global_camera_show_id(show_id)

    def NEXT_fun(event):
        cameranum = profile.get_global_camera_num()
        show_id = profile.get_global_camera_show_id()
        if show_id < (cameranum - 1):
            show_id = show_id + 1
            profile.set_global_camera_show_id(show_id)

    def MessageBox():
        temvar = profile.get_global_temvar()

        def savekey():
            key = sheet_text.get()
            if len(key) < 1  or key[0]==' ':
                message.set('Wrong id! enter again!')
            else:
                show_id = profile.get_global_camera_show_id()
                profile.set_global_key_in(key)
                message.set('Submit Successful!')
                global_temvar = copy.deepcopy(profile.get_global_temvar())
                if len(global_temvar) > 1:
                    area_dict = {profile.get_global_key_in(): global_temvar}
                    print(area_dict)
                    print('add area')
                    profile.set_global_detect_areas(show_id, area_dict)
                    profile.clear_global_temvar()
                    profile.set_global_add_area(False)
                    # key_in.grid_forget()
                    # quit
                    key_in.destroy()

        def delete():
            profile.clear_global_temvar()
            key_in.destroy()


        if len(temvar) > 1:
            s = abs((temvar[0][0] - temvar[1][0]) * (temvar[0][1] - temvar[1][1]))
            if s > 10000:
                key_in = Toplevel(img_canvas)
                key_in.wm_attributes('-type', 'splash')
                key_in.title('enter id!')
                xy = profile.get_global_root_xy()
                key_in.geometry('%dx%d+%d+%d' % (200, 130, xy[0] + 500, xy[1] + 500))

                Label(key_in, text='Please enter the id: ', fg = "#FF0000", font=('Times', 14)).place(x=100, y=15, anchor=CENTER)
                sheet_text = StringVar()
                entry = Entry(key_in, textvariable=sheet_text)
                entry.place(x=100, y=45, anchor=CENTER)
                sheet_text.set('')
                message = StringVar()
                Label(key_in, textvariable=message).place(x=100, y=75, anchor=CENTER)
                message.set('')
                Button(key_in, text='Submit', command=savekey).place(x=50, y=105, anchor=CENTER)
                Button(key_in, text='Delete', command=delete).place(x=150, y=105, anchor=CENTER)
            else:
                profile.clear_global_temvar()




    def add_area_fun(event):
        MessageBox()
        # thread_MessageBox = Thread(target=MessageBox())
        # thread_MessageBox.start()



    def show_frame():
        show_id = profile.get_global_camera_show_id()
        frame = profile.get_global_frames(show_id)
        # frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label_img.imgtk = imgtk
        label_img.configure(image=imgtk)
        # if profile.get_global_mousein():
        #     draw_mouse()
        info_show.action()
        show_topframes()
        label_img.after(10, show_frame)

    def movewindow_fun(event):
        if profile.get_global_mouse_move_release():
            xy = [event.x_root, event.y_root]
            profile.set_global_mouse_move_xy(copy.deepcopy(xy))


            profile.set_global_mouse_move_release(False)

        move_x = event.x_root - profile.get_global_mouse_move_xy()[0]
        move_y = event.y_root - profile.get_global_mouse_move_xy()[1]
        profile.set_global_move_xy(copy.deepcopy([move_x, move_y]))

        root_xy = profile.get_global_root_xy()
        x = root_xy[0] + move_x
        y = root_xy[1] + move_y
        root.geometry('%dx%d+%d+%d' % (def_val.root_width, def_val.root_height, x, y))

        # profile.set_global_root_xy(copy.deepcopy([x, y]))

    def mouse_release_fun(event):
        profile.set_global_mouse_move_release(True)
        move_xy = profile.get_global_move_xy()
        root_xy = profile.get_global_root_xy()
        x = root_xy[0] + move_xy[0]
        y = root_xy[1] + move_xy[1]
        profile.set_global_root_xy(copy.deepcopy([x, y]))

    def thread_off(event):
        stop_thread(thread_videofun)
        stop_thread(thread_framedetection)
        sys.exit()
        # print('end of program')

    label_img.bind('<B1-Motion>', mouse_motion_fun)
    label_img.bind('<Button-1>', add_point_fun01)

    label_img.bind('<Enter>', mouse_in_fun)

    label_img.bind('<Leave>', mouse_out_fun)

    label_img.bind('<ButtonRelease-1>', add_area_fun)

    topframe.bind('<B1-Motion>', movewindow_fun)
    topframe.bind('<ButtonRelease-1>', mouse_release_fun)
    OFF_button.bind('<Button-1>', thread_off)

    LAST_button.bind('<Button-1>', LAST_fun)
    NEXT_button.bind('<Button-1>', NEXT_fun)

    show_frame()
    root.mainloop()