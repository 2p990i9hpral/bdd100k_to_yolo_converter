import json
import os
from tqdm import tqdm
import cv2


def classify_classes(c_name):
    vehicle = ["car", "truck", "bus", "train"]
    if c_name in vehicle:
        return 0
    else:
        return 1


def convert2yolo_roi(img_name, obj):

    obj_name = obj["category"]
    obj_class = classify_classes(obj_name)
    obj_roi = obj['box2d']

    img = cv2.imread(img_name)
    img_w, img_h = img.shape[1], img.shape[0]

    w = (obj_roi["x2"] - obj_roi["x1"])
    h = (obj_roi["y2"] - obj_roi["y1"])
    x = (obj_roi["x1"] + w/2)
    y = (obj_roi["y1"] + h/2)

    x, y, w, h = x/img_w, y/img_h, w/img_w, h/img_h

    return "{} {} {} {} {}\n".format(obj_class, x, y, w, h)


if __name__ == '__main__':
    imgPath = "./100k/train/"
    labelPath = "./labels/bdd100k_labels_images_train.json"

    with open(labelPath) as labelFile:
        lines = json.load(labelFile)

    counter = {"car": 0,    
               "truck": 0,
               "bus": 0,
               "train": 0,
               "person": 0,
               "rider": 0}

    for line in tqdm(lines):
        name = line['name']
        labels = line['labels']
        txtPath = (imgPath + name).replace("jpg", "txt")
        if not os.path.isfile(imgPath+name):
            continue
        with open(txtPath, "w")as file:
            for label in labels:
                category = label["category"]
                if category in counter.keys():
                    counter[category] += 1
                    file.write(convert2yolo_roi(imgPath+name, label))

    print("line_num : {}".format(len(lines)))
