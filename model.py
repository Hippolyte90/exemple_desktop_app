import pandas as pd
from sklearn.linear_model import LinearRegression

def train_and_predict(csv_path, value):
    df = pd.read_csv(csv_path)

    X = df[['x']]
    y = df['y']

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[value]])
    return round(prediction[0], 2)
