import numpy as np
import random,math

class FFNN:
    def __init__(self,dims):
        self.w = []
        self.b = []
        self.l = dims
        self.build()
    def full_pass(self,inputs):
        for x in range(len(self.l)-1):
            inputs = self.layer_dense(inputs,self.w[x],self.b[x],self.l[x+1])
        return inputs

    def layer_dense(self,inp,w,b,n):
        l_out = []
        for x in range(n):
            l_out.append(self.tanh(self.node_dense(inp,w[x])+b[x]))
        return l_out
    
    def node_dense(self,inputs,weights):
        return np.dot(inputs,weights)
    
    def relu(self,x):
       return np.maximum(0,x)
    def tanh(self,x):
        return math.tanh(x)
    def sigmoid(self,x):
        return 1 / (1 + math. exp(-x))

    def build(self):
        for (index,val) in enumerate(self.l[1:]):
            self.b.append([random.uniform(-1,1) for x in range(val)])
            
        for (index,val) in enumerate(self.l[:-1]):
            self.w.append([[random.uniform(-1,1) for x in range(val)] for z in range(self.l[index+1])])

