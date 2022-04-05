class Solution:

    def solve(self, A):
        if len(A) == 1:
            return "-1";
       
        for x in range(len(A)-1,-1,-1):
            smallest_pos = -1;
            smallest_num = 10;
            for y in range(len(A)-1,x,-1):
                if smallest_num > int(A[y]) and int(A[y]) > int(A[x]):
                    smallest_num = int(A[y])
                    smallest_pos = y
            if smallest_num > int(A[x]) and smallest_pos != -1:
                    ret = A[0:x] + str(smallest_num)
                    rest = A[x:smallest_pos]
                    
                    if(smallest_pos+1<len(A)):
                        rest+=A[smallest_pos+1:]
                    
                    rest = sorted(rest)
                    rest2=""
                    for x in rest:
                        rest2 += x 
                    #print(ret)
                    #print(rest)
                    #print(rest2)                   
                    return ret + rest2
           
        return "-1"     


s = Solution()
print(s.solve('740948'))