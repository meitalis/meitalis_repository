import os
import numpy as np
fname = os.getcwd() + "\\weather-raw.csv"


#dtype = np.dtype([("Tempdeg","f8"),("PressmBar","i8")])
#dtype = np.dtype([("Tempdeg","f8"),("PressmBar","f8")])

#data = np.genfromtxt(fname,dtype=dtype,skip_footer=0,skip_header=0,delimiter=',',usecols=(1,4),missing_values={1: -1, 4:-1},filling_values={1: np.NAN,4: np.NaN})
data = np.genfromtxt(fname,skip_footer=0,skip_header=0,delimiter=',',usecols=(1,4))
print(data[55485])
mask = np.any(np.isnan(data),axis=1)

data = data[~mask]
#print(data)

x = data[:,0]
y = data[:,1]
c = np.corrcoef(x,y)
print(c)