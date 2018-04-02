import os
import numpy as np
from easydict import EasyDict as edict
import numpy as np
import copy
import cv2

class global_val():
    # frame = np.array([])
    frames = {}

    # frame_det = np.array([])
    frame_dets = {}

    # img_info = [0, 0, 0, 0]
    img_infos = {}

    # detect_area = {}
    detect_areas = {}

    temvar = []

    mousein = False

    mouse_xy = [0, 0]

    add_area = False

    message_log = []

    get_message = False

    # detect_data = {}
    detect_datas = {}

    mouse_move_xy = [0, 0]
    mouse_move_release = True
    root_xy = [0, 0]
    move_xy = [0, 0]

    add_firstpoint = True

    key_in = ''


    # data_change = {}
    data_changes = {}

    # time_show = 0.01
    time_shows ={}
    camera_num = 0

    camera_show_id = 0









# def set_global_frame(global_frame):
#     global_val.frame = global_frame
#
# def get_global_frame():
#     return global_val.frame

def set_global_frames(key, global_frame):
    global_val.frames.update({key:global_frame})

def get_global_frames(key):
    if not global_val.frames.has_key(key):
        global_val.frames.update({key:np.array([])})
    return global_val.frames[key]



# def set_global_frame_det(global_frame_det):
#     global_val.frame_det = global_frame_det
#
# def get_global_frame_det():
#     return global_val.frame_det

def set_global_frame_dets(key, global_frame_det):
    global_val.frame_dets.update({key:global_frame_det})


def get_global_frame_dets(key):
    if not global_val.frame_dets.has_key(key):
        global_val.frame_dets.update({key:np.array([])})
    return global_val.frame_dets[key]

# def set_global_img_info(w, h, y1, y2):
#     global_val.img_info = [w, h, y1, y2]
#
# def get_global_img_info():
#     return global_val.img_info


def set_global_img_infos(key, info):
    global_val.img_infos.update({key:info})

def get_global_img_infos(key):
    if not global_val.img_infos.has_key(key):
        global_val.img_infos.update({key:np.array([])})
    return global_val.img_infos[key]




# def set_global_detect_area(area_dict):
#     global_val.detect_area.update(area_dict)
#     print('add detect area')
#     print(get_global_detect_area())
#
# def clear_global_detect_area():
#     global_val.detect_area.clear()
#
# def get_global_detect_area():
#     return global_val.detect_area


def set_global_detect_areas(key,area_dict):

    global_val.detect_areas[key].update(area_dict)

def clear_global_detect_areas():
    global_val.detect_areas.clear()

def get_global_detect_areas(key):
    if not global_val.detect_areas.has_key(key):
        global_val.detect_areas.update({key:{}})
    return global_val.detect_areas[key]


def set_global_temvar(x, y):
    temvar_len = len(global_val.temvar)
    if temvar_len < 2:
        global_val.temvar.append([x, y])
    else:
        global_val.temvar[1] = copy.deepcopy([x, y])

def clear_global_temvar():
    global_val.temvar[:] = []
    print('clear temvar')

def get_global_temvar():
    return global_val.temvar

def set_global_mousein(bool_var):
    global_val.mousein = bool_var

def get_global_mousein():
    return global_val.mousein

def set_global_mouse_xy(xy):

    global_val.mouse_xy = xy

def get_global_mouse_xy():
    return global_val.mouse_xy

def set_global_add_area(boolvar):
    global_val.add_area = boolvar

def get_global_add_area():
    return global_val.add_area

def set_global_message_log(message):
    global_val.message_log.append(message)

def get_global_message_log():
    return global_val.message_log

def set_global_get_message(bool_var):
    global_val.get_message = bool_var

def get_global_get_message():
    return global_val.get_message




# def set_global_detect_data(detect_data_):
#     global_val.detect_data = detect_data_
#
# def get_global_detect_data():
#     return global_val.detect_data

def set_global_detect_datas(key,detect_data_):
    global_val.detect_datas.update({key:detect_data_})

