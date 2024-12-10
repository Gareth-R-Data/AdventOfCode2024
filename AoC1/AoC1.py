List1 = []
List2 = []
TotalDiff = 0
Similarity = 0

with  open('C:\Repos\AoC\AdventOfCode2024\AoC1\Data.txt') as input_file:
    for line in input_file:
        List1.append(line.strip().split('   ')[0])
        List2.append(line.strip().split('   ')[1])

List1.sort()
List2.sort()

for i in range(len(List1)):
    TotalDiff = TotalDiff + abs(int(List1[i]) - int(List2[i]))

print(f"Answer to Part A is {TotalDiff}")

for i in range(len(List1)):
    Similarity = Similarity + (int(List1[i]) * int(List2.count(List1[i])))

print(f"Answer to Part B is {Similarity}")