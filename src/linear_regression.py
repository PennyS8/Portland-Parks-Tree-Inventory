from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

def linear_regression(data):
    # Step 1: Extract input features (X) and target variable (y) from data dictionary
    X = np.array(data['DBH']).reshape(-1, 1)  # Input feature
    y = np.array(data['Total_Annual_Benefits'])  # Target variable

    # Step 2: Standardization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 3: Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Step 4: Train Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 5: Evaluate Performance
    # Predict on training and testing sets
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Calculate R2 and RMSE for training set
    r2_train = r2_score(y_train, y_train_pred)
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))

    # Calculate R2 and RMSE for testing set
    r2_test = r2_score(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))

    # Step 6: Plot Model Prediction
    plt.scatter(X_train, y_train, color='blue', label='Training Data')
    plt.scatter(X_test, y_test, color='green', label='Testing Data')
    plt.plot(X_train, model.predict(X_train), color='red', label='Linear Regression Model')
    plt.xlabel('Diameter at Breast Height (DBH)')
    plt.ylabel('Total Annual Benefits')
    plt.title('Linear Regression Model Prediction')
    plt.savefig('resources/visualizations/linear_regression_prediction.png')
    # plt.show()

    # Step 7: Describe Model Performance
    print('\nTraining set performance:')
    print('R2:', r2_train)
    print('RMSE:', rmse_train)
    print('\nTesting set performance:')
    print('R2:', r2_test)
    print('RMSE:', rmse_test)