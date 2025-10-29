from pathlib import Path
def compare_files(file1,file2):
    base_path = Path(__file__).parent
    file1_path = base_path / file1
    file2_path = base_path / file2
    lines1 = file1_path.read_text().splitlines()
    lines2 = file2_path.read_text().splitlines()
    min_len = min(len(lines1),len(lines2))
    diff_lines = []
    for i in range(min_len):
        if lines1[i] != lines2[i]:
            diff_lines.append(i+1)
    if len(lines1)!=len(lines2):
        diff_lines.extend(range(min_len+1,max(len(lines1),len(lines2))+1))
    if diff_lines:
        print("不同的行编号为：",diff_lines)
    else:
        print("两个文件的内容完全相同。")

if __name__ == "__main__":
    file1 = "test.txt"
    file2 = "copy_test.txt"
    compare_files(file1,file2)
