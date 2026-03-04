import os
from pathlib import Path
import json
import shutil

save_data = "folder_name.json"

if os.path.exists(save_data):
    with open(save_data) as f:
        data = json.load(f)
else:
    data = {}

def move_file(file):
    if file.suffix not in data :
        folder_name = input(f"Enter the folder name for {file.suffix} extension : ")
        data[file.suffix] = folder_name
    os.makedirs(data[file.suffix], exist_ok=True)
    destination = cwd_path / data[file.suffix]
    #print(f"Moving {file.name} → {data[file.suffix]}/")
    shutil.move(file, f"{destination}/{file.name}")

cwd_path = Path(os.path.dirname(os.path.abspath(__file__)))

for i in cwd_path.iterdir():
    if (
        not i.is_file()
        or i.name.startswith(".")
        or i.suffix == ""
        or i.name in ["main.py", "folder_name.json"]
    ):
        continue

    move_file(i)

print("ORGANIZED SUCCESSFULLY !!!")
with open(save_data, 'w') as f:
    json.dump(data, f)