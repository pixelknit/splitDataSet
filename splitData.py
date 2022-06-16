import os
import shutil
from tqdm import tqdm
#from tkinter import *
#from tkinter import ttk
#from tkinter import fileDialog

DIRPATH = r"/Users/felipepesantez/Documents/development/ML/datasets/flowers"
print(DIRPATH)

print(os.listdir(DIRPATH))

TRAINPATH = os.path.join(DIRPATH,"train")
TESTPATH = os.path.join(DIRPATH,"test")

print(TRAINPATH, TESTPATH)

container_folder = os.listdir(DIRPATH)[0]

def create_training_folder():
    if not os.path.exists(TRAINPATH):
        os.mkdir(os.path.join(TRAINPATH))
    else:
        print("Folder already exists")

create_training_folder()

def move_to_train_folder():
    source_dir = os.path.join(DIRPATH,"flowers")
    target_dir = TRAINPATH

    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

move_to_train_folder()

def create_test_folder():
    L = os.listdir(TRAINPATH)
    print(L)
    if not os.path.exists(TESTPATH):
        os.mkdir(TESTPATH)
        test_path = TESTPATH 
        for folder in L:
            if folder == ".DS_Store":
                continue
            os.mkdir(os.path.join(test_path, folder))
            source_dir = os.path.join(TRAINPATH, folder)
            target_dir = os.path.join(test_path, folder)

            size = len(os.listdir(os.path.join(TRAINPATH, folder)))
            print("The size is: *****")
            print(size)
            print("And the percentage is:")
            print(int(size*0.20))
            pictures = os.listdir(os.path.join(TRAINPATH, folder))[:int(size*0.20)]
            for img in tqdm(pictures):
                if img == ".DS_Store":
                    continue
                shutil.move(os.path.join(source_dir, img), target_dir)
    else:
        print("Test Folder exists")



create_test_folder()
