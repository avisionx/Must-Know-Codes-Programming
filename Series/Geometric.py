# Geometric.py
""" Geometric takes the first number a_1, the q and the number of elements Num, and returns a list containing "Num" numbers in the Geometric series.
	Pre-Conditions - a_1 should be an Number.
				   - q should be an Number.
				   - Num should be an integer >=1.

	Geometric(a_1=7,q = 9,Num = 5) --> Standard function call

	Output --> Num numbers are returned in series starting from a_1 with geometric value q

	Example:
	
	Geometric(1,1,2) returns --> [1,1]
	Geometric(2,2,5) returns --> [2,4,8,16,32]
"""


def Geometric(a_1, q, Num):
    return [a_1 * (q ** i) for i in range(Num)]


if __name__ == '__main__':
    print(Geometric(1, 1, 2))
    print(Geometric(2, 2, 5))