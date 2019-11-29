import os
import hashlib
import csv
from pathlib import Path
from time import gmtime, strftime

def file_as_bytes(full_path):
    with open(full_path,'rb') as file:
        return file.read()


def scan_all_files(duplicate,dirs_info):

    files_info = {}
    path = input("enter path to scan. press . to current dir\n>>>")
    if path == '.':
        path = os.getcwd()

    for dirpath, dirnames, files in os.walk(path,followlinks=True):
        for file_name in files:
            full_path = os.path.join(dirpath, file_name)
            file_size = os.path.getsize(full_path)
            file_hash = hashlib.md5(file_as_bytes(full_path)).hexdigest()

            if file_hash in files_info:
                if file_hash in duplicate:
                    duplicate[file_hash][2] += 1
                else:
                    duplicate[file_hash] = [file_name, file_size, 2]
            else:
                files_info[file_hash] = (full_path, file_size)

        for dir_name in dirnames:
            dir_full_path = Path(os.path.join(dirpath, dir_name))
            dir_size = sum(f.stat().st_size for f in dir_full_path.rglob('*/') if f.is_file() )

            dirs_info[dir_full_path] = dir_size

    print("*" * 45 , " SCAN RESULTS" , "*" * 45 )
    print("*" * 45,f"[{files_info.__len__()}] files info" , "*" * 44 )
    for key, value in files_info.items():
        print("hash",key,"value",value)

    print("*" * 43, f"[{duplicate.__len__()}] duplicate files", "*" * 42)
    for key, value in duplicate.items():
        print("hash", key, "value", value)

def output_duplicate_files(duplicate,dirs_info):
    if len(duplicate) == 0:
        print("no duplicate files. scan again to be sure")
        scan_all_files(duplicate,dirs_info)

    output_file_name = 'output_' + strftime("%Y%m%d%H%M%S", gmtime()) + ".csv"
    with open(output_file_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["file name","file size","copies"])
        for key, value in duplicate.items():
            writer.writerow([value[0],value[1],value[2]])
        print("*" * 45,f"file {output_file_name} saved successfully", "*" * 45)


def output_tree_view(cmd,dirs_info):
    if len(dirs_info) == 0:
        print("no dirs to show. scan again to be sure")
        scan_all_files(duplicate,dirs_info)

    depth = 3
    #check of level to show
    index = cmd.rfind(":")
    if index != -1:
        depth = int(cmd[index+1])

    print("*" * 45, " OUTPUT TREE VIEW", "*" * 45)
    for i , key in enumerate(dirs_info):
        if i == depth:
            break
        print("directory:", key, "size:", dirs_info[key])


def exit_cli(duplicate,dirs_info):
    print("exit_cli")
    exit()


if __name__== '__main__':
    duplicate = {}
    dirs_info = {}

    commands = {
        'sc': scan_all_files,
        'du': output_duplicate_files
    }

    cmd = -1
    while cmd != 0:
        cmd = input("*" * 90 + "\n" +
                    "sc - Scans all files in <path> and below. Searches for duplicate file, and sizes\n"
                    "du - Output duplicate files to a new csv file\n"
                    "ds:level - Output a tree-view of directory sizes, up to depth levels\n"
                    + ">" * 3 + "\n"
                    )

        if cmd.startswith('ds'):
            output_tree_view(cmd,dirs_info)
        else:
            commands.get(cmd.lower(),exit_cli)(duplicate,dirs_info)
