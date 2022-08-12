import os
import argparse
import cv2
import sys

# y=96
# x=152
ROOT_DIR = 'peopleTest'


def dfs(x, y, img_numpy, list_xy):
    max_x, max_y, _ = img_numpy.shape
    if img_numpy[x][y][0] < 10 or img_numpy[x][y][1] < 10 or img_numpy[x][y][
        2] < 10 or x < 5 or y < 5 or x >= max_x - 5 or y >= max_y - 5:
        return
    t = 5
    list_xy.append([x, y])
    list_xy.append([x + t, y])
    list_xy.append([x, y + t])
    list_xy.append([x - t, y])
    list_xy.append([x, y - t])
    list_xy.append([x + t, y + t])
    list_xy.append([x + t, y - t])
    list_xy.append([x - t, y + t])
    list_xy.append([x - t, y - t])
    img_numpy[x][y][0] = 0
    img_numpy[x][y][1] = 0
    img_numpy[x][y][2] = 0
    dfs(x - 1, y, img_numpy, list_xy)
    dfs(x + 1, y, img_numpy, list_xy)
    # dfs(x - 1, y - 1, img_numpy)
    # dfs(x + 1, y + 1, img_numpy)
    dfs(x, y - 1, img_numpy, list_xy)
    dfs(x, y + 1, img_numpy, list_xy)
    # dfs(x + 1, y - 1, img_numpy)
    # dfs(x - 1, y + 1, img_numpy)

    return img_numpy


def find_down_xy(ct_numpy):
    center_x, _, _ = ct_numpy.shape
    center_y = center_x / 2
    center_x -= 10

    # center_x = 190
    # center_y = 96

    center_x = int(center_x)
    center_y = int(center_y)

    while ((ct_numpy[center_x][center_y - 1][0]) < 150):

        if center_x <= 1:
            break

        center_x -= 1

    return center_y, center_x


def main():
    mainPath = ROOT_DIR
    people_root_dir_list = os.listdir(mainPath)

    deal_with_ct_dir_list = []

    for people_root_dir in people_root_dir_list:
        deal_with_ct_dir_list.append(os.path.join(mainPath, os.path.join(people_root_dir), 'CT'))
        if not os.path.exists(os.path.join(os.path.join(mainPath, people_root_dir), 'CT_removal')):
            os.mkdir(os.path.join(os.path.join(mainPath, people_root_dir), 'CT_removal'))

    # print(deal_with_ct_dir_list)

    for people_ct_dir in deal_with_ct_dir_list:
        PPC_path = people_ct_dir
        # print(PPC_path)

        people_ct_img_list = os.listdir(PPC_path)
        # print(people_ct_img_list)
        target_ct_img_to_xy_path1 = os.path.join(PPC_path, people_ct_img_list[0])
        target_ct_img_to_xy_path2 = os.path.join(PPC_path, people_ct_img_list[46])
        target_ct_img_to_xy_path3 = os.path.join(PPC_path, people_ct_img_list[12])
        # print(target_ct_img_to_xy_path)
        ct_numpy_tar1 = cv2.imread(target_ct_img_to_xy_path1)
        ct_numpy_tar2 = cv2.imread(target_ct_img_to_xy_path2)
        ct_numpy_tar3 = cv2.imread(target_ct_img_to_xy_path3)
        xx1, yy1 = find_down_xy(ct_numpy_tar1)
        xx2, yy2 = find_down_xy(ct_numpy_tar2)
        xx3, yy3 = find_down_xy(ct_numpy_tar3)

        print(xx1, yy1)
        removal_ct_xy_list = []
        dfs(yy1, xx1, ct_numpy_tar1, removal_ct_xy_list)
        dfs(yy2, xx2, ct_numpy_tar2, removal_ct_xy_list)
        dfs(yy3, xx3, ct_numpy_tar3, removal_ct_xy_list)
        # print(removal_ct_xy_list)

        i = 0
        for people_ct_img in people_ct_img_list:
            ct_numpy = cv2.imread(os.path.join(PPC_path, people_ct_img))
            new_ct_name = people_ct_img.split('.')[0]
            for ls in removal_ct_xy_list:
                print(ls[0], ls[1])
                xx = int(ls[0])
                yy = int(ls[1])

                ct_numpy[xx][yy][0], ct_numpy[xx][yy][1], ct_numpy[xx][yy][2] = 0, 0, 0
            cv2.imwrite(os.path.join(
                os.path.join(mainPath, people_ct_dir.split('\\')[1], 'CT_removal')) + '/' + new_ct_name + '.png',
                        ct_numpy)
            i += 1


if __name__ == '__main__':
    main()
