print("Staircase2!")


# Function will take in three parameters
# steps: amount of steps staircase has,
# max: maximum amount of steps that can be taken at one time,
# array: we will dynamically store our answer in this array as we move forward
def staircase_2(steps, max, array):

	# When steps equals 0-1, only one way to reach top.
	if (steps <= 1): return 1