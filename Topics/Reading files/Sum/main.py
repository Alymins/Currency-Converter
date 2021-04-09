# read sums.txt
with open("sums.txt") as file:
    for line in file:
        line = line.strip().split()
        print(int(line[0]) + int(line[1]))
