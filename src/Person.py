# import os library 
import os 

class Person:

    def __init__(self,id,name,surname,gender,age):
        self.id = id
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.personContent = ""
        self.print_person_console()


    def print_person_console(self,willPrint = True):
        self.personContent = f"""
------ PERSON {self.id} ------
| Name      : {self.name}
| Surname   : {self.surname}
| Gender    : {self.gender}
| Age       : {self.age}
        """

        if willPrint:
            print(self.personContent)
        
    def save_person_txt(self):
        fileName = str(self.id)+"_"+self.name+".txt"
        print(os.getcwd())
        filePath = os.getcwd()+"/db/Person/"
        f = open(filePath + fileName, "w")
        f.write(self.personContent)
        f.write("\n\n@2021 All Rights Reserved Emin K & Asya B")
        f.close()
    
    def read_person_txt(id,name):
        fileName = id+"_"+name
        f = open(os.getcwd() +"/db/Person/"+fileName+".txt", "r")
        currentPersonContent = f.read()

        contentArr = currentPersonContent.split(":")
        contentArr = contentArr[1:]

        personInfo = []

        for line in contentArr:
            lineArr = line.split("\n")
            personInfo.append(lineArr[0].lstrip())

        currentPerson = Person(id,personInfo[0],personInfo[1],personInfo[2],personInfo[3])
        

       




## DRIVER PROGRAM

Person.read_person_txt("1","Emin")