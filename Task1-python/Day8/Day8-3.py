from pathlib import Path
import random
import string

current_dir = Path(__file__).parent
print(current_dir)
img_dir = current_dir / "img"
img_dir.mkdir(exist_ok=True)

filenames = set()
while len(filenames) < 100:
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    filename = f"{name}.png"
    filenames.add(filename)
print(filenames)

for filename in filenames:
    (img_dir / filename).touch()