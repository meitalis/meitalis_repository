# for notebook
# %matplotlib #do not need to use show
#inline or notebook
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.pyplot as plt
#
# plt.plot()
# plt.show()
# fig = plt.figure()
# fig.savefig('fig name.png');
#
# from IPython.dispaly import Image
# Image(...)
#
#
# plt.subplot(2,1,1) #rows , columns, panel number
#

# x = [1,2,3,4,5]
# y= [2,3,4,5,6]
# plt.plot(x,y)
# plt.show()


# a = np.linspace(-2*np.pi,2*np.pi,1000)
# plt.plot(a,np.sin(a)**2,color='red')
# plt.plot(a,np.sin(a)**2,color='0.75',linestyle="--")
# plt.plot(a,np.sin(a)**2,'--g')


# plt.plot(a,np.sin(a)**2,'--g')
# plt.xlim(-1,11)
# plt.ylim(-1.5,1.5)


# plt.plot(a,np.sin(a)**2,'--g')
# plt.axis([-1,11,-1.5,1.5])
#
# plt.axis('tight')


# plt.plot(a,np.sin(a)**2,'--g')
# plt.xlabel("x")
# plt.ylabel("sin(x) ** 2")


# a = np.linspace(-2*np.pi,2*np.pi,1000)
# plt.plot(a,np.sin(a)**2,'--g',label="lg1")
# plt.xlabel("x")
# plt.ylabel("sin(x) ** 2")
# plt.legend();
# plt.grid()


# s = np.linspace(0,1,100)
# y = lambda x: (0.1*x) / (0.04 +x)
# plt.plot(s,y(s))
# plt.xlabel("S")
# plt.ylabel("V")
# plt.grid(axis='y')
# plt.title("title",fontsize=18)



# x = np.linspace(0,10,30)
# y = np.sin(x)
# y1 = np.cos(x)
# plt.plot(x,y,'-ok',x,y1,'-k')


# years_observed = [1972,1974,1978,1982,1985,1989,1993,1997,1999,2000,2003,2004,2007,2008,2012]
# observed = [0.00025,0.005,0.029,0.12,0.275,1.18,3.1,7.5,24,42,220,592,1720,2046,3100]
# l_observed = np.log10(observed)
#
# years_predicted = np.linspace(1972,2012,100)
# predicted = np.log10(0.0025) + ((years_predicted - 1972) / 2 ) * np.log10(2)
# plt.plot(years_observed,l_observed,'*',years_predicted,predicted,'--')



# x = [1972,1974,1978,1982,1985,1989,1993,1997,1999,2000,2003,2004,2007,2008,2012]
# y = [0.00025,0.005,0.029,0.12,0.275,1.18,3.1,7.5,24,42,220,592,1720,2046,3100]
# plt.scatter(x,y,c=range(20),s=18,alpha=0.4,cmap='viridis')
# plt.colorbar();


#more issues
#plt.grid()
#plt.text()
#ax = plt.axes()
#plt.annotate()
#plt.style

#Seaborn - 





plt.show()






