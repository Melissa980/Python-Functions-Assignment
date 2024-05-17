# Question 4 Task 1
questions_answers = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What color is the sky on a sunny day?": "Blue",
    "How many legs does a cat have?": "Four",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Question 4 Task 2
def quiz():
    score = 0
    for question, answer in questions_answers.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    return score

# Question 4 Task 3
def score_quiz(score):
    total_questions = len(questions_answers)
    percentage = (score / total_questions) * 100
    if percentage >= 70:
        print(f"You scored {score}/{total_questions}. Great job!")
    else:
        print(f"You scored {score}/{total_questions}. You can do better next time.")
