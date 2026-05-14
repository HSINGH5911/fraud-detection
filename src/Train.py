from src.Preprocess import load_data, split_data, preprocess

df = load_data("data/raw/creditcard.csv")

X, y = split_data(df, "Class")

X_train, X_test, y_train, y_test = preprocess(X, y)