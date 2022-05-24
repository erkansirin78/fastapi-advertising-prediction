import os
import joblib
import pathlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def read_and_train():
    # read data
    df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/Advertising.csv")
    print(df.head())

    # Feature matrix
    X = df.iloc[:, 1:-1].values
    print(X.shape)
    print(X[:3])

    # Output variable
    y = df.iloc[:, -1]
    print(y.shape)
    print(y[:6])

    # split test train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # train model
    estimator = RandomForestRegressor(n_estimators=200)
    estimator.fit(X_train, y_train)

    # Test model
    y_pred = estimator.predict(X_test)
    r2 = r2_score(y_true=y_test, y_pred=y_pred)
    print(f"R2: {r2}")

    # Save Model
    current_dir = pathlib.Path(__file__).parent.resolve()
    print(f"current_dir: {current_dir}")
    try:
        os.mkdir(os.path.join(current_dir, 'saved_models'))
    except:
        print("FileExistsError: File exists.")
    dirname = os.path.join(current_dir, 'saved_models')
    print(dirname)

    joblib.dump(estimator, os.path.join(dirname,"03.randomforest_with_advertising.pkl"))

    # make predictions
    # Read models
    estimator_loaded = joblib.load(os.path.join(dirname,"03.randomforest_with_advertising.pkl"))

    # Prediction set
    X_manual_test = [[230.1, 37.8, 69.2]]
    print("X_manual_test", X_manual_test)

    prediction = estimator_loaded.predict(X_manual_test)
    print("prediction", prediction)