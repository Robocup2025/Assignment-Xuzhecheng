import random
import string
from pathlib import Path

def filegenerate(filename,rows):
    base_path = Path(__file__).parent
    file_path = base_path / filename
    with open (file_path,'w',encoding='utf-8') as f:
        for _ in range(rows):
            row=''.join(random.choice(string.printable[:-6]) for _ in range(20))
            f.write(row+'\n')
    return file_path

#文件复制
def copy_file(file1, file2):
    base_path = Path(__file__).parent
    file1_path = base_path / file1
    file2_path = base_path / file2
    with open(file1_path,'r',encoding='utf-8') as f1, open(file2_path,'w',encoding='utf-8') as f2:
        for line in f1:
            f2.write(line)
    return file2_path

if __name__ == "__main__":
    filename = "test.txt"
    copy_filename = "copy_test.txt"
    rows = int(input())
    file_path = filegenerate(filename, rows)
    copy_path = copy_file(filename, copy_filename)
