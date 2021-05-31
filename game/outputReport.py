import matplotlib.pylab as plt
import numpy as np


def drawing_average_best_worst(average, best, worst):
    x = np.array([i for i in range(1, (len(average))+1)])
    plt.plot(x, average, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='green', markersize=12)
    plt.plot(x, worst, color='red', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='red', markersize=12)
    plt.plot(x, best, color='blue', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()