import os
import shutil

DIRPATH = os.path.join(r"C:\Users\gabriel\Documents\development\datasets\flowers")
print(DIRPATH)

print(os.listdir(DIRPATH))
container_folder = os.listdir(DIRPATH)[0]

def create_training_folder():
    folder_name = "\\train"
    if not os.path.exists(DIRPATH + folder_name):
        os.mkdir(DIRPATH + folder_name)
    else:
        print("Folder already exists")

create_training_folder()

def move_to_train_folder():
    source_dir = DIRPATH + "\\flowers"
    target_dir = DIRPATH + "\\train"

    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

if not os.path.exists(DIRPATH + "\\train"):
    move_to_train_folder()
else:
    print("Train folder already exists")

def create_test_folder():
    L = os.listdir(DIRPATH + "\\train")
    print(L)
    if not os.path.exists(DIRPATH + "\\test"):
        os.mkdir(DIRPATH + "\\test")
        test_path = DIRPATH + "\\test"
        dir_train = DIRPATH + "\\train"
        for folder in L:
            os.mkdir(test_path + "\\" + folder)
            source_dir = DIRPATH + "\\train" + "\\" + folder
            target_dir = test_path + "\\" + folder

            size = len(os.listdir(DIRPATH + "\\train" + "\\" + folder))
            print("The size is: *****")
            print(size)
            print("And the percentage is:")
            print(int(size*0.20))
            pictures = os.listdir(DIRPATH + "\\train" + "\\" + folder)[:int(size*0.20)]
            for img in pictures:
                shutil.move(os.path.join(source_dir, img), target_dir)
    else:
        print("Test Folder exists")



create_test_folder()

