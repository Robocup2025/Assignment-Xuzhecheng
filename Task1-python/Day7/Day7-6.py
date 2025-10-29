from pathlib import Path

def replace_python_with_class():
    base_path = Path(__file__).parent
    test_dir = base_path / "test"

    for file in test_dir.iterdir():
        if file.is_file():
            content = file.read_text()
            if "python" in content:
                content = content.replace("python", "class")
                file.write_text(content)

            if "python" in file.stem:
                new_name = file.stem.replace("python", "class") + file.suffix
                new_file = file.with_name(new_name)
                file.rename(new_file)

if __name__ == "__main__":
    replace_python_with_class()
