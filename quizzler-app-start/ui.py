from tkinter import *
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text='question',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, columnspan=2, row=1, padx=50, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button()
        self.true_button.config(image=true_img, command=self.pressed_true)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button()
        self.false_button.config(image=false_img, command=self.pressed_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n"
                                                            f"Your final score was: {self.quiz.score}/"
                                                            f"{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def pressed_true(self):
        is_right = self.quiz.check_answer('True')
        self.get_feedback(is_right)

    def pressed_false(self):
        is_right = self.quiz.check_answer('False')
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            color = 'green'
        else:
            color = 'red'
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)

