import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(
            text="Score: 0",
            font=("Arial", 12, "bold"),
            fg="#FFFFFF", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=290,
            text="big booty bitches",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        x_image = tkinter.PhotoImage(file="images/false.png")
        self.x_button = tkinter.Button(image=x_image, highlightthickness=0, command=self.false_pressed)
        self.x_button.grid(column=1, row=2)

        y_image = tkinter.PhotoImage(file="images/true.png")
        self.y_button = tkinter.Button(image=y_image, highlightthickness=0, command=self.true_pressed)
        self.y_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.x_button.config(state="disabled")
            self.y_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
