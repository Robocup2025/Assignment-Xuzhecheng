from pathlib import Path
def addstr(file_path):
    with open(file_path,'r+',encoding='utf-8') as f:
        content = f.read()
        f.seek(0,0)
        f.write('python\n' + content)
        f.seek(0,2)
        f.write('python\n')
    return file_path

if __name__ == "__main__":
    filename = 'test.txt'
    base_path = Path(__file__).parent
    file_path = base_path / filename
    addstr(file_path)