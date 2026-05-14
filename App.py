from src.Preprocess import load_data, split_data, preprocess
from src.Features import engineer_features
from src.Train import train_model, save_model
from src.Evaluate import evaluate_model

df = load_data("data/raw/creditcard.csv")
df = engineer_features(df)

x, y = split_data(df, "Class")
x_train, x_test, y_train, y_test = preprocess(x, y)

model = train_model(x_train, y_train)

evaluate_model(model, x_test, y_test)

save_model(model, "models/fraud_model.pkl")
