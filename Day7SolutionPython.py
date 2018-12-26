import string

lines = open('Day7Input.txt').read().split('\n')
lines = [(l.split()[1], l.split()[7]) for l in lines[:-1]]
steps_set = set(string.ascii_uppercase)

# Part 1
def unblocked_steps(steps, lines):
    return [s for s in steps if all(b != s for (_, b) in lines)]

def get_ordered_steps(lines):
    steps = set(string.ascii_uppercase)
    completed_steps = []
    while len(steps) > 0:
        possible_steps = list(unblocked_steps(steps, lines))
        possible_steps.sort()
        executed_step = possible_steps[0]
        completed_steps.append(executed_step)
        steps.remove(executed_step)
        lines = [(a, b) for (a, b) in lines if a != executed_step]
    return ''.join(completed_steps)

print(get_ordered_steps(lines))

# Part 2
def step_time(step):
    return 60 + ord(step) - ord('A')

def get_completion_time(lines):
    steps = set(string.ascii_uppercase)
    time = 0
    workers = [0] * 5
    work = [None] * 5
    while len(steps) > 0 or any(w > 0 for w in workers):
        possible_steps = list(unblocked_steps(steps, lines))
        possible_steps.sort()
        possible_steps = possible_steps[::-1]

        for i in range(5):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    lines = [(a, b) for (a, b) in lines if a != work[i]]
                if possible_steps:
                    n = possible_steps.pop()
                    workers[i] = step_time(n)
                    work[i] = n
                    steps.remove(n)
        time += 1
    return time

get_completion_time(lines)
