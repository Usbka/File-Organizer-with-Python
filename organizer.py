import os  #operating system module to interact with the file system
import shutil #module to perform high-level file operations like copying and moving files

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Invalid path!")
    exit()

file_types={
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"], 
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"],
    "Code": [".py", ".cpp", ".java"],
    "Archives": [".zip", ".rar"]
}

files=os.listdir(folder_path)

for file in files:
    file_path=os.path.join(folder_path, file)
    if os.path.isdir(file_path):
        continue
    _, ext = os.path.splitext(file)
    moved = False

    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            shutil.move(file_path, os.path.join(category_path, file))
            print(f"Moved {file} → {category}")
            moved = True
            break
    if not moved:
        others_path = os.path.join(folder_path, "Others")

        if not os.path.exists(others_path):
            os.makedirs(others_path)

        shutil.move(file_path, os.path.join(others_path, file))
        print(f"Moved {file} → Others")
        print(f"File: {file}, Extension: {ext}")