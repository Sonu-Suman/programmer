# For finding smallest word in the list

# This is the first and logest Approach for this problem
s = ["flower","flow","flightgf"]
d = 0

for i in s:
    if d == 0:
        d = len(i)
    else:
        if d>len(i):
            d = len(i)
            s = i

print(d)
print(s)

# This is smallest Approach and second method
shortest = min(s, key=len)


# Now finding longest common prefix in the list

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        smallest = min(strs, key=len)
        
        for i, c in enumerate(smallest):
            for other in strs:
                if other[i] != c:
                    return smallest[:i]
                
        return smallest


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) 