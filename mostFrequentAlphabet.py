def mostFrequentAlphabet(s):
	ans = ""
	for i in range(0,len(s)):
		if s[i] == " ":
			continue
		else:
			if s[i].count() > ans:
				ans = s[i]
	if ans == "":
		return "none"
	else:
		return ans
