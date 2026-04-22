# Sidemen Charity Match Quiz Program

quiz_questions = {
    "Who is the all‑time top goalscorer in the Sidemen Charity Match?": ["Miniminter", "Simon"],
    "How much money has the Sidemen Charity Match raised in total (to the nearest million £)?": "15",
    "What year was the first Charity Match?": "2016",
    "Where was the most recent charity match held?": "Wembley",
    "Which team has the most total wins?": "Sidemen"
}


def welcome():
    print("Welcome to the Sidemen Charity Match Quiz!")
    name = input("What is your name? ")
    print(f"Great to have you here, {name}!")
    return name


def ask_question(question, correct_answer):
    user_answer = input(f"\n{question}\nYour answer: ").strip().lower()


    if isinstance(correct_answer, list):
        valid = [ans.lower() for ans in correct_answer]
        if user_answer in valid:
            print("Correct!")
            return True
        else:
            print(f"Incorrect, the answers were: {', '.join(correct_answer)}")
            return False
        
    if user_answer == str(correct_answer).lower():
        print("Correct! Nice one.")
        return True
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
        return False



def show_results(score, total, name):
    percentage = (score / total) * 100
    print("\n--- QUIZ RESULTS ---")
    print(f"{name}, you scored {score} out of {total}.")
    print(f"Your percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Outstanding! You're a Sidemen Charity Match expert!")
    elif percentage >= 60:
        print("Great job! You know your stuff.")
    else:
        print("Keep learning! You'll smash it next time.")


def main():
    name = welcome()
    score = 0
    total_questions = len(quiz_questions)

    for question, answer in quiz_questions.items():
        if ask_question(question, answer):
            score += 1

    show_results(score, total_questions, name)


if __name__ == "__main__":
    main()
