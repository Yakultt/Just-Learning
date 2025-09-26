#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
# using a different number of arguments each time.


def sandwich(*items):
    for i in items:
        print(f"you want {i} on your sandwich, nice!")

print(sandwich("mustard", "ketchup", "onion", "lettuce"))
print(sandwich("ham"))
print(sandwich("roast beef", "ketchup"))


#User Profile: Start with a copy of user_profile.py from page 148. Build a profile of yourself by calling build_profile(),
#  using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

person = build_profile("harit", "sook", major="cyber", fav_food = "burger", dog="mochi" )
print(person)

#Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, 
# such as a color or an optional feature. Your function should work for a call like this one:
def car(manufacturer, model, **kwargs):
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs

example = car("subaru", "wrx", electric = "no", expensive = "yes")
print(example)