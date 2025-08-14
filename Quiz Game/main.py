def run_quiz(questions):
    score = 0
    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")


        user_input = input("Enter the number of your answer: ")

        try:
            user_choice_index = int(user_input) - 1
            if 0 <= user_choice_index and options[user_choice_index] == correct_answer:
                print("Correct!\n")
                score +=1
            else:
                print(f"Incorrect. The correct answer was: {correct_answer}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
        except IndexError:
            print("Invalid option number. Please try again\n")
    print(f"Quiz completed! Your final score is: {int((score/len(questions))* 100)}%")


quiz_questions = [
    {
        "question": "Worse PM ever after Independence? ",
        "options": ["Jawal lal nehru", "Narendra modi", "Indira Gandhi", "Manmohan singh" ],
        "correct_answer": "Narendra modi"
    },
    {
        "question": "Which country has the highest nuclear weapons ?",
        "options" : ["Russia", "America", "United Kindom", "France"],
        "correct_answer": "Russia"
    },
    {
        "question": "Which country GDP is the highest GPD? ",
        "options": ["India", "America", "China", "Japan"],
        "correct_answer": "America"
    },
    {
        "question": "What is the square root of  19? ",
        "options": ["361", "200", "350", "150"],
        "correct_answer": "361"
    }
]

print("Welcome to the python Quiz Game!\n")
run_quiz(quiz_questions)