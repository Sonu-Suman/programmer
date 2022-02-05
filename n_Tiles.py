"""
Given a “2 x n” board and tiles of size “2 x 1”,count the number of ways to tile the given board 
using the 2 x 1 tiles. 
"""
# $ Now I want to build this code in Dynamic Programming methode.

def Count(c):
	assert c==int(c), "Please sir enter number in integer form."

	n = [0]*(c+1)

	if 0<=c<3:
		return c
	elif c<0:
		return "It's not fair boss, You are juding me.\nNoty Bosssssssssssssss."

	n[0] = 0
	n[1] = 1
	n[2] = 2

	i = 3

	while i < (c+1):
		n[i] = n[i-1]+n[i-2]
		i+=1

	return n[c]

print(Count(-67))