import os
import cv2

ROOT_DIR = 'peopleTest'
a, b, c = -45, 50, 3


# 旋转
def rotate(pic, i):
    rows, cols = pic.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), i, 1)
    return cv2.warpAffine(pic, M, (cols, rows))


# 平滑处理
def smooth_img(pic):
    pass


def main():
    ROOTDIR = ROOT_DIR
    for ROOT in os.listdir(ROOTDIR):

        # ROOT = '01Patient-CHEN RENMING'

        if ROOT == '.idea' or ROOT.split('.')[-1] == 'py':
            continue

        ROOT_NAME = ROOT.split('-')[-1]

        # a,b,c = -90,100,10


        new_ct_path = os.path.join(os.path.join(ROOTDIR, ROOT), 'CT_enhancement_({}~{})_interval={}'.format(a, b, c))
        new_pet_path = os.path.join(os.path.join(ROOTDIR, ROOT), 'PET_enhancement_({}~{})_interval={}'.format(a, b, c))

        if not os.path.exists(new_ct_path):
            os.mkdir(new_ct_path)

        if not os.path.exists(new_pet_path):
            os.mkdir(new_pet_path)

        CT_lists = os.listdir(os.path.join(os.path.join(ROOTDIR, ROOT), 'CT_removal'))
        PET_lists = os.listdir(os.path.join(os.path.join(ROOTDIR, ROOT), 'PET'))

        for ct_list, pet_list in zip(CT_lists, PET_lists):

            for i in range(a, b, c):
                ct_name = ct_list.split('.')[0]
                img_ct = cv2.imread(os.path.join(os.path.join(ROOTDIR, ROOT), os.path.join('CT_removal', ct_list)))
                img_ct_rotate = rotate(img_ct, i)
                if i <= 0:
                    cv2.imwrite(os.path.join(new_ct_path, ROOT_NAME + ct_name + '_rotate_1(' + str(i) + ').png'),
                                img_ct_rotate)
                else:
                    cv2.imwrite(os.path.join(new_ct_path, ROOT_NAME + ct_name + '_rotate_2(' + str(i) + ').png'),
                                img_ct_rotate)

                pet_name = pet_list.split('.')[0]
                img_pet = cv2.imread(os.path.join(os.path.join(ROOTDIR, ROOT), os.path.join('PET', pet_list)))
                img_pet_rotate = rotate(img_pet, i)
                if i <= 0:
                    cv2.imwrite(os.path.join(new_pet_path, ROOT_NAME + pet_name + '_rotate_1(' + str(i) + ').png'),
                                img_pet_rotate)
                else:
                    cv2.imwrite(os.path.join(new_pet_path, ROOT_NAME + pet_name + '_rotate_2(' + str(i) + ').png'),
                                img_pet_rotate)
        print(ROOT, '完成')


if __name__ == '__main__':
    main()
