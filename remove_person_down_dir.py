'''
every people data remove to
train
    |-pet
    |-CT_removal
folder
'''
import os
import shutil

ROOT_DIR = "people1"
peolpe_dir_del_list_path = []

del_dir = [
    'CT_removal',
    'CT_enhancement_(-45~50)_interval=3',
    'PET_enhancement_(-45~50)_interval=3'

]

for dir in os.listdir(ROOT_DIR):

    if len(dir.split('-')) == 2:
        people_path = os.path.join(ROOT_DIR, dir)
        for der in del_dir:
            peolpe_dir_del_list_path.append(os.path.join(people_path, der))

print(peolpe_dir_del_list_path)

for rmd in peolpe_dir_del_list_path:
    if os.path.exists(rmd):
        shutil.rmtree(path=rmd)
