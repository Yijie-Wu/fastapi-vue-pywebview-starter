import os
import uuid
import shutil
from datetime import datetime


def split_list(input_list, n):
    # 使用列表推导式和切片
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]


def rename_file(old_filename):
    ext = os.path.splitext(old_filename)[1]
    new_filename = uuid.uuid4().hex + '-' + str(int(datetime.utcnow().timestamp())) + ext
    return new_filename


def delete_file(filename):
    try:
        os.remove(filename)
        return True, '文件已删除'
    except FileNotFoundError:
        return False, '文件不存在'


def remove_folder(folder):
    shutil.rmtree(folder)
    return True, '文件夹已删除'
