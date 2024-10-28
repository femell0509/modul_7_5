import os
import time


directori = os.getcwd()
print(f'{directori}\n')

for root, dirs, files in os.walk(directori):
    for file in files:
        filepath = os.path.join(root, file)
        filtime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filtime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
