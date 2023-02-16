from tkinter import *
import API_Request as API
import html

class UI:
    def __init__(self):
        self.api = API.QuizApi()
        self.window = Tk()
        self.window.config(background="#375362",padx=50)
        self.window.minsize(width=400, height=500)
        self.questions_asked=0
        self.score=0
        self.score_label = Label(text=f"Score:{self.score} / {self.questions_asked}", background="#375362" ,font=("Arial",12 ,"bold") , highlightcolor="white",foreground="white" )
        self.canvas = Canvas(width=300, height=400, background="white")
        self.currentQuestion = self.api.randomQuestion()
        question= html.unescape(self.currentQuestion["question"])
        self.question_text = self.canvas.create_text(150, 200, text=question ,width=200, font=("Arial",16 , "bold"))
        correct_image = PhotoImage(file="images/true.png")
        incorrect_image=PhotoImage(file="images/false.png")
        correct_button= Button(image=correct_image ,highlightthickness=0 , command=self.trueAnswer)
        incorrect_button = Button(image=incorrect_image, highlightthickness=0 , command=self.falseAnswer)

        self.score_label.grid(column=1 , row=0 , pady=20)
        self.canvas.grid(column=0,row=1 ,columnspan=2)
        correct_button.grid(row=2, column=0 ,pady=20)
        incorrect_button.grid(row=2,column=1)

        self.window.mainloop()

    def nextQuestion(self):
        self.currentQuestion = self.api.randomQuestion()
        question = html.unescape(self.currentQuestion["question"])
        self.canvas.itemconfig(self.question_text,text= question)
        self.canvas.configure(bg="white")

    def trueAnswer(self):
        self.questions_asked+=1
        if self.currentQuestion["correct_answer"] == "True":
            self.score+=1
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000,self.nextQuestion)
        self.score_label.config(text=f"Score:{self.score}/{self.questions_asked}")

    def falseAnswer(self):
        self.questions_asked += 1
        if self.currentQuestion["correct_answer"] == "False":
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.nextQuestion)
        self.score_label.config(text=f"Score:{self.score}/{self.questions_asked}")

