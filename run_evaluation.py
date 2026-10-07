import json
import os


results = {
    "qa_evaluation": {
        "total_questions": 3,
        "correct": 0,
        "incorrect": 0,
        "accuracy": 0
    },
    "hallucination_evaluation": {
        "total_questions": 5,
        "correctly_rejected": 0,
        "rejection_rate": 0
    }
}


output_path = "data/processed/evaluation_results.json"


os.makedirs(
    "data/processed",
    exist_ok=True
)


with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4
    )


print("Evaluation file created:")
print(output_path)