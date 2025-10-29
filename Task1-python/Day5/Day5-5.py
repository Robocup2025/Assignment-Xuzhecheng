from pathlib import Path
import random

img_dir=Path(__file__).parent / "img"
print(img_dir)

png_files=list(img_dir.glob("*.png"))
#print(png_files)

selected=random.sample(png_files, k=50)
for file_path in selected:
    new_name=file_path.stem+".jpg"
    new_path=file_path.with_name(new_name)
    file_path.rename(new_path)