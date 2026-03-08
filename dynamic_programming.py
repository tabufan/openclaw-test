# Dynamic Programming Script

# Example: Fibonacci sequence using dynamic programming

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Create a table to store Fibonacci numbers
    dp = [0] * (n + 1)
    dp[1] = 1

    # Build the table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test the function
if __name__ == "__main__":
    number = 10
    print(f"The {number}th Fibonacci number is: {fibonacci(number)}")