import math

def get_row(seat, rows):
    row = [0,rows]
    for i in range(len(seat)):
        if seat[i] == "L" or seat[i] == "F":
            row = [min(row), math.floor((max(row)+min(row))/2.0)]
        else:
            row = [math.ceil(((max(row)+min(row))/2.0)), max(row)]
    return row[0]

with open("day5.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)
ids = []

for i in range(len(lines)):
    row = get_row(lines[i][:7],127)
    column = get_row(lines[i][7:],7)
    id = row * 8 + column
    ids.append(int(id))

print set(ids)

min = min(ids)
for i in range(len(ids)):
    if not min+1 in ids:
        print min+1
        pass
    min+=1