def fibonacci(n):
    # Initialize the cache as a function attribute if it doesn't exist yet
    if not hasattr(fibonacci, "cache"):
        fibonacci.cache = {}

    def helper(number):
        # Check the function attribute cache at the start
        if number in fibonacci.cache:
            return fibonacci.cache[number]

        # Base case
        if number <= 1:
            return number

        # Compute the result (making sure number decreases!)
        result = helper(number - 1) + helper(number - 2)

        # Store the result in the function attribute cache right before returning
        fibonacci.cache[number] = result
        return result

    return helper(n)
