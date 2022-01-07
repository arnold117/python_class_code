import pandas as pd
import numpy as np
import statistics as sta
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def to_csv():
    data = {
        "dataset": ["Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅰ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ", "Ⅱ",
                    "Ⅱ", "Ⅱ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅲ", "Ⅳ", "Ⅳ", "Ⅳ", "Ⅳ", "Ⅳ", "Ⅳ", "Ⅳ",
                    "Ⅳ", "Ⅳ", "Ⅳ", "Ⅳ"],
        "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5, 10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5, 10, 8, 13, 9, 11, 14, 6, 4,
              12, 7, 5, 8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
        "y": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68, 9.14, 8.14, 8.74, 8.77, 9.26, 8.10,
              6.13, 3.10, 9.13, 7.26, 4.74, 7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73, 6.58,
              5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]}
    df = pd.DataFrame(data)
    df.to_csv("anscombe.csv", header=True, index=False)


if __name__ == "__main__":
    to_csv()
    anascombe = pd.read_csv('anscombe.csv')
    msg = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"]
    Xarray = []
    Yarray = []
    for i in range(4):
        array1 = anascombe.x[i * 11:i * 11 + 11].values
        Xarray.append(array1)
        array2 = anascombe.y[i * 11:i * 11 + 11].values
        Yarray.append(array2)

    print(Xarray, Yarray, sep="\n")
    for j in range(4):
        Xmean = np.mean(Xarray[j])
        print("数据集" + msg[j] + "中的x均值为:%.2f" % Xmean)
        Ymean = np.mean(Yarray[j])
        print("数据集" + msg[j] + "中的y均值为:%.2f" % Ymean)
        Xvariance = sta.variance(Xarray[j])
        print("数据集" + msg[j] + "中的x方差为:%.2f" % Xvariance)
        Yvariance = sta.variance(Yarray[j])
        print("数据集" + msg[j] + "中的y方差为:%.2f" % Yvariance)
        print("-" * 40)

    for k in range(4):
        X = Xarray[k].reshape(-1, 1)
        Y = Yarray[k].reshape(-1, 1)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
        regressor = LinearRegression()
        regressor = regressor.fit(X_train, Y_train)
        plt.title("dataset %s" % msg[k])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.scatter(Xarray[k], Yarray[k], color='red')
        plt.plot(X_train, regressor.predict(X_train), color='blue')
        plt.show()
