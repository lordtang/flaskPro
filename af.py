import os
import time


def readtxt(name):
    while True:
        try:
            file_dir = os.listdir(os.chdir('C:/log'))
            while name not in file_dir:
                file_dir = os.listdir(os.chdir('C:/log'))
                print(111)
                time.sleep(3)
            with open(name, 'r') as f:
                a = f.read().strip()  # 去掉文本中的换行和空格
            if a.endswith('#LingDing@Finish'):  # 完整性判断
                os.remove('C:/log/' + name)
                return a.strip('#LingDing@Finish')  # 去掉截止符号
            else:
                continue
        except:
            continue


a = readtxt('qq.txt')
print(a)
