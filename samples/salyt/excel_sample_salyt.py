import os
import pandas as pd

path = "C:\meital\salyt\s"
files = os.listdir(path)

gr_frame = pd.DataFrame()
for idx,file_name in enumerate(files):
    full_path = os.path.join(path,file_name)
    data = pd.read_excel(full_path)
    gr_data = data.groupby(['name']).max()["T3"]
    print(type(gr_data))
    print(gr_data)
    #gr_frame = gr_data.to_frame()
    #print(type(gr_frame))
    #print(gr_frame)

    print(idx)
    col_name = data.at[0,'Case_id']
    #print(col_name)
    gr_data.name = col_name
    print(gr_data)
    #gr_frame.insert(idx+1,data.at[0,'Case_id'],gr_data.values)
    gr_frame = gr_frame.append(gr_data)
    print(gr_frame.T)
    #gr_frame = pd.concat([gr_frame,gr_data], axis=1, join='outer')

    gr_frame.to_excel("C:\meital\salyt\output.xlsx")