# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-1,5,80)
y=2*x
plt.plot(x,y,linewidth=5,color='k',label='Parabola')

plt.show()
