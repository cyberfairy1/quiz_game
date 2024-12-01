class QuizBrain:

    def __init__(self, question_list):
        """
        Initialize the QuizBrain with a list of questions.
        """
        self.current_question_index = 0
        self.score = 0
        self.question_list = question_list

    def has_more_questions(self):
        """
        Check if there are more questions left in the quiz.
        """
        return self.current_question_index < len(self.question_list)

    def ask_next_question(self):
        """
        Present the next question to the user and check their answer.
        """
        current_question = self.question_list[self.current_question_index]
        self.current_question_index += 1
        user_input = input(
            f"Q.{self.current_question_index}: {current_question.text} (True/False): "
        )
        self.evaluate_answer(user_input, current_question.answer)

    def evaluate_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer matches the correct answer.
        """
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            print("🎉 Correct! Great job!")
        else:
            print("❌ Oops! That's not right.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score so far: {self.score}/{self.current_question_index}")
        print("-" * 40)  # Separator for clarity in the console





