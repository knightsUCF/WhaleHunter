import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


class Chart():
    

    def graph(self, title, x_label, x = [1, 2, 3, 4], y = ['a', 'b', 'c', 'd']):
        font = {'family' : 'Arial',
        'weight' : 'bold',
        'size'   : 4}
        plt.rc('font', **font)
        y_pos = np.arange(len(x))
        plt.barh(y_pos, x, align = 'center', alpha = 0.4)
        plt.yticks(y_pos, y)
        plt.xlabel(x_label)
        plt.title(title)
        plt.show()



