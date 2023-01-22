from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # passing quiz-brain as input to output it in the main.py and initialize it in the function...when initialize a
    # quizinterface then we must pass in quiz_brain object which is of datatype QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        check_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        # since working in classes...have to add self to command method
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.check_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    # passing in quiz and attaching next question when interface is initialized...tapping into the canvas so the
    # next questions can go into the canvas
    def get_next_question(self):
        # making sure the canvas turns back to white after each question
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # replacing the score_label with the quiz.score which will calculate the number or right answers which goes
            # back to the check_answer method where the score is added if user gets it right
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            # calling itemconfig to add q_text to question_text aka the canvas text
            self.canvas.itemconfig(self.question_text, text=q_text)
        # changing the question_text to tell user they reached the end of the quiz and disabling the buttons so user
        # can't keep pressing the buttons after quiz is done
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    # calling check_answer method from quiz_brain.py and telling which one is true or false based on the button pushed
    # by going into the method to see if correct answer == user answer
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # creating a new method to figure out if whichever button pushed answers the question of the variable is_right
    def give_feedback(self, is_right):
        # saying if is_right is true then change background color to green or red if false...this gives user feedback
        # whether they got it right or wrong...because we call next question after 1 sec the canvas turns back to white
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
