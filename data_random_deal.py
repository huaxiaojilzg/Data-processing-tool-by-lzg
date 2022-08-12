import os
import cv2
import random


# 翻转
def filp(pic, i=1):
    '''
    i=1:水平翻转
    i=0:垂直翻转
    i=-1:中心翻转
    '''
    return cv2.flip(pic, 1)


# 15度旋转
def rotate(pic, i):
    rows, cols = pic.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), i, 1)
    return cv2.warpAffine(pic, M, (cols, rows))


if __name__ == "__main__":
    ct_path = 'CT'
    pet_path = 'PET'

    save_ct_path = ct_path + "_finish"
    save_pet_path = pet_path + "_finish"

    if not os.path.exists(save_ct_path):
        os.mkdir(save_ct_path)
    if not os.path.exists(save_pet_path):
        os.mkdir(save_pet_path)

    ct_lists = os.listdir(ct_path)
    pet_lists = os.listdir(pet_path)

    i = 0
    for ct, pet in zip(ct_lists, pet_lists):
        # 对图片进行翻转旋转
        # random_deal_num = random.randint(-1, 1)
        random_deal_num = 1
        random_rot_num = random.randint(-15, 15)

        ct_name = ct.split('.')[0]
        img_ct = cv2.imread(os.path.join(ct_path, ct))
        img_ct_rot = rotate(img_ct, random_rot_num)
        cv2.imwrite(os.path.join(save_ct_path, ct_name + "_rot_" + str(random_rot_num) + '.png'), img_ct_rot)
        img_ct_silp = filp(img_ct, random_deal_num)
        cv2.imwrite(os.path.join(save_ct_path, ct_name + "_filp_and_rot_" + str(random_deal_num) + '.png'), img_ct_silp)
        print(ct_name, "ct旋转完成")

        pet_name = pet.split('.')[0]
        img_pet = cv2.imread(os.path.join(pet_path, pet))
        img_pet_rot = rotate(img_pet, random_rot_num)
        cv2.imwrite(os.path.join(save_pet_path, pet_name + "_rot_" + str(random_rot_num) + '.png'), img_pet_rot)
        img_pet_silp = filp(img_pet, random_deal_num)
        cv2.imwrite(os.path.join(save_pet_path, pet_name + "_filp_and_rot_" + str(random_deal_num) + '.png'),
                    img_pet_silp)
        print(pet_name, "pet旋转完成")

        # print(i, ct, pet)
        i += 1
