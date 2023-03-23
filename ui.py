from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(pady=30, padx=30, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   width=280,
                                                   text=f"some text",
                                                   fill=THEME_COLOR,
                                                   font=("arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image,
                                  highlightthickness=0,
                                  command=self.true_clicked)
        self.true_button.grid(column=0, row=3)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image,
                                   highlightthickness=0,
                                   command=self.false_clicked)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"you have reached the end of the quiz"
                                                          f"\nyour score is {self.quiz.score} ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        correct = self.quiz.check_answer("true")
        self.feedback(correct)

    def false_clicked(self):
        correct = self.quiz.check_answer("false")
        self.feedback(correct)

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)