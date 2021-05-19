'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 
steps at a time. Implement a method to count how many possible ways the child can run up the 
stairs.
'''
import time

memo = {}
start = time.time()
def triple_step(n):
	if (n in memo):
		return memo[n]
	elif n < 0:
		return 0

	elif n == 0:
		return 1
	else:
		#return triple_step(n-1) + triple_step(n-2) +  triple_step(n-3)
		memo[n] = triple_step(n-1) + triple_step(n-2) +  triple_step(n-3)
		return memo[n]

print(triple_step(37))
print(time.time() - start)