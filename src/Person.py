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
        filePath = "../db/Person/"
        os.chdir(filePath) 
        f = open(fileName, "w")
        f.write(self.personContent)
        f.write("\n\n@2021 All Rights Reserved Emin K & Asya B")
        f.close()
    # burada sorun şu ben Person.py dosyasındayım ve "path" dediğim şey :D  aynen bi dizin çıkmam lazım iki nokta koyarsan bi üst dizine çıkar
    # sonra da orada db diye bir yer arar :ok
    

       




## DRIVER PROGRAM
person1 = Person(1,"Emin","Kartci","Male",21)
person1.save_person_txt()
person2 = Person(2,"Asya","Bostaoğlu","Female",20)
person2.save_person_txt()