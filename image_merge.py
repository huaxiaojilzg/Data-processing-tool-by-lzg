import os
import numpy as np
import cv2

ROOT_DIR = 'peopleTest'
OBJ_DIR = 'train_init_2'

new_path = os.path.join(ROOT_DIR, OBJ_DIR + '_merge')
imA = os.path.join(ROOT_DIR, OBJ_DIR, 'CT')  # ct
imB = os.path.join(ROOT_DIR, OBJ_DIR, 'PET')  # pet

# 超参数


if not os.path.exists(new_path):
    os.mkdir(new_path)

ct_list = os.listdir(imA)
pet_list = os.listdir(imB)

i = 0
for ct, pet in zip(ct_list, pet_list):
    print(ct, pet)
    img1 = cv2.imread(imA + '/' + ct)
    img2 = cv2.imread(imB + '/' + pet)
    image = np.concatenate([img1, img2], axis=1)
    #
    cv2.imwrite(new_path + '/img_' + str(i) + '.png', image)
    i += 1
