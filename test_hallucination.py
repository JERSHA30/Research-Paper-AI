import json
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai.answer_generator import generate_answer


# Load paper
with open(
    "data/processed/paper_data.json",
    "r",
    encoding="utf-8"
) as file:

    paper_data = json.load(file)


# Questions that should NOT be answerable from the paper
questions = [
    "What is the favorite programming language of the authors?",
    "Where do the authors live?",
    "What is the personal email password of the authors?",
    "What is the favorite food of the authors?",
    "What is the next research paper the authors will publish?"
]


print("\n==============================")
print("HALLUCINATION TEST")
print("==============================")


for question in questions:

    # No relevant evidence is intentionally supplied
    evidence = []

    answer = generate_answer(
        question,
        evidence
    )

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer)

    print("\n------------------------------")