from pathlib import Path


RESULTS_PATH = Path("raw_results.txt")
CLEANED_RESULTS_PATH = Path("cleaned_results.txt")


def parse_results(results_path=RESULTS_PATH):
    text = results_path.read_text(encoding="utf-8")
    blocks = [block.strip() for block in text.split("=" * 72) if block.strip()]

    runs = []
    for block in blocks:
        lines = [line.rstrip() for line in block.splitlines()]
        run = {
            "run": "",
            "imports": [],
            "active_model_import": "",
            "model": "",
            "parameters": {},
            "metrics": {},
            "confusion_matrix": [],
        }

        section = None
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if not line:
                i += 1
                continue

            if line.startswith("Run:"):
                run["run"] = line.removeprefix("Run:").strip()
            elif line == "Imports:":
                section = "imports"
            elif line == "Active model import:":
                run["active_model_import"] = lines[i + 1].strip()
                i += 1
            elif line.startswith("Model:"):
                run["model"] = line.removeprefix("Model:").strip()
            elif line == "Parameters:":
                section = "parameters"
            elif line == "Metrics:":
                section = "metrics"
            elif line == "Confusion Matrix":
                run["confusion_matrix"] = [
                    lines[i + 1].strip(),
                    lines[i + 2].strip(),
                ]
                i += 2
            elif section == "imports":
                run["imports"].append(line)
            elif section == "parameters" and "=" in line:
                name, value = line.split("=", 1)
                run["parameters"][name] = value
            elif section == "metrics":
                name, value = line.split(maxsplit=1)
                run["metrics"][name.lower()] = float(value)

            i += 1

        runs.append(run)

    return runs


def make_map(runs):
    condensed = {}

    for run in runs:
        name = f"{run['run']} | {run['model']} | {run['active_model_import']}"
        condensed[name] = {
            "accuracy": run["metrics"]["accuracy"],
            "precision": run["metrics"]["precision"],
            "recall": run["metrics"]["recall"],
            "f1": run["metrics"]["f1"],
            "confusion_matrix": run["confusion_matrix"],
            "parameters": run["parameters"],
        }

    return condensed


def format_runs(condensed):
    output = []

    for name, values in condensed.items():
        output.append(name)
        output.append("  Parameters:")
        for param, value in values["parameters"].items():
            output.append(f"    {param}: {value}")
        output.append(f"  Accuracy : {values['accuracy']}")
        output.append(f"  Precision: {values['precision']}")
        output.append(f"  Recall   : {values['recall']}")
        output.append(f"  F1       : {values['f1']}")
        output.append(f"  Confusion Matrix: {values['confusion_matrix']}")
        output.append("")

    return "\n".join(output)


def format_highest(condensed, metric):
    name, values = max(condensed.items(), key=lambda item: item[1][metric])
    output = [
        f"Highest {metric}:",
        name,
        str(values[metric]),
        "Parameters:",
    ]

    for param, value in values["parameters"].items():
        output.append(f"  {param}: {value}")

    output.append("")
    return "\n".join(output)


def build_report(condensed):
    sections = [
        format_runs(condensed),
        format_highest(condensed, "accuracy"),
        format_highest(condensed, "precision"),
        format_highest(condensed, "recall"),
        format_highest(condensed, "f1"),
    ]

    return "\n".join(sections)


def save_report(report, cleaned_results_path=CLEANED_RESULTS_PATH):
    cleaned_results_path.write_text(report, encoding="utf-8")


def main():
    runs = parse_results()
    condensed = make_map(runs)
    report = build_report(condensed)

    print(report)
    save_report(report)
    print(f"Saved cleaned results to {CLEANED_RESULTS_PATH}")


if __name__ == "__main__":
    main()
