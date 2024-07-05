#Now let's build a Love Calculator!

print("Welcome to the Love Calcutaor!")
name1 = input("What is your name?\n")
name2 = input("What is their name\n")
#TRUE LOVE
first_name = name1.lower()
second_name = name2.lower()

combined_names = first_name + second_name
name= combined_names.lower()
tru = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

combined_score =  str(tru) + str(love)
percentage = int(combined_score)

if percentage <= 10 or percentage >= 90:
    print(f"Your score is {percentage}%. You go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}%. You are alright together.")
else:
    print(f"Your love score is {percentage}%.")