from pandas.io.xml import preprocess_data

from src.Preprocess import *
from src.Features import *
from src.Train import *
from src.Evaluate import *

df = load_data("data/raw/creditcard.csv")
df = engineer_features(df)

x, y = split_data(df, "Class")
x_train, x_test, y_train, y_test = preprocess_data(x, y)

model = train_model(x_train, y_train)

evaluate_model(model, x_test, y_test)

save_model(model, "models/fraud_model.pkl")
