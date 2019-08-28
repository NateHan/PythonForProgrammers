
try : 
	yearBorn = int(input("What Year were you born?\n"))
	print("Wow, at {}, you're super duper old".format(2019 - yearBorn))
except Exception: 
	print("That's not a year, dummy.")


