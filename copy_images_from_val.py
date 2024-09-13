import os
import shutil

# 相对路径
val_file = 'data_mouse_labels/val.txt'  # val.txt 文件的相对路径
images_dir = 'data_mouse_labels/images'  # 图片文件夹的相对路径
target_dir = 'detecttest'  # 目标文件夹的相对路径

# 确保目标文件夹存在
os.makedirs(target_dir, exist_ok=True)

# 读取 val.txt 文件
with open(val_file, 'r') as file:
    lines = file.readlines()

# 处理 val.txt 中的每一行
for line in lines:
    # 获取图片文件的名称，移除多余的空格和换行符
    image_name = os.path.basename(line.strip())

    # 构建完整的图片路径
    full_image_path = os.path.join(images_dir, image_name)

    # 检查图片是否存在于源目录中
    if os.path.exists(full_image_path):
        # 复制图片到目标文件夹
        shutil.copy(full_image_path, target_dir)
        print(f"Copied: {full_image_path} to {target_dir}")
    else:
        print(f"Image not found: {full_image_path}")
