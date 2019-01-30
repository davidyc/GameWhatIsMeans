import pyodbc
import random


def ConnectToDataBase():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=WhatIsmeans;Trusted_Connection=yes;')
    return cnxn.cursor()


def GetIncorrectWord(currextNum):
    cursor = ConnectToDataBase()
    i = 0
    string = []
    while(i<3):
        numberRandom = random.randint(1,3)
        if(currextNum == numberRandom):
            numberRandom+=1
    
        word = cursor.execute("select russianword from Words where id = {0}".format(numberRandom))    
      
        for item in word:
            string.append(str(item[0]))           

        i+=1

    return string

def GetCountWord():
    cursor = ConnectToDataBase()
    cursor.execute("select count(*) from words")
    res =  cursor.fetchone()
    return res[0]


print(GetAllWords())