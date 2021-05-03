from circle import circle
from PID import PID
import numpy as np

class blue(object):
    def __init__(self):
        self.curx = 0
        self.cury = 0
        self.curPos = np.zeros(2)
        self.index = 0
        self.color = 0
        
        self.pid = PID(0.2, 1, 1)
    
    def update(self, redPos):
        distance = np.linalg.norm(self.curPos - redPos)
        self.pid.update(distance)
        self.curPos = self.curPos + self.pid.get() * (self.curPos - redPos)
    
    def getPos(self):
        return np.array([self.curPos[0], self.curPos[1], self.color])

if __name__ == "__main__":
    obj = blue()
    print(obj.curPos)

    redPos = np.array([1, 1])
    obj.update(redPos)
    print(obj.curPos)