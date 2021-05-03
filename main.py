from PID import PID
from circle import circle
from animatedScatter import AnimatedScatter
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation

if __name__ == "__main__":
    circle = circle()
    pid = PID()


    path = circle.getPath()

    plot = AnimatedScatter(path)
    plt.show()