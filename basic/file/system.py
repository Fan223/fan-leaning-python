import os
import os.path as path

# os.system('notepad.exe')  # 打开记事本
# os.system('calc.exe')  # 打开计算器

print(os.getcwd())

l1 = os.listdir('../file')
print(l1)

print(path.abspath('system.py'))
print(path.exists('D:\\DevelopmentTools\\Project\\fan-leaning-python\\fan\\file\\system.py'))
print(path.splitext('system.py'))
print(path.basename('D:\\DevelopmentTools\\Project\\fan-leaning-python\\fan\\file\\system.py'))
print(path.dirname('.D:\\DevelopmentTools\\Project\\fan-leaning-python\\fan\\file\\system.py'))
print(path.isdir('D:\\DevelopmentTools\\Project\\fan-leaning-python\\fan\\file\\system.py'))
print(path.isdir('D:\\DevelopmentTools\\Project\\fan-leaning-python\\fan\\file'))
