Guest_list = ["mother", "father", "sister", "friend"]

print(f"hello {Guest_list[0].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[1].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[2].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[3].title()}, would you like to come to dinner?")

print(f"Guest {Guest_list[0].title()} cannot make the dinner")
Guest_list[0] = "brother"

print(f"hello {Guest_list[0].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[1].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[2].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[3].title()}, would you like to come to dinner?")

print("hello everyone, i found a bigger dinner table")

Guest_list.insert(0,"gabe")
Guest_list.insert(2, "ramzi")
Guest_list.append("Harit")

print(f"hello {Guest_list[0].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[1].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[2].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[3].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[4].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[5].title()}, would you like to come to dinner?")
print(f"hello {Guest_list[6].title()}, would you like to come to dinner?")

print(f"sorry guys i can only invite 2 ppl to dinner")
Harit = Guest_list.pop(6)
print(f"sorry {Harit}, i cant invite you to dinner")
friend = Guest_list.pop(5)
print(f"sorry {friend}, i cant invite you to dinner")
sister = Guest_list.pop(4)
print(f"sorry {sister}, i cant inite you to dinner")
father = Guest_list.pop(3)
print(f"sorry {father}, i cant invite you to dinner")
ramzi = Guest_list.pop(2)
print(f"sorry {ramzi}, i cant invite you to dinner")

print(f"hey {Guest_list[0].title()} and {Guest_list[1].title()}, you two are still invited")
del Guest_list[1]
del Guest_list[0]

print(Guest_list)




