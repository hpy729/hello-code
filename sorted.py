list = []

with open('WOW-UI List.txt', 'r') as f:
    for line in f:
        list.append(line.strip())

with open('WOW-UI List_done.txt', 'w') as f:
    for item in sorted(list):
        f.writelines(item)
    f.close()