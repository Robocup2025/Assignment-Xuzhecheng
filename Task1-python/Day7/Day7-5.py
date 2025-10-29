from pathlib import Path
import random
import string

def create_files_and_modify(i, j):
    base_path = Path(__file__).parent
    test_dir = base_path / "test1"
    test_dir.mkdir(exist_ok=True)

    for n in range(1, i + 1):
        file_path = test_dir / f"file{n}.txt"
        with open(file_path, "w") as f:
            for _ in range(j):
                line = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                f.write(line + "\n")

    for file in test_dir.iterdir():
        if file.is_file():
            lines = file.read_text().splitlines()
            new_lines = [line + "-pythonver1" for line in lines]
            new_name = file.stem + "-pythonver1" + file.suffix
            new_file = file.with_name(new_name)
            new_file.write_text('\n'.join(new_lines))

if __name__ == "__main__":
    i = int(input())
    j = int(input())
    create_files_and_modify(i, j)
