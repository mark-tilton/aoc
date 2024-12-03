list_a = []
list_b = []
with open("day_1.txt", mode="r") as f:
    for line in f.readlines():
        nums = [int(num_str) for num_str in line.split("  ")]
        list_a.append(nums[0])
        list_b.append(nums[1])

list_a.sort()
list_b.sort()

value = 0
for a, b in zip(list_a, list_b):
    value += abs(a - b)

print(value)
