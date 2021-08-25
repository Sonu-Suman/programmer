# Longest Common Substring

"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring. 


"""

def Longest(X, Y, m, n):
    l = [[0 for k in range(n+1)]for i in range(m+1)]
    result = 0

    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                l[i][j] = 0
            elif (X[i-1]==Y[j-1]):
                l[i][j]= l[i-1][j-1]+1
                result = max(result, l[i][j])
            else:
                l[i][j]=0

    return result


X = "OldSite:GeeksforGeeks.org"
Y = 'NewSite:GeeksQuiz.com'
print(Longest(X, Y, len(X), len(Y)))