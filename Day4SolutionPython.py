from collections import defaultdict
import re

lines = open('Day4Input.txt').read().split('\n')
lines.sort()

# Part 1
def getMinute(line):
    minute = re.search('(00|23):(\d+)', line)
    if minute:
        return minute.group(2)

def getGuard(line):
    guard = re.search('] Guard #(\d+)', line)
    if guard:
        return guard.group(1)

guard_total_sleep_time = defaultdict(int)
guard_minute_sleep_count = defaultdict(int)
guard = None
asleep = None
for line in lines:
 if line:
     minute = int(getMinute(line))
     if 'begins shift' in line:
         guard = int(getGuard(line))
         asleep = None
     elif 'falls asleep' in line:
         asleep = minute
     elif 'wakes up' in line:
         for t in range(asleep, minute):
             guard_minute_sleep_count[(guard, t)] += 1
             guard_total_sleep_time[guard] += 1


def sleepiest_guard_times_minute():
    sleepiest_guard = max(
        guard_total_sleep_time, key=guard_total_sleep_time.get
    )
    minute_sleep_count = 0
    sleepiest_minute = 0
    for (guard, time), frequency in guard_minute_sleep_count.items():
        if guard == sleepiest_guard:
            if frequency > minute_sleep_count:
                minute_sleep_count = frequency
                sleepiest_minute = time
    return sleepiest_guard * sleepiest_minute


# Part 2

def minute_with_sleepiest_guard():
    highest_slept_minute = 0
    max_frequency = 0
    offending_guard = 0
    for (guard, time), frequency in guard_minute_sleep_count.items():
        if frequency > max_frequency:
            max_frequency = frequency
            highest_slept_minute = time
            offending_guard = guard
    return offending_guard * highest_slept_minute
