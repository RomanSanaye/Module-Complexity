def fibonacci(n):
    # Initialize the cache dictionary
    cache = {}

    def helper(number):
        # Check the cache at the start
        if number in cache:
            return cache[number]

        # Base case
        if number <= 1:
            return number

        # Compute the result (making sure number decreases!)
        result = helper(number - 1) + helper(number - 2)

        # Store the result in the cache right before returning
        cache[number] = result
        return result

    return helper(n)