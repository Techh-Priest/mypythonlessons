age = int(input("Considering you live up to 90 years of age,\nlets calculate how much time you have left.\nWhat is your current age?\n"))
years_left = 90 - age
weeks_left = years_left * 52
months_left = years_left * 12
days_left = years_left * 365

print(f"You have {days_left} days,{weeks_left} weeks and {months_left} months left")