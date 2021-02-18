# -*- coding: utf-8 -*-
"""cdf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e2LRXz5J6QVJOnMs6vYTbH35pkxiV2PE
"""

def to_cdf(a):
    x, counts = np.unique(a, return_counts=True)
    y = np.cumsum(counts)
    x = np.insert(x, 0, x[0])
    y = np.insert(y/y[-1], 0, 0.)
    plt.plot(x, y, drawstyle='steps-post')
    plt.grid(True)
    # specify the column name here
    plt.savefig('fig.png')
#specify the column name here
to_cdf(df['latitude'])

