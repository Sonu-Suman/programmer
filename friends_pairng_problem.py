"""
Given n friends, each one can remain single or can be paired up with some other friend. 
Each friend can be paired only once. Find out the total number of ways in which friends can remain 
single or can be paired up. 

Examples: --------

Input  : n = 3
Output : 4
Explanation:
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.

Mathematical Explanation:
The problem is simplified version of how many ways we can divide n elements into multiple groups.
(here group size will be max of 2 elements).
In case of n = 3, we have only 2 ways to make a group: 
    1) all elements are individual(1,1,1)
    2) a pair and individual (2,1)
In case of n = 4, we have 3 ways to form a group:
    1) all elements are individual (1,1,1,1)
    2) 2 individuals and one pair (2,1,1)
    3) 2 separate pairs (2,2)

"""

#--------------------------------------------------------------------------------
# This is first type solution


def pair_friendds(n):
	d = [0]*(n+1)

	for i in range(n+1):
		if i<=2:
			d[i] = i
		else:
			d[i] = d[i-1] + (i-1)*d[i-2]

	return d[n]


print(pair_friendds(6))


#-------------------------------------------------------------------------
# This is second type problem for this problem.


# Python3 program for solution of friends pairing problem Using Recursion
dp = [-1] * 1000
# Returns count of ways n people can remain single or paired up.
def countFriendsPairings(n):
	global dp
	
	if(dp[n] != -1):
		return dp[n]

	if(n > 2):

		dp[n] = (countFriendsPairings(n - 1) +
				(n - 1) * countFriendsPairings(n - 2))
		return dp[n]

	else:
		dp[n] = n
		return dp[n]
	
# Driver Code
n = 4
print(countFriendsPairings(n))


# ----------------------------------------------------------------
# This is third type solution for this problem.

# Returns count of ways n people can remain single or paired up.
def countFriendsPairings(n):
	a, b, c = 1, 2, 0;
	if (n <= 2):
		return n;
	for i in range(3, n + 1):
		c = b + (i - 1) * a;
		a = b;
		b = c;
	return c;


# Driver code
n = 4;
print(countFriendsPairings(n));

