import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def machine_learning_plot(data):

    X = np.array(data['DBH']) # Input feature
    y = np.array(data['Total_Annual_Benefits']) # Target variable

    kf = KFold(n_splits=5)

    RMSE_train = []
    RMSE_test = []
    R2_train = []
    R2_test = []

    for train_index, test_index in kf.split(X):
        xTrain, xTest = X[train_index], X[test_index]
        yTrain, yTest = y[train_index], y[test_index]

        model = LinearRegression()
        model.fit(xTrain.reshape(-1, 1), yTrain)

        y_pred_train = model.predict(xTrain.reshape(-1, 1))
        y_pred_test = model.predict(xTest.reshape(-1, 1))

        RMSE_train.append(mean_squared_error(yTrain, y_pred_train, squared=False))
        RMSE_test.append(mean_squared_error(yTest, y_pred_test, squared=False))
        R2_train.append(r2_score(yTrain, y_pred_train))
        R2_test.append(r2_score(yTest, y_pred_test))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(range(1, 6), RMSE_train, color="blue", label="Train")
    plt.scatter(range(1, 6), RMSE_test, color="green", label="Test")
    plt.xticks(range(1, 6))
    plt.xlabel('Fold number')
    plt.ylabel('RMSE')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(range(1, 6), R2_train, color="blue", label="Train")
    plt.scatter(range(1, 6), R2_test, color="green", label="Test")
    plt.xticks(range(1, 6))
    plt.xlabel('Fold number')
    plt.ylabel('R2')
    plt.legend()

    plt.tight_layout()
    plt.savefig('resources/visualizations/ml_results.png')
    # plt.show()
