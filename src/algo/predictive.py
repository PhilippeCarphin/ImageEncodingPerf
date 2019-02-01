"""
Image encoding using the predictive algorithm

inspired by:
https://github.com/gabilodeau/INF8770/blob/master/Codage%20predictif%20sur%20image.ipynb
"""
import subprocess
import numpy as np
import matplotlib.pyplot as py
from PIL import Image


matpred_normal = [[0.33,0.33],
                  [0.33,0.0]]

matpred_bad    = [[0.0,0.0],
                  [0.0,0.0]]
def run(op):
    if op.get('pred') == 'bad':
        matpred = matpred_bad
    else:
        matpred = matpred_normal
    input_f  = op['input']
    output_f = op['output']

    image = prepare_image(op)
    image = prepare_for_predictive(image)
    image = exec_prediction(image, matpred)

    im = Image.fromarray(image)
    im = im.convert("L")
    im.save(output_f)

    if 'show' in op.keys():
        img = mpimg.imread(filename)
        imgplot = plt.imshow(img)
        plt.show()


def rgb2gray(rgb):
    return np.dot(rgb[:,:], [0.299, 0.587, 0.114])


def prepare_image(op):
    """Lecture d'une image, conversion en tons de gris, conversion de
    l'image en float pour les calculs, et affichage
    """
    fig1 = py.figure(figsize = (10,10))
    imagelue = py.imread(op['input'])
    image=imagelue.astype('float')
    image=rgb2gray(image)

    if 'show' in op.keys():
        imageout=image.astype('uint8')
        py.imshow(imageout,cmap = py.get_cmap('gray'))
        py.show()

    return image


def prepare_for_predictive(image):
    """Duplication des colonnes et rangées pour les frontières.
    """
    col=image[:,0]
    image = np.column_stack((col,image))
    col=image[:,len(image[0])-1]
    image = np.column_stack((col,image))
    row=image[0,:]
    image = np.row_stack((row,image))
    row=image[len(image)-1,:]
    image = np.row_stack((row,image))
    return image


def exec_prediction(image, matpred):
    erreur = np.zeros((len(image)-2,len(image[0])-2))
    imagepred = np.zeros((len(image)-2,len(image[0])-2))
    for i in range(1,len(image)-2):
        for j in range(1,len(image[0])-2):
            imagepred[i][j] = \
                 image[i-1][j-1]* matpred[0][0]\
               + image[i-1][j]  * matpred[0][1]\
               + image[i][j-1]  * matpred[1][0]
            erreur[i][j]=imagepred[i][j]-image[i][j]

    return imagepred
