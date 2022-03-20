
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label()
        self.label.config(text="Score:0", fg="white", bg=THEME_COLOR,font=("Ariel", 20))
        self.label.grid(column=1, row=0)
        # self.label.itemconfig(text=f"Score:{QuizBrain.check_answer}")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(150,125, width=250,text="test", fill=THEME_COLOR, font=("Ariel", 20))
        self.canvas.grid(column=0, row=1,columnspan=2,pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_img,command=self.user_false)
        self.button_false.grid(column=1, row=2)


        true_img = PhotoImage(file="images/true.png")
        self.button_true=Button(image=true_img,command=self.user_true)
        self.button_true.grid(column=0, row=2)



        self.get_next_question()



        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"This is the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    def user_false(self):
        # self.user_answer="False"
        is_correct=self.quiz.check_answer("False")
        self.feed_back(is_correct)

    def user_true(self):
        is_correct=self.quiz.check_answer("True")
        self.feed_back(is_correct)


    def feed_back(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")


        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)














