# Python program to find the smallest number which  
# is greater than a given no. has same set of  
# digits as given number 
  
# Given number as int array, this function finds the  
# greatest number and returns the number as integer 
def findNext(number,n): 
    # Start from the right most digit and find the first 
    # digit that is smaller than the digit next to it
    i=-1
    for idx in range(n-1,0,-1): 
        if number[idx] > number[idx-1]: 
            i=idx
            break
               
    # If no such digit found,then all numbers are in  
    # descending order, no greater number is possible 
    if i == -1:
        return "-1"
           
    # Find the smallest digit on the right side of  
    # (i-1)'th digit that is greater than number[i-1] 
    x = number[i-1] 
    smallest = i 
    for j in range(i+1,n): 
        if number[j] > x and number[j] < number[smallest]: 
            smallest = j 
           
    # Swapping the above found smallest digit with (i-1)'th 
    number[smallest],number[i-1] = number[i-1], number[smallest] 
       
    # X is the final number, in integer datatype  
    x = 0
    # Converting list upto i-1 into number 
    for j in range(i): 
        x = x * 10 + number[j] 
       
    # Sort the digits after i-1 in ascending order 
    number = sorted(number[i:]) 
    # converting the remaining sorted digits into number 
    for j in range(n-i): 
        x = x * 10 + number[j]
    return x
  
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        #list variable to integeres
        int_list =[]
        # converting characters to integers
        for ch in A:
            int_list.append(int(ch))
        return findNext(int_list,len(int_list)) 


s = Solution()
print(s.solve('740948'))
