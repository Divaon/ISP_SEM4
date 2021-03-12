
data1 = []
len1 = 0
data2 = []
len2 = 0
with open("data1.txt") as f:
    for line in f:
        data1.append([float(x) for x in line.split()])
        len1 += 1
print(data1)
with open("data2.txt") as f:
    for line in f:
        data2.append([float(x) for x in line.split()])
        len2 += 1
print(data2)
if len1 != len2:
    print("Not equal arrays. Goodbye.")
    raise SystemExit(1)
for i in range(0, len1):
    if len(data1[i]) != len(data2[i]):
        print("Not equal arrays. Goodbye.")
        raise SystemExit(1)
for i in range(0, len(data1)):
    for j in range(0, len(data1[0])):
        data1[i][j] += data2[i][j]
print(data1)

