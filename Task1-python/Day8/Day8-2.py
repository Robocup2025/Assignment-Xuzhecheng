#使用Day7-4.py封装新的函数
from pathlib import Path
from typing import List, Optional


def compare_files(
    file1: str,
    file2: str,
    max_lines: Optional[int] = None,
) -> List[int]:
    base_path: Path = Path(__file__).parent
    file1_path: Path = base_path / file1
    file2_path: Path = base_path / file2

    lines1: List[str] = file1_path.read_text().splitlines()
    lines2: List[str] = file2_path.read_text().splitlines()

    if max_lines is not None:
        lines1 = lines1[:max_lines]
        lines2 = lines2[:max_lines]

    min_len: int = min(len(lines1), len(lines2))
    diff_lines: List[int] = []

    for i in range(min_len):
        if lines1[i] != lines2[i]:
            diff_lines.append(i + 1)

    if len(lines1) != len(lines2):
        diff_lines.extend(range(min_len + 1, max(len(lines1), len(lines2)) + 1))

    return diff_lines

if __name__ == "__main__":
    file1 = "test.txt"
    file2 = "copy_test.txt"
    result=compare_files(file1,file2)
    print(f"不同的行号: {result}")