pos_num = input("enter pos num")
import math as m
count = m.floor(m.log10(int(pos_num)))
#count = m.floor(m.log10(int(pos_num)) + 1)
print (count)

#log10(100) = 2
#log10(1000) = 3
