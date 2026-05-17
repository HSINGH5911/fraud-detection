from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

def train_model(x_train, y_train):
    model = XGBClassifier(
        n_estimators=50,
        max_depth=4,
        learning_rate=0.3,
        subsample=0.5,
        colsample_bytree=.7,
        scale_pos_weight=9,
        random_state=42,
        n_jobs=1,
    )

    model.fit(x_train, y_train)

    return model

# def train_model(x_train, y_train):
#     model = RandomForestClassifier(
#         n_estimators=100,
#         random_state=42,
#         n_jobs=1,
#         max_depth = 50,
#         warm_start = True,
#     )
#
#     model.fit(x_train, y_train)
#
#     return model


# def train_model(x_train, y_train):
#     model = LogisticRegression(solver='lbfgs', max_iter=100)
#     model.fit(x_train, y_train)
#
#     return model


def save_model(model, model_path):
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
