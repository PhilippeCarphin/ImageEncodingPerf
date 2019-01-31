"""
Image encoding using the predictive algorithm

inspired by:

https://github.com/gabilodeau/INF8770/blob/master/Codage%20predictif%20sur%20image.ipynb
"""
import subprocess
import numpy as np
import matplotlib.pyplot as py


def run(op):
    filename = op['input']
    predictive(op)


def rgb2gray(rgb):
    return np.dot(rgb[:,:], [0.299, 0.587, 0.114])


def predictive(op):
    fig1 = py.figure(figsize = (10,10))
    imagelue = py.imread(op['input'])
    image=imagelue.astype('float')
    image=rgb2gray(image)
    imageout=image.astype('uint8')
    py.imshow(imageout,cmap = py.get_cmap('gray'))

    if 'show' in op.keys():
        py.show()
