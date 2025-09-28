#Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again.

#add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again.

#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business.
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



Rest1 = Restaurant("mcdonalds", "fast food")
print(Rest1.number_served)
Rest1.set_number_served(40)
print(Rest1.number_served)
Rest1.increment_number_served(50)
print(Rest1.number_served)




#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called 
# reset_login_attempts() that resets the value of login_attempts to 0.

#Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make
#  sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, uid, group):
        self.first = first_name
        self.last = last_name
        self.uid = uid
        self.group = group
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"here is a summary of your user: ")
        print(f"\t{self.first}")
        print(f"\t{self.last}")
        print(f"\t{self.uid}")
        print(f"\t{self.group}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attemps = 0


    def greet_user(self):
        print(f"hello {self.first} {self.last}, i would you're having a wonderful day")