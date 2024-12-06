rules = []
pages = []

with open("day_5.txt", mode="r") as f:
    reading_rules = True
    for line in [line.rstrip() for line in f.readlines()]:
        if line == "":
            reading_rules = False
            continue
        if reading_rules:
            rules.append(tuple(int(a) for a in line.split("|")))
        else:
            pages.append([int(a) for a in line.split(",")])


def check_rule(page, rule):
    a, b = rule
    # print(f"{a}, {b}")
    found_b = False
    for num in page:
        # print(num)
        if num == a and found_b:
            return False
        if num == b:
            found_b = True
    return True


def check_page(page):
    for rule in rules:
        if not check_rule(page, rule):
            print(page)
            print(rule)
            return False
    return True


total_value = 0
for page in pages:
    if check_page(page):
        total_value += page[round((len(page) - 1) / 2)]

print(total_value)
