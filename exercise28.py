dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]

count = {True: 0, False : 0 }

for bool in dabools:
	count[bool] += 1

print(count)