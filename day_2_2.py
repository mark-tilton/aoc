def check_values(values):
    last_change = 0
    for a, b in zip(values, values[1:]):
        change = b - a
        if change == 0:
            return False
        if abs(change) > 3:
            return False
        if last_change == 0:
            last_change = change
            continue
        if change > 0 and last_change < 0:
            return False
        if change < 0 and last_change > 0:
            return False
        last_change = change
    return True


with open("day_2.txt", mode="r") as f:
    num_safe = 0
    for line in f.readlines():
        values = [int(val) for val in line.split(" ")]
        for i in range(len(values)):
            skip_i = values[:i] + values[i + 1 :]
            if check_values(skip_i):
                num_safe += 1
                break
    print(num_safe)
