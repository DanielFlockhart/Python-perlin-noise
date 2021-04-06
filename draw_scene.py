from PIL import Image,ImageDraw
import random

deepocean = (0,25,255)
ocean = (25,210,255)
beach = (250,255,0)
earth = (130,75,0)
green = (0,255,0)
rock = (115,115,115)
snow = (255,255,255)
types = [deepocean,ocean,beach,earth,green,rock,snow]
class Draw:
    def __init__(self,dims,values):
        self.xDim = dims[0]
        self.yDim = dims[1]
        self.gradients = values
        self.res = self.draw_Environment()
        
    def save_image(self,name,ftype,im):
        im.save(f'{name}.png', f'{ftype}')#PNG
    def load_image(self,):
        pass
    def draw_Environment(self):
        im = Image.new('RGB', (self.xDim, self.yDim), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for x in range(0,self.xDim):
            for y in range(0,self.yDim):
                colour = (self.gradients[0][x][y],self.gradients[1][x][y],self.gradients[2][x][y])#types[get_type(round(self.gradients[x][y]))]
                draw.point([x, y], colour)
        return im
    
def get_type(height):
    x = min(round(height // 50),6)
    return x

        
