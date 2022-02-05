# This is permutation problem for mathematics


#-------------------------------------------------------
# # This is a simple code.

def Permuatation_coefficient(n, k):
	s = 1

	if k>0 and k==int(k) and n==int(n) and n>0 and k<n:
		for i in range(k):
			if i==0:
				s *= n
			else:
				s *= (n-i)
		return s

	return 1


print(Permuatation_coefficient(15900000000000000000000000000000000000000000000000, 21))



# This is second method in the Dynamic programming.


def Permuatations(n, k):
	s = [0]*(min(k, (n-k))+1)

	# if you have a multiplication function, then it's seems right.

		# for i in range(k):
		# 	s[i] = (n-i)

		# res = math.mul(s)
	if k<1 and k==int(k) and n==int(n) and n>0 and k<n:
		return 1

	for i in range(k):
		if i==0:
			s[i] = n
		else:
			s[i] = (s[i-1]*(n-i))

	return s[-2]


print(Permuatations(10, 1))