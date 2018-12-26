polymer = open('Day5Input.txt').read().strip()

# Part 1

def filter_reactions(polymer):
    react = [' ']
    for i in polymer:
        prev = react[-1]
        if i == prev.swapcase():
            react.pop()
        else:
            react.append(i)
    return len(react) - 1

print(filter_reactions(polymer))

# Part 2

def letter_performance(polymer):
    results = []
    for i in ascii_lowercase:
        pol = polymer
        filtered_pol = pol.replace(i, "").replace(i.upper(), "")
        result = filter_reactions(filtered_pol)
        results.append(result)
    return min(results)

print letter_performance(polymer)
