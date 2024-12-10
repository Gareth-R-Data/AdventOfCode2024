import re

multiplierResult = 0

with  open('C:\Repos\AoC\AdventOfCode2024\AoC3\Data.txt') as input_file:
    splitOnDo = re.split(r'do\x28\x29', input_file.read())

    for seq in splitOnDo:
        splitOnDont = re.split(r"don't\x28\x29", seq)

        validMatch = re.findall(r'mul\x28\d{1,3},\d{1,3}\x29', splitOnDont[0])

        for match in validMatch:
    
            multipliers = match.split('(')[1].split(')')[0].split(',')

            multiplierResult = multiplierResult + (int(multipliers[0]) * int(multipliers[1]))

print(f"Answer to Part B is {multiplierResult}")