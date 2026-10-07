import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai.answer_generator import generate_answer


test_cases = [
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


correct = 0
incorrect = 0


print("\n==============================")
print("Q&A ACCURACY EVALUATION")
print("==============================")


for i, test in enumerate(test_cases, start=1):

    question = test["question"]
    evidence = test["evidence"]
    expected_keywords = test["expected_keywords"]

    answer = generate_answer(
        question,
        evidence
    )

    answer_lower = answer.lower()

    matched = all(
        keyword.lower() in answer_lower
        for keyword in expected_keywords
    )

    print(f"\nTEST {i}")

    print("Question:")
    print(question)

    print("\nAnswer:")
    print(answer)

    print("\nExpected keywords:")
    print(expected_keywords)

    if matched:
        print("Result: PASS")
        correct += 1
    else:
        print("Result: FAIL")
        incorrect += 1

    print("------------------------------")


total = len(test_cases)

accuracy = (
    correct / total
) * 100


print("\n==============================")
print("FINAL METRICS")
print("==============================")

print("Total questions:", total)
print("Correct:", correct)
print("Incorrect:", incorrect)
print(f"Accuracy: {accuracy:.2f}%")