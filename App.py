from src.Preprocess import load_data, split_data, preprocess
from src.Features import engineer_features
from src.Train import train_model, save_model
from src.Evaluate import evaluate_model
from src.Results import append_results

print("Loading data...", flush=True)
df = load_data("data/raw/creditcard.csv")

print("Engineering features...", flush=True)
df = engineer_features(df)

print("Splitting and scaling data...", flush=True)
x, y = split_data(df, "Class")
x_train, x_test, y_train, y_test = preprocess(x, y)

print("Training model...", flush=True)
model = train_model(x_train, y_train)

print("Evaluating model...", flush=True)

print("Saving model...", flush=True)
save_model(model, "models/fraud_model.pkl")

print("Done.", flush=True)

print()
print("Results:")

metrics = evaluate_model(model, x_test, y_test)
append_results("results.txt", model, metrics, "src/Train.py")
print("Saved results to results.txt", flush=True)
