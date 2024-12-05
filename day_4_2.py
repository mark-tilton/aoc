with open("day_4.txt", mode="r") as f:
    word_grid = [line.rstrip() for line in f.readlines()]


def count_xmas(line):
    return line.count("XMAS") + line.count("SAMX")


total_xmas = 0
for line in word_grid:
    total_xmas += count_xmas(line)

for col in range(len(word_grid[0])):
    line = "".join([line[col] for line in word_grid])
    total_xmas += count_xmas(line)


def get_diagnal(col, row, dir):
    index = [row, col]
    line = ""
    for i in range(col + 1):
        if (
            index[0] < len(word_grid)
            and index[1] < len(word_grid[0])
            and index[0] >= 0
            and index[1] >= 0
        ):
            line += word_grid[index[0]][index[1]]
        index[0] += dir[0]
        index[1] += dir[1]
    return count_xmas(line)


for col in range(len(word_grid[0]) + len(word_grid) - 1):
    total_xmas += get_diagnal(col, 0, [1, -1])

for col in range(len(word_grid[0]) + len(word_grid) - 1):
    total_xmas += get_diagnal(col, len(word_grid) - 1, [-1, -1])

print(total_xmas)
