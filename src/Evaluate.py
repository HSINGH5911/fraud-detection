from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
    }

    print("Accuracy", metrics["accuracy"])
    print("Precision", metrics["precision"])
    print("Recall", metrics["recall"])
    print("F1", metrics["f1"])

    print("Confusion Matrix")
    print(metrics["confusion_matrix"])

    return metrics
