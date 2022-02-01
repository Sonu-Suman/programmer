
"""
# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

1). Count the number of expressions containing n pairs of parentheses which are correctly matched. 
For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2). Count the number of possible Binary Search Trees with n keys.

3). Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no 
children) with n+1 leaves.

4). Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points 
such that no 2 chords intersect.
"""

# Let's define the function for catlan numbers.
def catlan(n):
	# Initialize the array for factorial of the n(number).
	num = [0]*((2*n)+1)

	# Initialize second number of array as 1.
	num[1] = 1

	i = 2

	# Calculating the factorial of number for Catlan number
	while i<((2*n)+1):
		# Let's find the factorial nummber of ith number.
		num[i] = num[i-1]*i

		# Let's move for the next number.
		i += 1

	# Now find the caltlan number of n.
	cat = num[2*n]//(num[n+1]*num[n])

	# Returning the catlan number of n
	return int(cat)


# Printing the Catlan number of nth number.
print(catlan(9000))