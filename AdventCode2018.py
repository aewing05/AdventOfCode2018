# advent - 404169-20181201-03e53c62

### Day 1 ###
import itertools

# Part 1
data = [int(x) for x in open("Day1Input.txt").readlines()]
print(sum(data))

# Part 2
frequency = 0
frequency_log = {0}
for num in itertools.cycle(data):
    frequency += num
    if frequency in frequency_log:
        print(frequency); break
    frequency_log.add(frequency)
