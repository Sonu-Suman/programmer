"""
Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }.
"""
# This is the first method.



# Define the function for Bell Number
def Bell_Number(i):
	# Initialize the dictionary for store Bell Number
	s = {}

	# Adding first two bell number
	s[0] = [1]
	s[1] = [0, 1]
	n = 2

	# Now calculating Bell number for greater and equal to 2.
	while n<(i+1):
		s[n] = [0]
		for k in range(1, n+1):
			d = (s[n-1][k-1])
			if k<n:                      
				d += (k*s[n-1][k])
			s[n].append(d)

		n +=1
		
	return sum(s[i])


print(Bell_Number(3000))


# THis is the second method.

def bellNumber(n):

	bell = [[0 for i in range(n+1)] for j in range(n+1)]
	bell[0][0] = 1
	for i in range(1, n+1):

		# Explicitly fill for j = 0
		bell[i][0] = bell[i-1][i-1]

		# Fill for remaining values of j
		for j in range(1, i+1):
			bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

	return bell[n][0]

# Driver program

print('Bell Number is', bellNumber(3000))