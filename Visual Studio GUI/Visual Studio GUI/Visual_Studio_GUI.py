from tkinter import *
from tkinter import messagebox
import random
root = Tk()

def Create_Window():
    create_window = Toplevel(root)
    create_window.title("Problems")
    create_window.geometry("666x666+0+0")
    answer = StringVar (create_window)
    answer_label = Label(create_window, text = "Enter your answer here").place(x = 300, y = 400)
    answer_entry = Entry(create_window)
    answer_entry.place(x = 300, y = 425)

 
    type_of_math = ["+", "-", "*", "/"]
    i = 1
    index = 100 #only one coordinate can change -- and that would be the y coordinate for the equations to be below the previous
    while i < 5:     

        var1 = random.randrange(0, 999)
        var2 = random.randrange(0, 999)

        plus_or_minus = (random.choice(type_of_math))
        question_label = Label(create_window, text = (str(var1) + "  " + plus_or_minus + " " + str(var2))).place(x = 333, y = index) 

        print(var1)
        print(var2)
        print(plus_or_minus)
        index += 50 # add fifty to the index of y to move the next equation to below the previous
        i += 1
        

    # setting up the equation labels
    # ---- align the equations with the answer boxes
   

root.title("Welcome to Math")
root.geometry("666x666+0+0")
button = Button(root,
                text = "Press me to begin",
                command = Create_Window)




button.pack()
root.mainloop()
