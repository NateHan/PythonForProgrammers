shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
	thetuple = thetuple + (value,)
	return thetuple

print(appendtotuple(shoes, "jordans"))