# Create plots
import matplotlib.pyplot as plt
import numpy as np


# Plots examples taken from
# https://matplotlib.org/stable/gallery/index.html

def create_barplot(file_path: str) -> None:
    N = 5
    menMeans = (20, 35, 30, 35, -27)
    womenMeans = (25, 32, 34, 20, -25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()

    p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
    p2 = ax.bar(ind, womenMeans, width,
                bottom=menMeans, yerr=womenStd, label='Women')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
    ax.legend()

    # Label with label_type 'center' instead of the default 'edge'
    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    ax.bar_label(p2)

    plt.savefig(file_path)

    return 


def create_scatterplot(file_path:str) -> None:
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.figure()
    x = np.arange(0.0, 50.0, 2.0)
    y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
    s = np.random.rand(*x.shape) * 800 + 500

    plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
                label="Luck")
    plt.xlabel("Leprechauns")
    plt.ylabel("Gold")
    plt.legend(loc='upper left')

    plt.savefig(file_path)

    return