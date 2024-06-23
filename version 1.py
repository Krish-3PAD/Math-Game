from tkinter import*
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Math Game")

headingLabel = Label(root, text= "Math Game", font = ("arial" , 20))
headingLabel.grid(row=0 , column = 0)

number1 = randint(1 , 10)
number2 = randint(1 , 10)

question = str(number1) +  "+" + str(number2)
answer = number1 + number2
def checkAnswer():
    if str(answer) == givenAnswer.get():
        print("Correct!")
    else:
        print ("wrong mate")



givenAnswer = StringVar()
   
        # User Interface

questionLabel = Label(root, text = question ,  font = ("arial" , 20))
questionLabel.grid( row = 1, column =0)

answerEntry = Entry(root, textvariable=givenAnswer , font= ('arial' , 20))
answerEntry.grid (row = 2 , column =0 )

submitButton = Button(root, text = "Submit" , font =("arial", 20), command= checkAnswer)
submitButton.grid(row = 2, column = 1)

print(question)
print(answer)


root.mainloop()