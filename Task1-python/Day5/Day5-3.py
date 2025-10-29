#使用os和random生成一个包含100000个1到100之间随机整数的data.txt文件
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'data.txt')

with open(data_path, 'w') as f:
    for _ in range(100000):
        f.write(str(random.randint(1, 100)) + '\n')