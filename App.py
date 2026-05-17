from src.Preprocess import load_data, split_data, preprocess
from src.Features import engineer_features
from src.Train import train_model, save_model
from src.Evaluate import evaluate_model
from src.Results import append_results
from ProcessData import process_results


def run_training(progress=print):
    progress("Loading data...")
    df = load_data("data/raw/creditcard.csv")

    progress("Engineering features...")
    df = engineer_features(df)

    progress("Splitting and scaling data...")
    x, y = split_data(df, "Class")
    x_train, x_test, y_train, y_test = preprocess(x, y)

    progress("Training model...")
    model = train_model(x_train, y_train)

    progress("Evaluating model...")

    progress("Saving model...")
    save_model(model, "models/fraud_model.pkl")

    progress("Done.")
    progress("")
    progress("Results:")

    metrics = evaluate_model(model, x_test, y_test)
    append_results("raw_results.txt", model, metrics, "src/Train.py")
    progress("Saved results to raw_results.txt")

    cleaned_results_path = process_results()
    progress(f"Saved cleaned results to {cleaned_results_path}")
    return cleaned_results_path


if __name__ == "__main__":
    run_training(lambda message: print(message, flush=True))
