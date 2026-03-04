import os
from pathlib import PurePath
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
    with open(save_data, 'w') as f:
        json.dump(data, f)
    os.makedirs(data[file.suffix], exist_ok=True)
    destination = os.path.dirname(os.path.abspath(__file__)) + f"/{data[file.suffix]}"
    print(file)
    shutil.move(file, f"{destination}/{file.name}")

print(data)
cwd_path = Path(os.path.dirname(os.path.abspath(__file__)))
#file = os.path.dirname(os.path.abspath(__file__)) + '/File'

for i in cwd_path.iterdir():
    if i.is_file():
        if i.name == 'folder_name.json':
            continue
        if i.name == 'main.py':
            continue
        print(i.suffix)
        move_file(i)


with open(save_data, 'w') as f:
    json.dump(data, f)

