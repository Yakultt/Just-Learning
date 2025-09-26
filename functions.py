#City Names: Write a function called city_country() that takes in the name of a city and its country. T
# the function should return a string 
#formatted like this:

#"Santiago, Chile"
#Call your function with at least three city-country pairs, and print the values that are returned.

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
#The function should take in an artist name and an album title, and it should return a dictionary containing 
#these two pieces of information. Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the dictionaries are storing the album information correctly.

#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
#  If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
#  Make at least one new function call that includes the number of songs on an album.


#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to 
# enter an album’s artist and title. Once you have that information, call make_album() with the user’s input 
# and print the dictionary that’s created. Be sure to include a quit value in the while loop.


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))
print(city_country("melbourne", "australia"))
print(city_country("new york", "United states of america"))

def make_album(name, title, songs=None): 
    album = {
        "name" : name,
        "title" : title
    }
    if songs:
        album["number of songs"] = songs
    return album

print(make_album("alice phoebe loue", "hammer"))

while True:
    print(f"please enter an artists name and their album!")
    print(f"press q to quit anytime")

    name = input("please enter the artists name: ")
    if name == 'q':
        break

    title = input("please enter the title: ")
    if title == 'q':
        break
    value = make_album(name, title)
    print(f"here is your dictionary!")
    print(value)


