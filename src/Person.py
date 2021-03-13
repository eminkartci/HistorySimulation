

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




## DRIVER PROGRAM
person1 = Person(1,"Emin","Kartci","Male",21)
person2 = Person(2,"Asya","Bostaoğlu","Female",20)