import requests

test_problems = [
    "I am stressed about money",
    "My friend betrayed my trust and I don't know what to do",
    "I failed an important exam and feel like giving up",
]

for problem in test_problems:
    response = requests.post(
        "http://127.0.0.1:5000/ask",
        json={"message": problem}
    )
    result = response.json()
    print(f"\n{'='*50}")
    print(f"PROBLEM: {result['your_problem']}")
    print(f"{'='*50}")
    print(f"FILMY DIDI: {result['filmy_didi_says']}")