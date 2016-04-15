def Check(string):
	i = 0
	add = 0
	while i < len(string):
		for l in string:
		if string[i] == string[l]:
			add = add + 1
		if add == 1:
			return "Found it, " + "string[l] 
		i = i + 1
