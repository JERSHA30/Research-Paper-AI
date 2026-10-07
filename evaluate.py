import sys
import os
import json

# Allow Python to find the ai package
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai.answer_generator import generate_answer


# ============================================================
# TEST 1 — Q&A ACCURACY
# ============================================================

qa_tests = [

    {
        "question": "What dataset is used in the paper?",
        "evidence": [
            {
                "page_start": 1,
                "page_end": 1,
                "text": "The experiments are conducted on the MNIST dataset."
            }
        ],
        "expected_keywords": ["MNIST"]
    },

    {
        "question": "What type of neural network is discussed?",
        "evidence": [
            {
                "page_start": 2,
                "page_end": 2,
                "text": "The paper investigates Single-Layer Feedforward Networks (SLFNs) and Extreme Learning Machine (ELM) methods."
            }
        ],
        "expected_keywords": [
            "Single-Layer Feedforward",
            "ELM"
        ]
    },

    {
        "question": "Which method achieved strong performance?",
        "evidence": [
            {
                "page_start": 7,
                "page_end": 7,
                "text": "The RF-CIW-ELM method achieves an error rate below 1% on the MNIST test dataset."
            }
        ],
        "expected_keywords": [
            "RF-CIW-ELM"
        ]
    }
]


# ============================================================
# TEST 2 — HALLUCINATION / UNSUPPORTED QUESTIONS
# ============================================================

hallucination_tests = [

    {
        "question": "What programming language was used by the authors?",
        "evidence": []
    },

    {
        "question": "What is the favorite programming language of the authors?",
        "evidence": []
    },

    {
        "question": "Where do the authors live?",
        "evidence": []
    },

    {
        "question": "What university did the authors attend?",
        "evidence": []
    },

    {
        "question": "What is the authors' favorite machine learning framework?",
        "evidence": []
    }
]


# ============================================================
# RUN Q&A TESTS
# ============================================================

qa_correct = 0
qa_incorrect = 0

print("\n==============================")
print("Q&A ACCURACY EVALUATION")
print("==============================")

for i, test in enumerate(qa_tests, start=1):

    answer = generate_answer(
        test["question"],
        test["evidence"]
    )

    answer_lower = answer.lower()

    passed = all(
        keyword.lower() in answer_lower
        for keyword in test["expected_keywords"]
    )

    print(f"\nTEST {i}")
    print("Question:", test["question"])
    print("Answer:", answer)

    if passed:
        print("Result: PASS")
        qa_correct += 1
    else:
        print("Result: FAIL")
        qa_incorrect += 1


qa_total = len(qa_tests)

qa_accuracy = (
    qa_correct / qa_total * 100
    if qa_total > 0
    else 0
)


# ============================================================
# RUN HALLUCINATION TESTS
# ============================================================

hallucination_rejected = 0

print("\n==============================")
print("HALLUCINATION EVALUATION")
print("==============================")

for i, test in enumerate(
    hallucination_tests,
    start=1
):

    answer = generate_answer(
        test["question"],
        test["evidence"]
    )

    answer_lower = answer.lower()

    rejection_phrases = [
        "no relevant evidence",
        "not mentioned in the paper",
        "not provided",
        "does not contain",
        "does not mention",
        "not available",
        "insufficient information"
    ]

    rejected = any(
        phrase in answer_lower
        for phrase in rejection_phrases
    )

    print(f"\nTEST {i}")
    print("Question:", test["question"])
    print("Answer:", answer)

    if rejected:
        print("Result: CORRECTLY REJECTED")
        hallucination_rejected += 1
    else:
        print("Result: POSSIBLE HALLUCINATION")


hallucination_total = len(
    hallucination_tests
)

rejection_rate = (
    hallucination_rejected
    / hallucination_total
    * 100
    if hallucination_total > 0
    else 0
)


# ============================================================
# FINAL RESULTS
# ============================================================

print("\n==============================")
print("FINAL AI EVALUATION")
print("==============================")

print("\nQ&A Accuracy")
print("------------------------------")

print("Total questions:", qa_total)
print("Correct:", qa_correct)
print("Incorrect:", qa_incorrect)
print(f"Accuracy: {qa_accuracy:.2f}%")


print("\nHallucination Rejection")
print("------------------------------")

print(
    "Total unsupported questions:",
    hallucination_total
)

print(
    "Correctly rejected:",
    hallucination_rejected
)

print(
    f"Rejection rate: {rejection_rate:.2f}%"
)


# ============================================================
# SAVE JSON REPORT
# ============================================================

results = {

    "qa_evaluation": {
        "total_questions": qa_total,
        "correct": qa_correct,
        "incorrect": qa_incorrect,
        "accuracy_percent": round(
            qa_accuracy,
            2
        )
    },

    "hallucination_evaluation": {
        "total_questions": hallucination_total,
        "correctly_rejected": hallucination_rejected,
        "rejection_rate_percent": round(
            rejection_rate,
            2
        )
    }
}


output_path = (
    "data/processed/"
    "evaluation_results.json"
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


print("\nEvaluation report saved to:")
print(output_path)