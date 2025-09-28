#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that 
# inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of 
# the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
#  Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_resturant(self):
        print(f"here is your resturant name {self.name}")
        print(f"and here is the cuisine type {self.cuisine_type}")
    
    def set_number_served(self, value):
        self.number_served = value

    def increment_number_served(self,increment_number):
        self.number_served += increment_number

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['Vanilla', "chocolate", "pistachio"]

    def display_flavors(self):
        print(f"here are the current ice cream flavors we have!: ")
        for i in self.flavors:
            print(f"\t{i}")



ice1 = IceCreamStand("ben and jerries", "ice cream")



#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the
# User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges,
#  that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
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

class admin(User):
    def __init__(self, first_name, last_name, uid, group):
        super().__init__(first_name, last_name, uid, group)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"here are the current priveleges the admin has")
        for i in self.privileges:
            print(f"\t{i}")


user1 = admin("harit", "sook", 120, "admin")
user1.show_privileges()

