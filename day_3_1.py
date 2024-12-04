import re

with open("day_3.txt", mode="r") as f:
    input_str = f.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", input_str)

print(sum([int(a) * int(b) for a, b in matches]))
