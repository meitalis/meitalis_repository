import os
import numpy as np
import datetime

print(os.getcwd())
fname = os.getcwd() + "\\mountain-data.txt"
print(fname)


#str2date = lambda x: np.datetime64(datetime.strptime(str(x), '%d/%m/%Y')) if x != "-" else np.datetime64('01/01/2001')
# str2epoch = lambda x: datetime.datetime.strptime(x.decode("utf-8"), '%d/%m/%Y').timestamp() if x != b"-" else datetime.datetime.strptime('01/01/1970'.decode("utf-8"), '%d/%m/%Y').timestamp()
str2epoch = lambda x: datetime.datetime.strptime(x.decode("utf-8"), '%d/%m/%Y').toordinal()
epoch2str = lambda x: datetime.datetime.fromordinal(x)
loc2float = lambda x: round((int(x[0:x.index(b"d")]) + int(x[3:x.index(b"m")])/60 + int(x[6:x.index(b"s")])/3600),3)

dtype = np.dtype([("name","S20"),("height","i8"),("First_ascent_date","uint64"),("First_winter_date","uint64"),("locationN","f8"),("locationE","f8")])

data = np.genfromtxt(fname,dtype=dtype,skip_footer=1,skip_header=4,delimiter='\t',missing_values={2: '-',3: '-'},
                    filling_values={2: 0,3: 0},converters = {2:str2epoch,3:str2epoch, 4: loc2float,5: loc2float} )
print("\n******************* data *******************")
print(data)

print("\n******************* lowest 8,000 m peak *******************")
data.sort(order=["height"])
print(data[0])

print("\n******************* The most northely, easterly, southerly and westerly peaks  *******************")
southerly = np.amin(data["locationN"])
northely = np.amax(data["locationN"])
westerly = np.amin(data["locationE"])
easterly = np.amax(data["locationE"])
print("southerly",southerly,"northely",northely,"westerly",westerly,"easterly",easterly)

print("\n******************* The most recent first ascent of the peaks *******************")
recent_first_ascent = np.amax(data["First_ascent_date"])
print("recent_first_ascent",epoch2str(recent_first_ascent))

print("\n******************* The first of the peaks to be climbed in winter  *******************")
First_winter_date = data["First_winter_date"][data["First_winter_date"] > 0].min()
print("First_winter_date",epoch2str(First_winter_date))

height2feet = lambda x: float(x) * 3.2808399
dtype2 = np.dtype([("name","S20"),("height2feet","f8"),("First_ascent_date","uint64")])
data2 = np.genfromtxt(fname,dtype=dtype2,skip_footer=1,skip_header=4,delimiter='\t',missing_values={2: '-'},
                    filling_values={2: 0},converters = {1:height2feet,2:str2epoch} )
print("\n******************* data2 *******************")
print(data2)

with open('height2feet.txt', 'w') as f:
     data2.sort(order=["height2feet"])
     print(data2,file=f)