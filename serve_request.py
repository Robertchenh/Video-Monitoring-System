import numpy as np
import cv2
import profile
from profile import def_val
import time
import requests
import json
import copy


def chang_size(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    image_scale = 850. / img_width
    if (image_scale * img_height) > 850.:
        image_scale = 850. / img_height
    img = cv2.resize(img, (int(round(img_width * image_scale, 0)), int(round(img_height * image_scale, 0))), interpolation=cv2.INTER_CUBIC)
    return img, image_scale


def draw_area(frame):
    detect_area = profile.get_global_detect_area()
    temvar = profile.get_global_temvar()
    if len(detect_area) > 0:
        # print(detect_area)
        for key, values in detect_area.items():
            # pts = np.array(values, np.int32).reshape((-1, 1, 2))
            # frame = cv2.polylines(frame, [pts], True, def_val.area_color)
            frame = cv2.rectangle(frame, (values[0][0], values[0][1]), (values[1][0], values[1][1]), def_val.area_color, 2)
            xy = np.mean(np.array(values), axis=0)
            cv2.putText(frame, key , (int(xy[0]), int(xy[1])), cv2.QT_FONT_NORMAL, 0.5, (0, 0, 255), 1)

    if len(temvar) > 1:
        # mousexy = profile.get_global_mouse_xy()
        # distance = np.sqrt(np.square(mousexy[0] - temvar[0][0]) + np.square(mousexy[1] - temvar[0][1]))
        # if distance > 10:
        #     cv2.circle(frame, (temvar[0][0], temvar[0][1]), 10, def_val.circle_color0, 1)
        # else:
        #     time1 = time.time()
        #     # print(time1)
        #     if (time1 % 1) < 0.25:
        #         cv2.circle(frame, (temvar[0][0], temvar[0][1]), 10,def_val.circle_color0, 1)
        #     elif (time1 % 1) > 0.25 and (time1 % 1) < 0.5:
        #         cv2.circle(frame, (temvar[0][0], temvar[0][1]), 10, def_val.circle_color1, 1)
        #     elif (time1 % 1) > 0.5 and (time1 % 1) < 0.75:
        #         cv2.circle(frame, (temvar[0][0], temvar[0][1]), 10, def_val.circle_color0, 1)
        #     else:
        #         cv2.circle(frame, (temvar[0][0], temvar[0][1]), 10, def_val.circle_color1, 1)
        # if len(temvar) > 1:
        #     for i in range(len(temvar) - 1):
        #         cv2.line(frame, tuple(temvar[i]), tuple(temvar[i + 1]), def_val.line_color, 1)
        #     if profile.get_global_add_area():
        #         cv2.line(frame, tuple(temvar[0]), tuple(temvar[-1]), def_val.line_color, 1)

        values =profile.get_global_temvar()

        frame = cv2.rectangle(frame, (values[0][0], values[0][1]), (values[1][0], values[1][1]), def_val.area_color, 1)

    return frame


def draw_detectdata(frame):
    frame = frame
    get_data = profile.get_global_detect_data()

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

def draw_mouse():
    frame = profile.get_global_frame()
    xy = profile.get_global_mouse_xy()
    img_info = profile.get_global_img_info()
    if 0 < xy[1] and xy[1] < img_info[1]:
        cv2.line(frame, (xy[0] - 20, xy[1]), (xy[0] + 20, xy[1]), (0, 255, 0), 1)
        cv2.line(frame, (xy[0], xy[1] - 20), (xy[0], xy[1] + 20), (0, 255, 0), 1)


def set_img_info(frame):
    frame, img_scale = chang_size(frame)
    img_width = frame.shape[1]
    img_height = frame.shape[0]
    y1 = int(round((850 - img_height) / 2, 0))
    y2 = int(round((850 - img_height) / 2, 0)) + int(img_height)
    profile.set_global_img_info(img_width, img_height, y1, y2)



def framedetectionfun():
    time.sleep(1)
    url = "http://localhost:9080"

    while (True):
        frame = profile.get_global_frame_det()
        frame = cv2.imencode('.jpg', frame)[1]
        frame = np.array(frame).tobytes()
        files = {'file': ('im.jpg', frame, 'image/jpeg', {'Expires': '0'})}
        r = requests.post(url, files=files)
        get_data = json.loads(r.text)
        profile.set_global_detect_data(get_data)
        dataandtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        target_area = profile.get_global_detect_area()
        pepole_num = {}
        data_change = profile.get_global_data_change()
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
                    # print key, values
                    in_var = False
                    # if not pepole_num.has_key(key):
                    #     pepole_num[key] = 0
                    for v in range(len(values)):
                        if min(x1, x2) < values[v][0] and values[v][0] < max(x1, x2):
                            if min(y1, y2) < values[v][1] and values[v][1] < max(y1, y2):
                                in_var = True
                    if in_var:
                        pepole_num[key] = pepole_num[key] + 1

        # for key, values in target_area.items():
        #
        #     if pepole_num[key] == 0:
        #         info_string = '        Area id: ' + key + '-------------' + 'Detecting Time: ' + dataandtime + '-------------' +\
        #                       'Detail Info: There are ' + str(pepole_num[key]) + ' people''!' + '-------------' + 'Main: abnormal!                                        '
        #     else:
        #         info_string = '        Area id: ' + key + '-------------' + 'Detecting Time: ' + dataandtime + '-------------' + \
        #                       'Detail Info: There are ' + str(pepole_num[key]) + ' people''!' + '-------------' + 'Main:    normal!                                        '
        #     profile.set_global_message_log(info_string)
            # print  profile.get_global_message_log()
        # print(data_change)
        for key, values in pepole_num.items():

            data_change[key].append(values)
        # profile.clear_global_data_change()
        profile.set_global_data_change(copy.deepcopy(data_change))
        # print('++++++++++++')
        # print(profile.get_global_data_change())

        timenow = time.time()
        timeshow = profile.get_global_timeshow()
        if timeshow == 0.01:
            profile.set_global_timeshow(timenow)
        if (timenow - timeshow) > 1.:
            for key, values in data_change.items():

                if len([x for x in range(len(data_change[key])) if data_change[key][x] == 0]) > (0.5 * len(data_change[key])):
                    info_string = '        Area id: ' + key + '-------------' + 'Detecting Time: ' + dataandtime + '-------------' + \
                                                    'Detail Info: There are ' + str(0) + ' people''!' + '-------------' + 'Main: abnormal!                                        '
                else:
                    info_string = '        Area id: ' + key + '-------------' + 'Detecting Time: ' + dataandtime + '-------------' + \
                                                    'Detail Info: There are ' + str(int(round(sum(data_change[key]) / len(data_change[key])))) + ' people''!' + '-------------' + 'Main:    normal!                                        '
                profile.set_global_message_log(info_string)

            profile.set_global_timeshow(timenow)
            profile.clear_global_data_change()








