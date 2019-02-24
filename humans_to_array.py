import pandas as pd
import numpy as np

from tf_pose import common
from tf_pose.common import CocoPart

def humans_to_csv(humans):
    for human in humans:
        # draw point
        array_humans = []

        for i in range(common.CocoPart.Background.value):
            array_humans.append([human.body_parts[i].x, human.body_parts[i].y, human.body_parts[i].score])
            body_part = human.body_parts[i]
            # center = (int(body_part.x * image_w + 0.5), int(body_part.y * image_h + 0.5))
            # centers[i] = center
            # cv2.circle(npimg, center, 3, common.CocoColors[i], thickness=3, lineType=8, shift=0)

    return npimg

    #     Nose = 0
#     Neck = 1
#     RShoulder = 2
#     RElbow = 3
#     RWrist = 4
#     LShoulder = 5
#     LElbow = 6
#     LWrist = 7
#     RHip = 8
#     RKnee = 9
#     RAnkle = 10
#     LHip = 11
#     LKnee = 12
#     LAnkle = 13
#     REye = 14
#     LEye = 15
#     REar = 16
#     LEar = 17
#     Background = 18