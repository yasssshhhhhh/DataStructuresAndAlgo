
def powerOfJump(s):

	# Initialize the count with 1
	count = 1
	max_so_far = 0
	
	# Find the character at last index
	ch = s[-1]
	
	# Start traversing the string
	for i in range(0, len(s)):
	
		# Check if the current char is
		# equal to the last character
		if s[i] == ch:
		
			# max_so_far stores maximum value of
			# the power of the jump from starting
			# to ith position
			if count > max_so_far:
				max_so_far = count
			
			# Reset the count to 1
			count = 1
		
		# Else, increment the number
		# of jumps/count
		else:
			count += 1
	
	# Return the maximum number of jumps
	return max_so_far

# Driver Code
if __name__ == "__main__":

	st = "11101"
	print(powerOfJump(st))

