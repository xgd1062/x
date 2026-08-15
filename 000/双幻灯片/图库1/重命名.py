import os

def rename_images():
    # 支持的图片格式
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    
    # 获取当前目录下所有的图片文件
    files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    # 按照文件名进行排序，确保重命名顺序有迹可循
    files.sort()

    if not files:
        print("当前文件夹下未发现图片文件。")
        return

    # 第一步：先重命名为临时名称（防止 1.jpg 重命名为 2.jpg 时发生文件冲突）
    temp_files = []
    for idx, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        old_path = filename
        temp_name = f"__temp_{idx}{ext}"
        os.rename(old_path, temp_name)
        temp_files.append(temp_name)

    # 第二步：正式重命名为 1.jpg, 2.jpg ... (统一转为 jpg 方便网页调用)
    for idx, temp_name in enumerate(temp_files):
        new_name = f"{idx + 1}.jpg"
        
        # 如果已存在同名文件（虽然理论上已temp化，但做保险处理）
        if os.path.exists(new_name):
            os.remove(new_name)
            
        os.rename(temp_name, new_name)

    print(f"重命名完成，共处理 {len(files)} 张图片。")

if __name__ == "__main__":
    rename_images()