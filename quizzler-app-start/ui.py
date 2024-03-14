import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Some Question Text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        rightphoto = tkinter.PhotoImage(file= r"images\true.png")
        wrongphoto = tkinter.PhotoImage(file=r"images\false.png")
        self.rightbutton = tkinter.Button(image=rightphoto, highlightthickness=0, command=self.true_pressed)
        self.wrongbutton = tkinter.Button(image=wrongphoto, highlightthickness=0, command=self.false_pressed)
        self.rightbutton.grid(column=0, row=2)
        self.wrongbutton.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.rightbutton.config(state="disable")
            self.wrongbutton.config(state="disable")

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
        self.window.after(1000, self.get_next_question)


