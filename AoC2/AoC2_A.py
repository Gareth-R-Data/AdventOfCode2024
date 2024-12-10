List1 = []
List2 = []
CountValid = 0

def checkRecords(reportList):

    flagInvalid = 0
    UpOrDown = 1
    reportRange = range(1, len(reportList))

    for i in reportRange:
        diff = (int(reportList[i]) - int(reportList[i-1]))
    
        if diff == 0:
            flagInvalid = flagInvalid + 1
            break
        if abs(diff) > 3:
            flagInvalid = flagInvalid + 1
            break
        if i == 1:
            if diff > 0:
                UpOrDown = 1
            if diff < 0:
                UpOrDown = -1
        if i > 1:
            if diff > 0 and UpOrDown == -1:
                flagInvalid = flagInvalid + 1
                break
            if diff < 0 and UpOrDown == 1:
                flagInvalid = flagInvalid + 1
                break

    if flagInvalid == 0:        
        return True

    flagInvalid = 0

with  open('C:\Repos\AoC\AdventOfCode2024\AoC2\Data.txt') as input_file:
    for line in input_file:
        stages = line.strip().split(' ')

        if checkRecords(stages) == True:
            CountValid = CountValid + 1

print(f"Answer to Part A is {CountValid}")