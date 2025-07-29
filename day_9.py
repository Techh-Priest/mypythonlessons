        #Python Dictionaries, Nesting Lists & how to combine them.

        #Dictionaries in Python also work kind of similarly like in real life.
    # Every word is a Key(word to be searched) and it has a value(definition of word)
    #The Key and the Value are both strings
    # A dictionary can also have more than one entry.
#programming_dictionary = {
#    "Bug": "An error in a program that prevents the program from running as expected.",
#    "Function": "A piece of code that can easily call repeatedly."
#}

    #Now, what if we wanted to retrieve something inside the dictionary?
#print(type("An error in a program that prevents the program from running as expected."))

    #Now, what if you wanted to add a piece of data to the dictionary?
#programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

    #Now, its helpful to start out with an empty dictionary when starting a project.
    #You can create an empty dictionary the same way you do with lists.
#empty_dictionary = {}
#empty_dictionary["Loop"] = "The action of doing something over and over again."
#print(empty_dictionary)

    #To wipe an entire dictionary:
#programming_dictionary = {}
#print(programming_dictionary)

    #To edit an item in the dictionary:
#programming_dictionary["Bug"] = "An moth in your PC, lol!!."
#print(programming_dictionary)

    #How to loop through the dictionary
#for thing in programming_dictionary:
#    print(thing)

#The code below prints the keys only:
#for key in programming_dictionary:
#    print(programming_dictionary[key])

        #Nesting
    #Now, you can store a list within a key in the dictionary and also store a dictionary
    # within the dictionary as seen in the crude example below:
#example = {"key": "[List]",
#           "key2": "{Dictionary}"
#        }
    # Here is a credible example
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
#
#     #Nesting a list in a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"]
#     "Germany": ["Berlin", "Stuttgart", "Hamburg"]
# }
#
#     #You can also nest a list within a list:
# ["A", "B", ["C", "D"]]
#
#     #Nesting a dictionary within a dictionary:
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Stuttgart", "Hamburg"], "total_visits": 5},
# }

    # Now nesting a dictionary inside a list:
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
#         "total_visits": 5}
# ]

            #Dictionary in List Exercise

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
#         "total_visits": 5}
# ]
#
# def add_new_country(country_visited, cities, times_visited):
#             new_entry= {}
#             new_entry["country"] = country_visited
#             new_entry["cities_visited"] = cities
#             new_entry["total_visits"] = times_visited
#             travel_log.append(new_entry)
#
#     # Now, its helpful to start out with an empty dictionary when starting a project.
#     # You can create an empty dictionary the same way you do with lists.
#     # empty_dictionary = {}
#     # empty_dictionary["Loop"] = "The action of doing something over and over again."
#     # print(empty_dictionary)
#
# add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
# print(travel_log)


        #Day 9 Project: First-Price Sealed Bid Auction

from art import logo1
print(logo1)
import os

ongoing_auction = True
bid_info = {}

def clear():
    os.system('cls') # This function works only if you check this box: Emulate Terminal in Output Console.
    # The box is found under Run Configuration settings. Also be sure to import os as seen above.

def bid_entry(bidder,cash):
            bid_info[name] = bid

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while ongoing_auction == True:
    name = input("What is your name?:\n")
    bid = int(input("What's your bid?:\n$"))

    bid_entry(name, bid)

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding == "no":
        ongoing_auction = False
        highest_bidder(bid_info)
    elif continue_bidding == "yes":
        clear()