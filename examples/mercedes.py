# https://www.kaggle.com/c/mercedes-benz-greener-manufacturing
import pandas as pd
import scipy.io

from deeptabular.deeptabular import DeepTabularRegressor

if __name__ == "__main__":
    train = pd.read_csv("../data/mercedes/train.csv")

    targets = ["y"]
    num_cols = []
    cat_cols = ["X%s" % i for i in range(386) if "X%s" % i in train.columns.values]

    for k in num_cols:
        train[k] = (train[k] - train[k].mean()) / train[k].std()

    regressor = DeepTabularRegressor(num_layers=4)

    regressor.fit(train, cat_cols=cat_cols, num_cols=num_cols, target_cols=targets)