# Project 1 - Grade Calc Bot

pointsPossible = 33

pointsEarned = 31

studentName = "Nate"

percentScore = round((pointsEarned / pointsPossible) * 100, 2)

minA = 90
minB = 80
minC = 70
minD = 60

gradeReceived = "Unknown"

if percentScore >= minA :
	gradeReceived = "A"
elif percentScore >= minB :
	gradeReceived = "B"	
elif percentScore >= minC :
	gradeReceived = "C"	
elif percentScore >= minD :
	gradeReceived = "D"	
else : gradeReceived = "F"

print("{} received {}% the grade of {}".format(studentName, percentScore, gradeReceived))