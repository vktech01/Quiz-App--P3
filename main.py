def run_quiz():
    questions = [
        {
            "question": "Who made the Python programming language?",
            "options": ["A) Guido van Rossum", "B) Elon Musk", "C) Bill Gates", "D) Mark Zuckerberg"],
            "answer": "A) Guido van Rossum"
        },
        {
            "question": "Which library is used for data manipulation and analysis in Python?",
            "options": ["A) NumPy", "B) Pandas", "C) Matplotlib", "D) Seaborn"],
            "answer": "B) Pandas"
        },
        {
            "question": "Which Python library is used for data visualization?",
            "options": ["A) Pandas", "B) NumPy", "C) Matplotlib", "D) SciPy"],
            "answer": "C) Matplotlib"
        },
        {
            "question": "Which are global SQL databases?",
            "options": ["A) MySQL", "B) PostgreSQL", "C) SQLite", "D) All of the above"],
            "answer": "D) All of the above"
        },
    ]

    score = 0   # ✅ correct place

    for index, q in enumerate(questions):
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ")

        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    print(f"Your final score is {score}/{len(questions)}")


run_quiz()
