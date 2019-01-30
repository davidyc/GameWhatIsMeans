# блок  подключений 
from tkinter import *
import pyodbc
import random




# описание всех функции для работы
def Answer(root, bool):   
    clear(root)
    btn = Button(root, text="next", fg="white",  bg="#FF4500", command= lambda: NextQuetion(root))

    if bool == True:
        countAnswer = Label(fg="green", bg="black", justify="center", text="Верно", font=72)        
    else:
        countAnswer = Label(fg="red", bg="black", justify="center", text="Не верно", font=72)

    btn.grid(row=1, column=0)
    countAnswer.grid(row=0, column=0, columnspan=3)

def clear(root):
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    
def NextQuetion(root):    
    tion = GetCorrectWord()      
    UIMenu(root, tion)

def ConnectToDataBase():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=WhatIsmeans;Trusted_Connection=yes;')
    return cnxn.cursor()

def GetCountWord():
    cursor = ConnectToDataBase()
    cursor.execute("select count(*) from words")
    res =  cursor.fetchone()
    return res[0]

def GetCorrectWord():
    cursor = ConnectToDataBase()
    numberRandom = random.randint(1,GetCountWord()-1)
    words = cursor.execute("select id, correctanswer, englishdefinition, englishword  from Words where id = {0}"
                           .format(numberRandom))    
    que = []
    uncorretAnswer = GetIncorrectWord(numberRandom)
    print("UNCORaNS {0}".format(uncorretAnswer))
   
    for word in words:           
        que.append(str(word[0]))
        que.append(str(word[1]))
        que.append(str(word[2]))
        que.append(str(word[3]))
        que += uncorretAnswer       
    return que
  
def GetIncorrectWord(currextNum):
    cursor = ConnectToDataBase()
    i = 0
    string = []
    while(i<3):
        numberRandom = random.randint(1,GetCountWord()) #изменить 
        if(currextNum == numberRandom):
            numberRandom+=1    
        word = cursor.execute("select englishword from Words where id = {0}".format(numberRandom))         
        for item in word:
            string.append(str(item[0]))  
        i+=1
    return string

def UIMenu(root, quest):   
    clear(root)   
# инициализация все компонетов    
    queshtionLabel = Label(text=quest[2], fg="white", bg="black", justify="center", bd=5)
    btnAnswer1 = Button(root,text=quest[3], width=28, height=2, fg="white", bg="#FF4500", 
                    command=lambda: Answer(root, True))
    btnAnswer2 = Button(root,text=quest[4], width=28, height=2, fg="white", bg="#FF4500",
                   command=lambda: Answer(root, False))
    btnAnswer3 = Button(root,text=quest[5], width=28, height=2, fg="white", bg="#FF4500",
                   command=lambda: Answer(root, False))
    btnAnswer4 = Button(root,text=quest[6], width=28, height=2, fg="white", bg="#FF4500", 
                    command=lambda: Answer(root, False))
  


# расположение эдементов в окне
    queshtionLabel.grid(row=0, column=0, columnspan=2)

    sortBtn = ([2,0],[2,1],[3,0],[3,1])
   
    counter = 0
    while(counter<4):
        number = random.randint(1,10)
        sortBtn[counter].append(number)
        counter+=1
    print(sortBtn)
  
    counter = 0
    while(counter<4):
         counterTwo = 0
         while(counterTwo<4):
            if sortBtn[counter][2] <= sortBtn[counterTwo][2]:
                tmprow = sortBtn[counter][0]              
                tmpcol = sortBtn[counter][1]
                tmran = sortBtn[counter][2]
                sortBtn[counter][0] = sortBtn[counterTwo][0]              
                sortBtn[counter][1] = sortBtn[counterTwo][1]
                sortBtn[counter][2] = sortBtn[counterTwo][2]
                sortBtn[counterTwo][0] = tmprow              
                sortBtn[counterTwo][1] = tmpcol
                sortBtn[counterTwo][2] = tmran                
            counterTwo+=1
         counter+=1
    


    btnAnswer1.grid(row=sortBtn[0][0], column=sortBtn[0][1])
    btnAnswer2.grid(row=sortBtn[1][0], column=sortBtn[1][1])
    btnAnswer3.grid(row=sortBtn[2][0], column=sortBtn[2][1])
    btnAnswer4.grid(row=sortBtn[3][0], column=sortBtn[3][1])




# Блок инициализации окна
root=Tk()
root.geometry("400x170")
root.title("What is mean?")
root.configure(bg="black")



queshtion = GetCorrectWord()
UIMenu(root, queshtion)

  

# цикл чего то там
root.mainloop()