from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import os, re, glob, io

fig = plt.figure()
axes = fig.add_subplot(111)
axes.xaxis.set_major_locator(MaxNLocator(symmetric=True))

upsrt = pd.DataFrame({'DAC3' : pd.Series([-2.1, -1., 0., 1., 2.]),
                      'norm' : pd.Series([5., 3., 6., 8., 2.])})

downsrt = pd.DataFrame({'DAC3' : pd.Series([-2., -1., 0., 1., 2.]),
                        'norm' : pd.Series([3., 7., 3., 6., 7.])})

upsrt.plot(x='DAC3', y='norm', color='red', label='Up',ax=axes)

downsrt.plot(x='DAC3', y='norm', color='blue', label='Down', ax=axes)

plt.show()