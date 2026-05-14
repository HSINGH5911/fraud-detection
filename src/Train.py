from src.Preprocess import load_data, split_data, preprocess
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(x_train, y_train):
    model = LogisticRegression()
    model.fit(x_train, y_train)

    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)

df = load_data("data/raw/creditcard.csv")

X, y = split_data(df, "Class")

X_train, X_test, y_train, y_test = preprocess(X, y)