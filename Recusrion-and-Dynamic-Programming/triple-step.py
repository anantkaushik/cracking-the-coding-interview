"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the satirs.
"""
# Recursive Method
def countWays(n):
    memo = [-1]*(n+1)
    return countWaysRecursive(n,memo)
    
def countWaysRecursive(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = countWaysRecursive(n-1, memo) + countWaysRecursive(n-2, memo) + countWaysRecursive(n-3, memo)
        return memo[n]
        
# Iterative Method
def countWaysIterative(n) : 
    memo = [-1] * (n + 1) 
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1) : 
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3] 
    return memo[n] 