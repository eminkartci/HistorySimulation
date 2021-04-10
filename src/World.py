
# import classes
from Community import  Community
from Person import  Person




class World:

    def __init__(self):
        self.people     = []
        self.communities = []

    # This function interacts with the user
        # automatic ID
        # Get other parameters
        # Create Community
        # Save Community
        # Add Community to class list
    def create_community(self):
        current_id = len(self.communities) + 1
        print("Community Creating...")
        title = input("Title: ")
        location = input("Location: ")
        population = int(input("Population: "))
        religion = input("Religion: ")
        Current_Community = Community(current_id, title, location, population, religion)
        self.communities.append(Current_Community)

        for i in range(population):
            self.create_person()

    def create_person(self):
        current_id = len(self.people) + 1
        print("Person Creating...")
        name = input("Name: ")
        surname = input("Surname: ")
        gender = input("Gender: ")
        age = input("Age: ")
        Current_Person = Person(current_id, name, surname, gender, age)
        self.people.append(Current_Person)

        

world1 = World()
world1.create_community()
#world1.create_person()

####### MANUEL CODE ########
# # Create a Community
# TurkCommAsia = Community(1,"Turk","Turkey - Asia",340,"Muslim")
# TurkCommEuro = Community(1,"Turk","Turkey - Europe",240,"Muslim")

# # Create Some People
# P1 = Person(1,"Emin","Kartci","Male",21)
# P2 = Person(1,"Asya","Bostanoglu","Female",20)

# Somehow we need to connect people and community
# TurkCommEuro.add_person(P1)
