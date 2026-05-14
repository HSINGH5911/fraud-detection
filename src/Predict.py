import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict_transactions(model, transactions):
    predictions = model.predict(transactions)
    return predictions

def predict_probabilities(model, transactions):
    predictions = model.predict_proba(transactions)[0][1]
    return predictions