def get_global_detect_datas(key):
    if not global_val.detect_datas.has_key(key):
        global_val.detect_datas.update({key:{}})
    return global_val.detect_datas[key]





def set_global_mouse_move_xy(xy):
    global_val.mouse_move_xy = xy

def get_global_mouse_move_xy():
    return global_val.mouse_move_xy


def set_global_mouse_move_release(bool_var):
    global_val.mouse_move_release = bool_var

def get_global_mouse_move_release():
    return global_val.mouse_move_release

def set_global_root_xy(xy):
    global_val.root_xy = xy

def get_global_root_xy():
    return global_val.root_xy


def set_global_move_xy(xy):
    global_val.move_xy = xy


def get_global_move_xy():

    return global_val.move_xy

def set_global_add_firstpoint(bool_var):
    global_val.add_firstpoint = bool_var

def get_global_add_firstpoint():
    return global_val.add_firstpoint


def set_global_key_in(key_in):
    global_val.key_in = key_in
    print('add key Successful!')

def get_global_key_in():
    return global_val.key_in



# def set_global_data_change(data_dict):
#     global_val.data_change.update(data_dict)
#
# def clear_global_data_change():
#     global_val.data_change.clear()
#
# def get_global_data_change():
#     return global_val.data_change



def set_global_data_changes(key,data_dict):
    global_val.data_changes.update({key:data_dict})

def clear_global_data_changes(key):
    global_val.data_changes[key].clear()

def get_global_data_changes(key):
    if not global_val.data_changes.has_key(key):
        global_val.data_changes.update({key:{}})
    return global_val.data_changes[key]





def set_global_timeshows(key ,timeshow):
    global_val.time_shows.update({key:timeshow})

def get_global_timeshows():
    return global_val.time_shows


def set_global_camera_num(camera_num):
    global_val.camera_num = camera_num

def get_global_camera_num():
    return global_val.camera_num





def set_global_camera_show_id(camera_show_id):
    global_val.camera_show_id = camera_show_id

def get_global_camera_show_id():
    return global_val.camera_show_id




def_val = edict()

# distribution parameter
def_val.root_width = 1800
def_val.root_height = 1025
def_val.root_resizable = False

def_val.topframe_width = 1800
def_val.topframe_height = 25
def_val.topframe_bg = '#000000'

def_val.lframe_width = 100
def_val.lframe_height = 1000
def_val.lframe_bg = '#E6E6FA'

def_val.t1frame_width = 50
def_val.t1frame_height = 150
def_val.t1frame_bg = '#D1EEEE'
def_val.t2frame_width = 150
def_val.t2frame_height = 150
def_val.t2frame_bg = '#E6E6FA'
def_val.t3frame_width = 150
def_val.t3frame_height = 150
def_val.t3frame_bg = '#E6E6FA'
def_val.t4frame_width = 150
def_val.t4frame_height = 150
def_val.t4frame_bg = '#E6E6FA'
def_val.t5frame_width = 150
def_val.t5frame_height = 150
def_val.t5frame_bg = '#E6E6FA'
def_val.t6frame_width = 150
def_val.t6frame_height = 150
def_val.t6frame_bg = '#E6E6FA'
def_val.t7frame_width = 50
def_val.t7frame_height = 150
def_val.t7frame_bg = '#D1EEEE'


def_val.cframe_width = 850
def_val.cframe_height = 850
def_val.cframe_bg = '#000000'

def_val.r1frame_width = 850
def_val.r1frame_height = 150
def_val.r1frame_bg = '#E6E6FA'

def_val.r2frame_width = 850
def_val.r2frame_height = 350
def_val.r2frame_bg = '#000000'

def_val.r3frame_width = 850
def_val.r3frame_height = 500
def_val.r3frame_bg = '#000000'



def_val.area_color = (255, 0, 0)

def_val.circle_color0 =(0, 0, 255)
def_val.circle_color1 =(255, 0, 0)

def_val.line_color = (0, 255, 255)




def_val.top_image_notshow_bg = '#D1EEEE'
def_val.top_image_show_bg = '#660066'







