with open("day_4.txt", mode="r") as f:
    word_grid = [line.rstrip() for line in f.readlines()]


total_xmas = 0

for row in range(1, len(word_grid) - 1):
    for col in range(1, len(word_grid[0]) - 1):
        letter = word_grid[row][col]
        if letter != "A":
            continue
        tl = word_grid[row - 1][col - 1]
        tr = word_grid[row - 1][col + 1]
        bl = word_grid[row + 1][col - 1]
        br = word_grid[row + 1][col + 1]
        tlbr = "".join([tl, br])
        trbl = "".join([tr, bl])
        if tlbr != "MS" and tlbr != "SM":
            continue
        if trbl != "MS" and trbl != "SM":
            continue
        total_xmas += 1

print(total_xmas)
