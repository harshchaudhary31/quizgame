import random

def load_questions():
    return [
        {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"], "answer": "A"},
        {"question": "What is 5 + 3?", "options": ["A. 5", "B. 8", "C. 10", "D. 15"], "answer": "B"},
        {"question": "Which programming language is this quiz written in?", "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"], "answer": "B"}
    ]

def main():
    questions = load_questions()
    random.shuffle(questions)
    score = 0

    for q in questions:
        print(f"\n{q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()

