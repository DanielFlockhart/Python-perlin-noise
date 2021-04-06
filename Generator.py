from PIL import Image,ImageDraw
import random,math,time
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
import time
import NeuralNet as net


class Generator:
    def __init__(self,dims,network):
        self.network = network
        self.xDim = dims[0]
        self.yDim = dims[1]
        self.env = [[1 for x in range(dims[0])] for y in range(dims[1])]
    def getEnv(self):
        return self.env
    def genEnv(self,bias):
        start = time.time()
        for x in range(0,self.xDim):
            for y in range(0,self.yDim):
                colour = self.network.full_pass([
                    x/self.xDim,
                    y/self.yDim,
                    (time.time()-start)])[0]
                self.env[x][y] = round(max((colour*255)+bias,0))
                #print(self.env[x][y])
            #print(f'Generated {x/self.xDim * 100}%')
