import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris

#list
# thelist = [ 178,-143,522,100,6,-38,118,153,-212,670,6,132]
# pd_lst = pd.Series( thelist )
#
# print("pd_lst=" , pd_lst)
# print(pd_lst.shape)

#numpy
# arr = np.array([ 178,-143,522,100,6,-38,118,153,-212,670,6,132])
# pd_np = pd.Series( arr )
# print("pd_np=" , pd_np)
# print(pd_np.shape)

#index
# index = [100,200,300,400,500,600,700,800,900,1000,1100,1200]
# arr_2 = np.array([ 178,-143,522,100,6,-38,118,153,-212,670,6,132])
# pd_np_2 = pd.Series( arr_2,index )
#
# print("pd_np_2=" , pd_np_2)
# print(pd_np_2.shape)
#
# pd_np_3 = pd_np_2.astype('int64')
# print("pd_np_3=" , pd_np_3)
# print(pd_np_3.shape)


#dict
# data = {'a':0,'b':1,'c':2,'d':6}
# pd_dict = pd.Series( data )
# print(pd_dict)


# df = pd.DataFrame()
# if df.empty:
#     print("Sorry. This df is empty")


# thelist = [ 178,-143,522,100,6,-38,118,153,-212,670,6,132]
# df = pd.DataFrame(thelist)
# #print(df)
# print(df.dtypes)

# ind = [1,2,3,4]
# all_data=[['Alex',53],['Bob',33],['Clarke',64],['Chip',29]]
# cols = ["Name","Age"]
# df = pd.DataFrame(data=all_data,columns=cols,index=ind)
# print(df)

#dict
# dict ={
#     'Name':
#         ['Tom','Jack','Steve','Ricky'],
#
#     'Age':
#         [28,34,29,42]
# }
#
# df = pd.DataFrame(dict)
# print(df)
#
# df["blood_pressure"] = [120,80,95,105]
# print("***************** add blood_pressure *************")
# print(df)


#data = load_breast_cancer()

#print(type(data.data))

#ds = pd.DataFrame(data=data.data,columns=data.feature_names)
#print(ds)
#print(data.target)
#print(ds.head(10))
#print(ds.tail(10))

#ds["target"] = data.target
#print(ds.head(10))

#print(ds.corr())
#print(ds.count())
#print(ds.mean())
#print(ds.min())
#print(ds.max())
#print(ds.describe())

#pd.set_option('display.max_columns',100)
#print(ds.describe())

#ds.drop("mean radius",axis=1,inplace=True)
#print(ds.head(10))

#print(ds["mean radius"]) # just to dispaly

#print(ds.loc[:,"mean radius"]) # work wlike this
#print(ds.loc[:,["mean radius","mean symmetry"]]) # work wlike this

#print(ds.columns)


#ind = ds.columns.get_loc("mean symmetry")
#print(ds.iloc[:,ind])
#print(ds.iloc[20:30,ind])
#print(ds.iloc[20:30,[3,4,5]])

#df2 = ds[["mean radius","mean concave points","mean symmetry"]]
#ds.drop(["mean radius","mean concave points","mean symmetry"],axis=1,inplace=True)

#print(ds.head(10))
#print(df2.head(10))


#df3 = pd.concat([df2,ds],axis=1)
#print(df3.head(10))

#df2 = pd.concat([df2,df2],axis=1)
#print(df2.head(10))

#print(ds["mean radius"] > 20)
#print(ds[ds["mean radius"] > 20])


#ds[(ds["mean radius"] > 20) & (ds["mean radius"] <= 21)]
#ds[(ds["mean radius"] == 20.6) | (ds["mean radius"] == 20.55)]
#ds[(ds["mean radius"] == 20.6) | (ds["mean area"] == 1308.0)]
#ds[~(ds["mean compactness"] > 20.6) | (ds["mean area"] == 1308.0)]

#ds.isnull()
#ds.notnull()
#ds[ds.notnull()]

data2 = load_iris()
ds = pd.DataFrame(data=data2.data,columns=data2.feature_names)
ds["target"] = data2.target

data2.target_names

df['target'] = df['target'].replace(0,"setosa")
df.loc[:,'target'][df.loc[:,'target']==1] = 'versicolor'