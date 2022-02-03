"""
This is a Bionomial coefficients code

# Formula: 

 B(n, k) = n! / (k!*(n-k)!)
"""

def Bionomial_Coefficient(n, k):
	if k>n:
		return 0
	
	if k==0 or k==n:
		return 1

	BC = [0]*(n+1)
	BC[0] = 0
	BC[1] = 1

	i = 2

	while i<(n+1):
		BC[i] = BC[i-1]*i

		i += 1

	bc = (BC[n])//(BC[k]*BC[n-k])

	return bc

print(Bionomial_Coefficient(5, 4))



# This is Recursive method.

def Bionomial_Coefficient(n, k):
	if k>n:
		return 0
	elif k==0 or k==n:
		return 1

	return Bionomial_Coefficient(n-1, k)+Bionomial_Coefficient(n-1, k-1)


print(Bionomial_Coefficient(5, 4))



# This is java code---------------------

# package com.company;


# public class  project {
#     static int Bionomial(int n, int k) {
#         if (k==0){
#             return 0;
#         }else if (k==n || k>n) {
#             return 1;
#         }
#         return Bionomial(n-1, k)+ Bionomial(n-1, k-1);
#     }

#     public static void main(String[] args) {
#         int n = 9;
#         int k = 5;
#         System.out.println(Bionomial(n, k));
#     }
# }