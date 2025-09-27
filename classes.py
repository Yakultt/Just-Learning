#Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information
# , and a method called open_restaurant() that prints a message indicating that the restaurant is open.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print(f"here is your resturant name {self.name}")
        print(f"and here is the cuisine type {self.cuisine_type}")


Rest1 = Restaurant("mcdonalds", "fast food")
print(Rest1.name)
print(Rest1.cuisine_type)
Rest1.describe_resturant()

#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes 
# that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

#Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, uid, group):
        self.first = first_name
        self.last = last_name
        self.uid = uid
        self.group = group
    
    def describe_user(self):
        print(f"here is a summary of your user: ")
        print(f"\t{self.first}")
        print(f"\t{self.last}")
        print(f"\t{self.uid}")
        print(f"\t{self.group}")

    def greet_user(self):
        print(f"hello {self.first} {self.last}, i would you're having a wonderful day")
    

user1 = User("harit", "sook", 2000, "harit")
user1.describe_user()
user1.greet_user()