class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for i, question in enumerate(self.questions, 1):
            user_answer = input(question.prompt + "\nYour Answer: ")
            if user_answer.lower() == question.answer.lower():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            print("Your current score: {}/{}\n".format(self.score, i))
        print("Quiz completed! You scored {}/{}.".format(self.score, len(self.questions)))


def main():
    question_prompts = [
        "What is the capital of France?\n(a) Paris\n(b) Madrid\n(c) Rome\n\n",
        "What is 7 x 3?\n(a) 21\n(b) 24\n(c) 27\n\n",
        "Who is the author of 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n\n"
    ]

    # Update correct answers for each question
    correct_answers = ["a", "a", "a"]

    questions = [
        Question(question_prompts[0], correct_answers[0]),
        Question(question_prompts[1], correct_answers[1]),
        Question(question_prompts[2], correct_answers[2])
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()
if __name__ == "__main__":
    main()  
