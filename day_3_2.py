import re

with open("day_3.txt", mode="r") as f:
    input_str = f.read()

matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input_str)

total = 0
enabled = True

for match in matches:
    a, b, do, dont = match
    if do == "do()":
        enabled = True
        continue
    if dont == "don't()":
        enabled = False
        continue
    if not enabled:
        continue
    total += int(a) * int(b)

print(total)
