# import os library 
import os 

class Community:

    # construction
    def __init__(self,id,title,location,population,religion):
        self.id         = id
        self.title      = title
        self.location   = location      
        self.population = population    # Population Amount
        self.people     = []            # People Objects
        self.religion   = religion      # Religion String -> Will be an object in future
        self.print_community_console()                 # after initializing the object print to the screen
        self.save_community_txt()                      # after initializing the object save it automatically 

    # add a person to people array list
    def add_person(self,person):
        # append people
        self.people.append(person)
        # inform the user
        print(f"{person.name} is appended to {self.title} successfully !")


    # print object to the screen
    def print_community_console(self,willPrint = True):

        # initialize a string
        self.communityContent = f"""
------ community {self.id} ------
| Title         : {self.title}
| Location      : {self.location}
| Population    : {self.population}
| Religion      : {self.religion}
        """

        # deafult value -> true
        # if it is specified don't print
        if willPrint:
            print(self.communityContent)
        
    # save object as txt file
    def save_community_txt(self):
        # file name -> id_name.txt
        fileName = str(self.id)+"_"+self.title+".txt"
        # path -> db -> community 
        filePath = os.getcwd()+"/db/Community/"

        # open a txt file
        f = open(filePath + fileName, "w")

        # write the content
        f.write(self.communityContent)

        # Write your rights
        f.write("\n\n@2021 All Rights Reserved Emin K & Asya B")

        # Close the file
        f.close()
    
    # read a community object from a txt file
    def read_community_txt(id,title):

        # file name -> id_name.txt
        fileName = str(id)+"_"+title+".txt"
        # path -> db -> community 
        filePath = os.getcwd()+"/db/Community/"
        # open the file
        f = open(filePath+fileName, "r")

        # read whole file
        currentcommunityContent = f.read()

        # Split the string by referring the : sign
        contentArr = currentcommunityContent.split(":")

        # ignore the first part beacuse we don't need it
        contentArr = contentArr[1:]

        # initialize a list
        communityInfo = []

        # for each element 
        for line in contentArr:
            # Split the string by referring the next line
            lineArr = line.split("\n")

            # append the list
                # get the 0 index and clear the space
            communityInfo.append(lineArr[0].lstrip())
        
        # create a new object by using the parameters
                        #     id  name          surname       gender        age
        currentcommunity = Community(id,communityInfo[0],communityInfo[1],communityInfo[2],communityInfo[3])
