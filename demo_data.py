DEMO_SUMMARY = """
This research paper presents a simple machine learning approach for predicting
student performance. The system uses attendance percentage, weekly study hours,
assignment scores, and previous examination marks as input features. The data is
cleaned and divided into training and testing portions, and a Decision Tree
classifier is trained to classify students into satisfactory and at-risk
performance groups. The results show that basic academic features can provide
useful information for early identification of students who may need academic
support.
"""


DEMO_INSIGHTS = [
    "The main objective is to predict student performance and identify students who may be at risk.",
    "The system uses attendance, study hours, assignment scores, and previous examination marks as input features.",
    "A Decision Tree classifier is used for student performance classification.",
    "Attendance and previous examination marks appear to be useful indicators of student performance.",
    "The proposed approach can be used as a basic early-warning component in an educational analytics system."
]


DEMO_TERMS = [
    {
        "term": "Machine Learning",
        "meaning": "A method of learning patterns from data."
    },
    {
        "term": "Classification",
        "meaning": "Assigning data to predefined categories."
    },
    {
        "term": "Feature",
        "meaning": "An input variable used by a machine learning model."
    },
    {
        "term": "Decision Tree",
        "meaning": "A tree-based machine learning model used for prediction."
    },
    {
        "term": "Training Data",
        "meaning": "Data used to learn model patterns."
    },
    {
        "term": "Testing Data",
        "meaning": "Data used to evaluate the trained model."
    }
]


DEMO_RESEARCH_GAP = {
    "gap": "The study uses a small sample dataset and only a limited number of academic features.",
    "limitations": [
        "The dataset contains only a small number of students.",
        "Only four academic features are considered.",
        "Factors such as motivation, learning environment, and financial conditions are not included."
    ],
    "future_work": [
        "Use larger datasets.",
        "Include additional student-related features.",
        "Compare multiple machine learning models.",
        "Evaluate the system using more extensive real-world data."
    ]
}