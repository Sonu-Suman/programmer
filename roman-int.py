# THis for converting roman to integer


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = 0
        l1 = len(s)
        ll = []
        for k in range(len(s)):
            if k<(l1-1):
                    if d[s[k]]<d[s[k+1]]:
                        a +=  d[s[k+1]]-d[s[k]]
                        ll.append(k)
                        ll.append(k+1)
            
            for i, j in d.items():
                if k not in ll:
                    if i == s[k]:
                        a += j

        return a


s = Solution()
print(s.romanToInt("LVIII"))