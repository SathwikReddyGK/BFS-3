def isValid(s):
        count = 0
        for c in s:
            if count < 0:
                return False
            elif c == "(":
                count += 1
            elif c == ")":
                count -= 1
        
        if count == 0:
            return True
        else:
            return False
        
def removeInvalidParentheses(s):
    workingS = [s[:]]
    result = []
    resultDict = {}

    if isValid(s): return [s]

    while not result:
        tempS = []
        for string in workingS:
            n = len(string)
            for i in range(n):
                if string[i].isalnum():
                    continue

                newS = string[0:i] + string[i+1:n]

                if isValid(newS) and newS not in resultDict:
                    result.append(newS)
                
                if newS not in resultDict:
                    tempS.append(newS)
                    resultDict[newS] = ""
            
            if result:
                tempS = []
                workingS = []
            else:
                workingS = tempS[:]

    return result

if __name__ == "__main__":
    # s = "()())()"
    # s = "(a)())()"
    s = ")("
    print(removeInvalidParentheses(s))