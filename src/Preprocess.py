from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def split_data(df, target_col):
    x = df.drop(target_col, axis=1)
    y = df[target_col]

    return x, y

def preprocess(x, y):
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    scaler = StandardScaler()

    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    return x_train_scaled, x_test_scaled, y_train, y_test
