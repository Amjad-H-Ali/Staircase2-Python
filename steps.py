print("Staircase2!")


# Function will take in three parameters
# steps: amount of steps staircase has,
# m: maximum amount of steps that can be taken at one time,
# array: we will dynamically store our answer in this array as we move forward
def helper(steps, m, array):

	# When steps equals 0-1, only one way to reach top.
	if (steps <= 1): return 1

	# If we already found answer before.
	if (array[steps]): return array[steps]

	# Store the sum in here.
	result = 0

	# Result equals helper(steps - 1, m, array) +  helper(steps - 2, m, array) + ...helper(steps - m, m, array)
	for i in range(1, m + 1):
		# Make sure steps >= 0.
		if (steps - i >= 0): result += helper(steps - i, m, array)

	# Dynamic Programming: Cache result befor returning result to prevent redundant computation.
	array[steps] = result

	return result	

# Wrapper function that calls helper function to initialize params.
def staircase_2 (steps, m):

	array = [None] * (steps + 1)

	return helper(steps, m, array)



print(staircase_2(3, 3)) # 4

print(staircase_2(4, 2)) # 5

print(staircase_2(3, 2)) # 3

print(staircase_2(0, 3)) # 1

print(staircase_2(1, 2)) # 1

print(staircase_2(3, 5)) # 4