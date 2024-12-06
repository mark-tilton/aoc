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
    found_b = False
    for num in page:
        if num == a and found_b:
            return False
        if num == b:
            found_b = True
    return True


def check_page(page):
    for rule in rules:
        if not check_rule(page, rule):
            return False
    return True


def find_index(val, page):
    for i, num in enumerate(page):
        if num == val:
            return i
    return None


failed_pages = []
for page in pages:
    if not check_page(page):
        failed_pages.append(page)

total_value = 0
for page in failed_pages:
    new_page = [page[0]]
    for num in page[1:]:
        latest = len(new_page)
        for a, b in rules:
            if a == num:
                b_index = find_index(b, new_page)
                if b_index is not None and b_index < latest:
                    latest = b_index
        new_page.insert(latest, num)
    total_value += new_page[round((len(new_page) - 1) / 2)]

print(total_value)
