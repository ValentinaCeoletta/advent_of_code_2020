
with open("day3.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

trees = 0
frees = 0

for x in range(len(lines)):
    y = 3*x % (len(lines[0])-1)
    if lines[x][y] == "#":
        trees+=1
    else:
        frees+=1

print("free: " + str(frees) + ", trees: " + str(trees))

res = 1
right = [1,3,5,7,1]
down = [1,1,1,1,2]
for s in range(len(right)):
    trees = 0
    frees = 0
    for x in range(0, len(lines), down[s]):
        print(x)
        y = int(right[s]*x/down[s]) % (len(lines[0])-1)
        if lines[x][y] == "#":
            trees+=1
        else:
            frees+=1
    res*=trees

print("trees :" + str(res))