import os
import time
def readtxt(name):
    while True:
        try:
            file_dir = os.listdir(os.chdir('C:/log'))
            while name not in file_dir:
                file_dir = os.listdir(os.chdir('C:/log'))
                print (111)
                time.sleep(3)
            with open(name, 'r') as f:
                a = f.read()
            os.remove('C:/log/'+name)
            return a
        except:
            continue
a = readtxt('qq.txt')
print (a)
    
