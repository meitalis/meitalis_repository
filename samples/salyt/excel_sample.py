import os
import pandas as pd
import csv
from xlsxwriter.workbook import Workbook
from pathlib import Path
from time import gmtime, strftime


def scan_all_files(dirs_info):

    files_info = {}
    path = input("enter path to scan. press . to current dir\n>>>")
    if path == '.':
        path = os.getcwd()

    for dirpath, dirnames, files in os.walk(path,followlinks=True):
        for file_name in files:
            full_path = os.path.join(dirpath, file_name)
            file_size = os.path.getsize(full_path)

            if full_path not in files_info:
                files_info[full_path] = file_size

    print("*" * 45,f"[{files_info.__len__()}] files info" , "*" * 44 )

    df_full = pd.DataFrame()
    count = 0
    for full_path, file_size in files_info.items():
        print("file name",full_path,"size",file_size)

        df = pd.read_excel(full_path,index_col=False,header=None)
        writer = pd.ExcelWriter(full_path, engine='xlsxwriter')

        print(df)

        df2 = df.groupby(df.columns[0], sort=False)[df.columns[1]].max()
        print(df2)
        print(type(df2))

        df.to_excel(writer, header=None,index=False,sheet_name='x1')
        df2.to_excel(writer, header=None,sheet_name='x2')

        df_full.append(df2)


        writer.save()
        writer.close()

    writer2 = pd.ExcelWriter("C:\meital\salyt\stemp.xlsx", engine='xlsxwriter')
    df_full.to_excel(writer2, header=None, sheet_name='x3')
    writer2.save()
    writer2.close()

def exit_cli(duplicate,dirs_info):
    print("exit_cli")
    exit()

#   C:\meital\salyt
if __name__== '__main__':

    dirs = os.listdir("C:\meital\salyt")
    # print(dirs)
    # print(type(dirs))
    for idx,file_name in enumerate(dirs):
        print(file_name)
    dirs_info = {}

    commands = {
        'sc': scan_all_files
    }

    cmd = -1
    while cmd != 0:
        commands.get("sc",exit_cli)(dirs_info)
