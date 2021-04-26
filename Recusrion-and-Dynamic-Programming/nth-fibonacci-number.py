"""
Compute the nth Fibonacci Number.
"""
# Recusive Approach
# Time Complexity -> O(2^n)
def fib_recursive(n):
    if n <= 1:
        return n
    
    return fib_recursive(n-1) + fib_recursive(n-2)


# Top Down Approach (or Memoization)
# Time Complexity -> O(n)
# Space Complexity -> O(n)
def fib(n):
    memo = [0] * (n+1)

    def fib_recursive(n, memo):
        if n <= 1:
            return n
        
        if memo[n] == 0:
            memo[n] = fib_recursive(n-1, memo) + fib_recursive(n-2, memo)
        
        return memo[n]
    
    return fib_recursive(n, memo)


# Bottom Up Approach
# Time Complexity -> O(n)
# Space Complexity -> O(1)
def fib_bottom_up(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    
    for _ in range(2, n+1):
        a, b = b, a + b
        
    return b
