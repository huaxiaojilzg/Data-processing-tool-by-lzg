'''
every people data init to
train
    |-pet
    |-ct
folder
'''
import os

ROOT_DIR = "people2"
TRAIN_DIR = 'train_init_2'


CT_PATH = 'CT_enhancement_(-45~50)_interval=3'
PET_PATH = 'PET_enhancement_(-45~50)_interval=3'

people_dir_list = []
peolpe_dir_ct__list_path = []
peolpe_dir_pet_list_path = []

for dir in os.listdir(ROOT_DIR):

    if len(dir.split('Patient')) == 2:
        people_path = os.path.join(ROOT_DIR, dir)
        peolpe_dir_ct__list_path.append(os.path.join(people_path, CT_PATH))
        peolpe_dir_pet_list_path.append(os.path.join(people_path, PET_PATH))

save_train_init_path = os.path.join(ROOT_DIR, TRAIN_DIR)
save_train_init_ct__path = os.path.join(save_train_init_path, 'CT')
save_train_init_pet_path = os.path.join(save_train_init_path, 'PET')

if not os.path.exists(save_train_init_path):
    os.mkdir(save_train_init_path)
if not os.path.exists(save_train_init_ct__path):
    os.mkdir(save_train_init_ct__path)
if not os.path.exists(save_train_init_pet_path):
    os.mkdir(save_train_init_pet_path)

i=0
for ct_path, pet_path in zip(peolpe_dir_ct__list_path, peolpe_dir_pet_list_path):

    for ct, pet in zip(os.listdir(ct_path), os.listdir(pet_path)):

        ct_all_path = os.path.join(ct_path, ct)
        pet_all_path = os.path.join(pet_path, pet)

        if not os.path.exists(os.path.join(save_train_init_ct__path,str(i)+'_ct.png')):
            os.rename(ct_all_path, os.path.join(save_train_init_ct__path,str(i)+'_ct.png'))

        if not os.path.exists(os.path.join(save_train_init_pet_path,str(i)+'_pet.png')):
            os.rename(pet_all_path, os.path.join(save_train_init_pet_path,str(i)+'_pet.png'))
        i+=1

