
import math
def countMinReversals(expr):
	length = len(expr)


	if (length % 2 != 0):
		return -1

	left_brace = 0
	right_brace = 0

	for i in range(length):

		# If we find a left bracket then we simply
		# increment the left bracket
		if (expr[i] == '{'):
			left_brace += 1

		# Else if left bracket is 0 then we find
		# unbalanced right bracket and increment
		# right bracket or if the expression
		# is balanced then we decrement left
		else:
			if (left_brace == 0):
				right_brace += 1

			else:
				left_brace -= 1

	ans = math.ceil(left_brace / 2) + math.ceil(right_brace / 2)
	return ans

# Driver program to test above function
if __name__ == "__main__":

	expr = "{{{{}}"
	print(countMinReversals(expr))

	# This code is cotributed by ukasp.
