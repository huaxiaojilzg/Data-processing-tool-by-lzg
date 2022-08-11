import os

dir_name = 'peopleTest'

for ROOT in os.listdir(dir_name):

    # ROOT = '01Patient-CHEN RENMING'

    ROOT = os.path.join(dir_name, ROOT)
    dirs = os.listdir(ROOT)

    for dir in dirs:

        print(dir)
        if dir == "Series-017":
            newdir1 = 'CT'
            os.renames(ROOT + '/' + dir, ROOT + '/' + newdir1)
        if dir == "Series-026":
            newdir2 = 'PET'
            os.renames(ROOT + '/' + dir, ROOT + '/' + newdir2)
