
# import classes
from Community import  Community
from Person import  Person




class World:

    def __init__(self):
        persons     = []
        communities = []

    # This function interacts with the user
        # automatic ID
        # Get other parameters
        # Create Community
        # Save Community
        # Add Community to class list
    def create_community(self):
        print("Community Creating...")

world1 = World()
world1.create_community()

####### MANUEL CODE ########
# # Create a Community
# TurkCommAsia = Community(1,"Turk","Turkey - Asia",340,"Muslim")
# TurkCommEuro = Community(1,"Turk","Turkey - Europe",240,"Muslim")

# # Create Some People
# P1 = Person(1,"Emin","Kartci","Male",21)
# P2 = Person(1,"Asya","Bostanoglu","Female",20)

# Somehow we need to connect people and community
# TurkCommEuro.add_person(P1)
