# import os library 
import os 

class Person:

    # construction
    def __init__(self,id,name,surname,gender,age):
        self.id             = id
        self.name           = name
        self.surname        = surname
        self.gender         = gender
        self.age            = age
        self.personContent  = ""                     # to print & save the parameters of the object
        self.print_person_console()                 # after initializing the object print to the screen
        self.save_person_txt()                      # after initializing the object save it automatically 

    # print object to the screen
    def print_person_console(self,willPrint = True):

        # initialize a string
        self.personContent = f"""
------ PERSON {self.id} ------
| Name      : {self.name}
| Surname   : {self.surname}
| Gender    : {self.gender}
| Age       : {self.age}
        """

        # deafult value -> true
        # if it is specified don't print
        if willPrint:
            print(self.personContent)
        
    # save object as txt file
    def save_person_txt(self):
        # file name -> id_name.txt
        fileName = str(self.id)+"_"+self.name+".txt"
        # path -> db -> Person 
        filePath = os.getcwd()+"/db/Person/"

        # open a txt file
        f = open(filePath + fileName, "w")

        # write the content
        f.write(self.personContent)

        # Write your rights
        f.write("\n\n@2021 All Rights Reserved Emin K & Asya B")

        # Close the file
        f.close()
    
    # read a person object from a txt file
    def read_person_txt(id,name):

        # file name -> id_name.txt
        fileName = str(id)+"_"+name+".txt"
        # path -> db -> Person 
        filePath = os.getcwd()+"/db/Person/"
        # open the file
        f = open(filePath+fileName, "r")

        # read whole file
        currentPersonContent = f.read()

        # Split the string by referring the : sign
        contentArr = currentPersonContent.split(":")

        # ignore the first part beacuse we don't need it
        contentArr = contentArr[1:]

        # initialize a list
        personInfo = []

        # for each element 
        for line in contentArr:
            # Split the string by referring the next line
            lineArr = line.split("\n")

            # append the list
                # get the 0 index and clear the space
            personInfo.append(lineArr[0].lstrip())
        
        # create a new object by using the parameters
                        #     id  name          surname       gender        age
        currentPerson = Person(id,personInfo[0],personInfo[1],personInfo[2],personInfo[3])