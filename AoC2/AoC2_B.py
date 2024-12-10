List1 = []
List2 = []
CountValid = 0

def checkRecords(reportList):

    flagInvalid = 0
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
        fullRange = range(len(stages))

        if checkRecords(stages) == True:
            CountValid = CountValid + 1

        else:
            for i in fullRange:
                cutStages = stages.copy()
                del(cutStages[i])

                if checkRecords(cutStages) == True:
                    CountValid = CountValid + 1
                    break

print(f"Answer to Part B is {CountValid}")