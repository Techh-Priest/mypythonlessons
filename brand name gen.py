#Where did the word debugging come from? A moth flew into one of the early computers in the 1980s.
#into the computer and get rid of the moth hence debugging a literal bug.

#Variable naming rules= make your code readable. If a variable has two names you have to use and underscore e.g
#user_name. Also you can also use numbers e.g name1,

name = input("Welcome to the Brand Name Generator.\nHello! What is your name?\n")
city = input("Hello " + name + "." + " Which city did you grow up in?\n")
pet = input("Nice! What's your pet's name?\n")
print("Your brand name can be " + city + pet)