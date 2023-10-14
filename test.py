import os
import shutil


def rename_images(folder_path, tar_path, last_num):
    # 获取文件夹下所有文件的列表
    files = os.listdir(folder_path)
    # 遍历文件列表
    for file in files:

        new_name = str(last_num + extract_numbers_from_string(file)+1) +'.png'

        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(tar_path, new_name)

        # 使用shutil模块重命名文件
        shutil.copyfile(file_path, new_file_path)

#提取图片名中的数字
def extract_numbers_from_string(string):
    numbers = ''
    for char in string:
        if char.isdigit():
            numbers += char
    return int(numbers)

# 调用函数进行重命名
Spot_root = '../data/SPOT/131/5/'
Spot_root_target = '../data/SPOT/131/All/'
if os.path.exists(Spot_root_target):
    shutil.rmtree(Spot_root_target)
os.mkdir(Spot_root_target)

rename_images(Spot_root,Spot_root_target,350)