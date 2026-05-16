import ast
from datetime import datetime
from pathlib import Path


def get_imports(file_path):
    source = Path(file_path).read_text()
    tree = ast.parse(source)

    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(source, node))

    return imports


def get_model_import(model, file_path):
    source = Path(file_path).read_text()
    tree = ast.parse(source)
    model_name = model.__class__.__name__

    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported_name = alias.asname or alias.name
                if imported_name == model_name:
                    return ast.get_source_segment(source, node)

        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_name = alias.asname or alias.name.split(".")[-1]
                if imported_name == model_name:
                    return ast.get_source_segment(source, node)

    model_class = model.__class__
    return f"from {model_class.__module__} import {model_name}"


def append_results(results_path, model, metrics, imports_path):
    results_file = Path(results_path)
    results_file.parent.mkdir(parents=True, exist_ok=True)

    model_name = model.__class__.__name__
    model_params = model.get_params()
    model_import = get_model_import(model, imports_path)
    imports = get_imports(imports_path)

    with results_file.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 72 + "\n")
        file.write(f"Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        file.write("Imports:\n")
        for import_line in imports:
            file.write(f"{import_line}\n")

        file.write(f"\nActive model import:\n{model_import}\n")
        file.write(f"\nModel: {model_name}\n")
        file.write("Parameters:\n")
        for param, value in model_params.items():
            file.write(f"{param}={value!r}\n")

        file.write("\nMetrics:\n")
        file.write(f"Accuracy {metrics['accuracy']}\n")
        file.write(f"Precision {metrics['precision']}\n")
        file.write(f"Recall {metrics['recall']}\n")
        file.write(f"F1 {metrics['f1']}\n")
        file.write("Confusion Matrix\n")
        file.write(f"{metrics['confusion_matrix']}\n")
