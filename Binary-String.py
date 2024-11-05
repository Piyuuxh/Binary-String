# Minimum Number of Changes to Make Binary String Beautiful
def minChanges(s):
    n = len(s)
    changes = 0
    for i in range(0, n, 2):
        if s[i] == s[i + 1]:
            continue
        else:
            changes += 1
    return changes

s = '1001'
print(minChanges(s))
