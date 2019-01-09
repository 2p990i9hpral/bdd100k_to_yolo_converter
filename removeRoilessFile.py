# -*- coding:utf-8 -*-
import os
import shutil


def returnFileList(dirname, extract):
    fileList = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        ext = os.path.splitext(filename)[-1]
        if ext == extract:
            fileList.append(filename)
    return fileList


if __name__ == '__main__':
    path = "./100k/train/"
    dest = "./100k/roiLess/"
    jpgName = returnFileList(path, ".jpg")
    txtName = returnFileList(path, ".txt")

    jpgName = [jpg.replace("jpg", "txt") for jpg in jpgName]
    roiLessFile = set(jpgName) - set(txtName)

    for file in roiLessFile:
        os.remove(path + file.replace("txt", "jpg"))
