import matplotlib.pylab as plt


def drawing_average_best_worst(average, best, worst):
    plt.hist(average, bins='auto', color='green',
                            alpha=0.7, rwidth=0.85)
    plt.hist(best, bins='auto', color='red',
                            alpha=0.7, rwidth=0.85)
    plt.hist(worst, bins='auto', color='blue',
                            alpha=0.7, rwidth=0.85)
    plt.show()