import math
a= 6378137.0
c= 6356752.314245

e_power_2 = 1- (pow(c,2)/pow(a,2))
s_obl_part_1 = 2 * math.pi * pow(a,2)
s_obl_part_2 = math.atanh(math.sqrt(e_power_2 ))
s_obl_part_3 = (1 - e_power_2 ) / math.sqrt(e_power_2 )

s_obl = s_obl_part_1 * ( 1 + s_obl_part_3 *  s_obl_part_2  )
print("obl", s_obl)


s_sphere = 4 * math.pi * 6371**2
print("sphere", s_sphere)