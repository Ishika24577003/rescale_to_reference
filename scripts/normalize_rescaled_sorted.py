import sys

dict = {}
total = 0

for line in sys.stdin:
    item = line.strip().split('\t')[1]
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
    total += 1

for i in dict:
    print(str(i)+"\t"+str(float(dict[i]/total)))

with open ("total.txt", "w") as f:
    f.write(str(total))
