import numpy as np
import cv2
import profile
from profile import def_val
import time
import requests
import json
import copy


def chang_size(img, scale):
    img_width = img.shape[1]
    img_height = img.shape[0]
    image_scale = scale / img_width
    if (image_scale * img_height) > scale:
        image_scale = scale / img_height
    img = cv2.resize(img, (int(round(img_width * image_scale, 0)), int(round(img_height * image_scale, 0))), interpolation=cv2.INTER_CUBIC)

    return img, image_scale


def draw_area(id, frame):
    detect_area = profile.get_global_detect_areas(id)
    show_id = profile.get_global_camera_show_id()
    temvar = profile.get_global_temvar()
    if len(detect_area) > 0:
        for key, values in detect_area.items():
            frame = cv2.rectangle(frame, (values[0][0], values[0][1]), (values[1][0], values[1][1]), def_val.area_color, 2)
            xy = np.mean(np.array(values), axis=0)
            cv2.putText(frame, key , (int(xy[0]), int(xy[1])), cv2.QT_FONT_NORMAL, 0.5, (0, 0, 255), 1)

    if (show_id == id) and (len(temvar) > 1):
        frame = cv2.rectangle(frame, (temvar[0][0], temvar[0][1]), (temvar[1][0], temvar[1][1]), def_val.area_color, 1)

    return frame


def draw_detectdata(id, frame):
    get_data = profile.get_global_detect_datas(id)
    for i in range(len(get_data)):
        class_name_val = get_data[str(i)][0]
        if class_name_val == 'person':
            bbox_val = get_data[str(i)][2]
            score_val = get_data[str(i)][1]
            x1 = int(bbox_val[0])
            y1 = int(bbox_val[1])
            x2 = int(bbox_val[2])
            y2 = int(bbox_val[3])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (135, 206, 255), 1)
            cv2.putText(frame, '{:s} {:.3f}'.format(class_name_val, score_val), (x1, y1 - 7),
                        cv2.QT_FONT_NORMAL, 0.5, (135, 206, 255), 1)
    return frame

# def draw_mouse():
#     frame = profile.get_global_frame()
#     xy = profile.get_global_mouse_xy()
#     img_info = profile.get_global_img_info()
#     if 0 < xy[1] and xy[1] < img_info[1]:
#         cv2.line(frame, (xy[0] - 20, xy[1]), (xy[0] + 20, xy[1]), (0, 255, 0), 1)
#         cv2.line(frame, (xy[0], xy[1] - 20), (xy[0], xy[1] + 20), (0, 255, 0), 1)


def set_img_infos(id, frame):
    frame, img_scale = chang_size(frame, 850.)
    img_width = frame.shape[1]
    img_height = frame.shape[0]
    y1 = int(round((850 - img_height) / 2, 0))
    y2 = int(round((850 - img_height) / 2, 0)) + int(img_height)
    profile.set_global_img_infos(id, [img_width, img_height, y1, y2])

def areafun(xylist1, xylist2):
    xy_1_1 = [min(xylist1[0][0], xylist1[1][0]), min(xylist1[0][1], xylist1[1][1])]
    xy_1_2 = [max(xylist1[0][0], xylist1[1][0]), max(xylist1[0][1], xylist1[1][1])]
    xy_2_1 = [min(xylist2[0][0], xylist2[1][0]), min(xylist2[0][1], xylist2[1][1])]
    xy_2_2 = [max(xylist2[0][0], xylist2[1][0]), max(xylist2[0][1], xylist2[1][1])]
    min_x = max(xy_1_1[0], xy_2_1[0])
    min_y = max(xy_1_1[1], xy_2_1[1])
    max_x = min(xy_1_2[0], xy_2_2[0])
    max_y = min(xy_1_2[1], xy_2_2[1])
    if(min_x < max_x) and (min_y < max_y):
        s = (max_x - min_x) * (max_y - min_y)
    else:
        s = 0
    return s



def framedetectionfun():
    time.sleep(2)
    url = "http://localhost:9080"
    cmera_num = profile.get_global_camera_num()
    while (True):
        for id in range(cmera_num):
            frame = profile.get_global_frame_dets(id)
            frame = cv2.imencode('.jpg', frame)[1]
            frame = np.array(frame).tobytes()
            files = {'file': ('im.jpg', frame, 'image/jpeg', {'Expires': '0'})}
            r = requests.post(url, files=files)
            get_data = json.loads(r.text)
            profile.set_global_detect_datas(id, get_data)
            dataandtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            target_area = profile.get_global_detect_areas(id)
            pepole_num = {}
            data_change = profile.get_global_data_changes(id)
            for key, values in target_area.items():
                pepole_num[key] = 0
                if not data_change.has_key(key):
                    data_change[key] = []

            for i in range(len(get_data)):
                class_name_val = get_data[str(i)][0]
                if class_name_val == 'person':
                    bbox_val = get_data[str(i)][2]
                    x1 = int(bbox_val[0])
                    y1 = int(bbox_val[1])
                    x2 = int(bbox_val[2])
                    y2 = int(bbox_val[3])
                    for key, values in target_area.items():
                        in_var = False
                        # values.append([values[0][0], values[1][1]])
                        # values.append([values[1][0], values[0][1]])
                        #
                        # for v in range(len(values)):
                        #     if min(x1, x2) < values[v][0] and values[v][0] < max(x1, x2):
                        #         if min(y1, y2) < values[v][1] and values[v][1] < max(y1, y2):
                        area = areafun([[x1, y1],[x2, y2]], values)
                        if area > 0:
                            in_var = True
                        if in_var:
                            pepole_num[key] = pepole_num[key] + 1

            for key, values in pepole_num.items():
                data_change[key].append(values)

            profile.set_global_data_changes(id, copy.deepcopy(data_change))
            timenow = time.time()
            timeshow = profile.get_global_timeshows()
            if not timeshow.has_key(id):
                profile.set_global_timeshows(id, timenow)
            else:
                if (timenow - timeshow[id]) > 1.:
                    for key, values in data_change.items():

                        if len([x for x in range(len(data_change[key])) if data_change[key][x] == 0]) > (0.5 * len(data_change[key])):
                            info_string = 'Camera id: ' + str(id) + '---------' + 'Area id: ' + key + '---------' + 'Detecting Time: ' + dataandtime + '---------' + \
                                                            'Detail Info: There are ' + str(0) + ' people''!' + '---------' + 'Main: abnormal!'
                        else:
                            info_string = 'Camera id: ' + str(id) + '---------' + 'Area id: ' + key + '---------' + 'Detecting Time: ' + dataandtime + '---------' + \
                                                            'Detail Info: There are ' + str(int(round(sum(data_change[key]) / len(data_change[key])))) + ' people''!' + '---------' + 'Main:    normal!'
                        profile.set_global_message_log(info_string)

                    profile.set_global_timeshows(id, timenow)
                    profile.clear_global_data_changes(id)








