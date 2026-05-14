from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

def train_model(x_train, y_train):
    model = LogisticRegression()
    model.fit(x_train, y_train)

    return model

def save_model(model, model_path):
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
