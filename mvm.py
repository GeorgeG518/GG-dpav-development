import numpy as np

class modelViewMatrix:
    def __init__(self):
        self.mvm= self.mat4()
        return

    def translate(self, x,y,z):
        self.mvm[0][3]=x
        self.mvm[1][3]=y
        self.mvm[2][3]=z
    
    def rotate(self, rot):
        theta=np.radians(rot)
        c,s = np.cos(theta), np.sin(theta)
        R=np.array([[c, -s, 0, 0], \
                    [s,  c, 0, 0],\
                    [0,  0, 1, 0],
                    [0, 0, 0, 1]])
        
    def scale(self, xs, ys,zs):
        self.mvm[0][0]=self.mvm[0][0]*xs
        self.mvm[1][1]=self.mvm[1][1]*ys
        self.mvm[2][2]=self.mvm[2][2]*zs


    def __mul__(self, other):

        return np.matmul(self.mvm, other)
    
    def mat4(self):
        return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0], [0,0,0,1]])

    def reset(self):
        self.mvm = self.mat4()
