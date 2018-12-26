import itertools
import re
from collections import Counter

# Part 1
data_lines = open("Day3Input.txt").readlines()

def get_coordinate_counter():
    claim_data = map(lambda d: map(int, re.findall(r'\d+', d)), data_lines)
    x_y_coords = []
    for (id, start_x, start_y, width, height) in claim_data:
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                x_y_coords.append(str((i,j)))
    return Counter(x_y_coords)

def overlapping_sq_inches():
    values = get_coordinate_counter().values()
    overlap_inches = 0
    for v in values:
        if v > 1:
            overlap_inches = overlap_inches + 1
    return overlap_inches

print(overlapping_sq_inches())

# Part 2

def unique_coordinates():
    coord_counter = get_coordinate_counter()
    unique_coords = []
    for k,v in coord_counter.items():
        if v == 1:
            unique_coords.append(k)
    return unique_coords

def get_unique_claim():
    claim_data = map(lambda d: map(int, re.findall(r'\d+', d)), data_lines)
    all_unique = unique_coordinates()
    for (id, start_x, start_y, width, height) in claim_data:
        claim_coords = []
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                claim_coords.append(str((i,j)))
        intersection = list(set(claim_coords) & set(all_unique))
        if len(claim_coords) == len(intersection):
            return id
            break

print(get_unique_claim())
