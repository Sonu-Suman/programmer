"""
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions:
 {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""

#----------------------------------------------------------------------------------------------------
# This is the Recursive methode for finding total number.

def Count(coins_array, Coins_array_len, changable_coin):
	if changable_coin==0:
		return 1

	if changable_coin<0:
		return 0

	if Coins_array_len<=0 and changable_coin>0:
		return 0

	return Count(coins_array, Coins_array_len-1, changable_coin)+Count(coins_array, Coins_array_len, changable_coin-coins_array[Coins_array_len-1])


s = [1, 2, 5, 10, 20, 50, 100, 1000]
m = len(s)
n = 70
print(Count(s, m, n))

#-------------------------------------------------------------------------------------------
# This is the second methode for finding total number of changeing coin in others coin,
#  and this is a Dynamic methode.


def count(S, m, n):
	# We need n+1 rows as the table is constructed
	# in bottom up manner using the base case 0 value
	# case (n = 0)
	table = [[0 for x in range(m)] for x in range(n+1)]

	# Fill the entries for 0 value case (n = 0)
	for i in range(m):
		table[0][i] = 1

	# Fill rest of the table entries in bottom up manner
	for i in range(1, n+1):
		for j in range(m):

			# Count of solutions including S[j]
			x = table[i - S[j]][j] if i-S[j] >= 0 else 0

			# Count of solutions excluding S[j]
			y = table[i][j-1] if j >= 1 else 0

			# total count
			table[i][j] = x + y

	return table[n][m-1]

# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))


# --------------------------------------------------------
# This is third type of solution

def count(s, m, n):
	table = [0] * (n+1)

	table[0] = 1

	for i in range(0, m):
		for j in range(s[i], n+1):
			table[j] += table[j-s[i]]

	return table[n]


s = [1, 2, 5, 10, 20, 50, 100, 1000]
m = len(s)
n = 70
print(count(s, m, n))



# This is for finding minimum number changing of coins.--------------------------------------

def count(n, s):
	d = []

	for i in range(len(s)):
		if s[i]<=n:
			d.append(s[i])

	
	j = 0
	q = []

	while j<n:
		n = n%max(d)
		j += 1
		q.append(max(d))
		d.remove(max(d))

	return j, q


print(count(70, [1, 2, 5, 10, 20, 50, 100, 1000]))