# Complete the countingValleys function below.
def countingValleys(n, s):
    counter = 0
    up = 0
    for i in range(len(s)):
        if s[i] == 'U':
            up += 1
            if up == 0:
                counter += 1
        else:
            up -= 1
    return counter
