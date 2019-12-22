from pandas import Series, DataFrame

import numpy as np
from numpy.random import randn, rand

import pandas.tools.plotting as plotting
import matplotlib.pyplot as plt

s = Series(randn(6), index=range(6))

df = DataFrame(randn(6, 3),
               index=range(6),
               columns=['x', 'y', 'z'])

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
plt.subplots_adjust(top=0.97, bottom=0.2, left=0.05, right=0.97, hspace=0.2)

df.plot(ax=axes[0], table=True, legend=False)
axes[0].get_xaxis().set_visible(False)

df.plot(ax=axes[1], table=np.round(df.T, 2), legend=False)
axes[1].get_xaxis().set_visible(False)

df.plot(ax=axes[2], legend=False)
plotting.table(axes[2], np.round(df.describe(), 2),
                loc='upper right', colWidths=[0.2, 0.2, 0.2])

plt.show()