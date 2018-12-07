from collections import Counter


data = [str(x) for x in open("Day2Input.txt").readlines()]


# Part 1
def getCodeChecksum(codes):
	twice = 0
	thrice = 0
	for code in codes:
		counts = Counter(code).values()
		if 2 in counts:
			if 3 in counts:
				twice = twice + 1
				thrice = thrice + 1
			else:
				twice = twice + 1
		elif 3 in counts:
			thrice = thrice + 1
	return twice * thrice


# Part 2
def matching_position(s1, s2):
    pos = -1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

def getMatch(codes):
	for i, code in enumerate(codes):
		others = codes[:i] + codes[i+1:]
		for other in others:
			pos = matching_position(code, other)
			if pos != -1:
				return code[:pos] + code[pos+1:]


# Display Results
print(getCodeChecksum(data))
print(getMatch(data))