with open("day6.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

## PART 1
#lines= ["ab","bc"]
res = []
aux = []
for i in range(len(lines)):
    if lines[i] != "\n":
        for char in lines[i].strip():
            aux.append(char)
    else:
        res.append(len(set(aux)))
        aux = []

res.append(len(set(aux)))
print sum(res)

## PART 2
#lines= ["ab","bc"]
res = []
aux = []

def response_count():
    all = []
    for ga in range(len(aux)):
        if ga > 0:
            all = list(set(all) & set(aux[ga]))
        else:
            all = set(aux[ga])
    return len(all)

for i in range(len(lines)):
    if lines[i] != "\n":
        aux.append([char for char in lines[i].strip()])
    else:
        res.append(response_count())
        aux = []

res.append(response_count())
print sum(res)
