from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

def train_model(x_train, y_train):
    model = RandomForestClassifier(
        n_estimators=50,
        random_state=42,
        class_weight='balanced',
        max_depth=10,
        n_jobs=1,
    )

    model.fit(x_train, y_train)

    return model


# def train_model(x_train, y_train):
#     model = LogisticRegression(random_state=0, solver='lbfgs')
#     model.fit(x_train, y_train)
#
#     return model


def save_model(model, model_path):
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
