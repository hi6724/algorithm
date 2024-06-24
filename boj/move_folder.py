# data.json와 다운받은 소스코드들 같은 폴더로 이동 후 실행
import os
import json
import shutil

def rename_and_move_files(file_info):
    for data in file_info:
        tier_folder = f"{data['tier']}"
        if not os.path.exists(tier_folder):
            os.makedirs(tier_folder)

    id_to_problem_id = {item["id"]: item["problemId"] for item in file_info}

    for data in file_info:
        file_id = data['id']
        file = data['file_name']
        tier_folder = f"{data['tier']}"

        if file_id in id_to_problem_id:
            ex = 'py'
            if data['language'] == 'Java 11':
                ex = 'java'
            elif data['language'] == 'node.js':
                ex = 'js'
            elif data['language'] == 'C++17':
                ex = 'cpp'

            base_new_name = f"{id_to_problem_id[file_id]}.{ex}"
            new_name = os.path.join(tier_folder, base_new_name)

            counter = 2
            while os.path.exists(new_name):
                new_name = os.path.join(tier_folder, f"{id_to_problem_id[file_id]}_{counter}.{ex}")
                counter += 1

            try:
                shutil.move(file, new_name)
                print(f"Renamed and moved {file} to {new_name}")
            except FileNotFoundError:
                print(f"Error: {file} not found.")
        else:
            print(f"No matching problemId found for {file}")


with open('data.json', 'r', encoding='utf-8') as f:
    file_info = json.load(f)

rename_and_move_files(file_info)

for tier in set(item['tier'] for item in file_info):
    tier_folder = f"{tier}"
    print(f"Contents of {tier_folder}: {os.listdir(tier_folder)}")
