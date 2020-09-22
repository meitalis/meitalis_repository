import pandas as pd
import numpy as np

def load_data():
    data = {'component': [1,1,3,1,2,3,1,2,3,1,2,3,1,2,3],
            'status': [4,4,5,5,6,6,5,5,4,4,5,6,7,6,5],
            'values': [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 20, 30, 40, 50],
            'x': [40,40,50,50,60,60,50,50,40,40,50,60,70,60,50]
            }

    df = pd.DataFrame(data)
    df.set_index(['component', 'status'], inplace=True)
    #print(df)


    data_to_add = {'component': [1,1,3,1,2,3,1,2,3,1,2,3,1,2,3],
            'status': [4,4,5,5,6,6,5,5,4,4,5,6,7,6,5],
            'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3]}
    df_to_add = pd.DataFrame(data_to_add)
    df_to_add.set_index(['component', 'status'], inplace=True)

    # df_tmp = pd.concat([df, df_to_add], axis=1, join='outer')
    # df_tmp['values'] = df_tmp['values'] + df_tmp['values_2']
    # df_tmp.drop(['values_2'], axis=1,inplace=True)
    # print(df_tmp)

    df.add(df_to_add)
    print(df)


    # df_max = df.groupby(level=[0, 1])[['values', 'x']].max()
    # print("group by max")
    # print(df_max)
    # print("sort group by max")
    # print(df_max.sort_values('x'))

    # df_min = df.groupby(level=[0, 1])['values', 'x'].min()
    # print("group by min")
    # print(df_min)

    # df_max2 = df.groupby(level=[0, 1])[['values', 'x']].max()
    # print("*** group 2 by max ***")
    # df_max2 = df_max2.reset_index()
    # print(df_max2)
    # print(df_max2.sort_values(['component','x']))


load_data()
