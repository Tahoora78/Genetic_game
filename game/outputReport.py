import matplotlib.pylab as plt


def drawing_average_best_worst(average, best, worst):
    nasl = [i for i in range(1, (len(worst))+1)]
    plt.plot(nasl, average, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='green', markersize=12)
    plt.plot(nasl, worst, color='red', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='red', markersize=12)
    plt.plot(nasl, best, color='blue', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()