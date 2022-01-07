import pandas as pd
import numpy as np
import statistics as sta
from matplotlib import pyplot as plt


def to_csv():
    data = {"dataset": ["Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ"],
            "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            "y": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]}
    df = pd.DataFrame(data)
    df.to_csv("anscombe.csv", header=True, index=False)


if __name__ == "__main__":
    to_csv()
    anascombe = pd.read_csv('anscombe.csv')
    print(anascombe)

    Xarray = []
    Yarray = []

    Xarray = anascombe.x[0:11].values
    print(Xarray)
    Yarray = anascombe.y[0:11].values
    print(Yarray)
    Xmean = np.mean(Xarray)
    print(Xmean)
    Ymean = np.mean(Yarray)
    print("{:.2f}".format(Ymean))
    Xvariance = sta.variance(Xarray)
    print("{:.2f}".format(Xvariance))
    Yvariance = sta.variance(Yarray)
    print("{:.2f}".format(Yvariance))

    plt.title("anscombe dataset Ⅰ")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(Xarray, Yarray)
    plt.show()
