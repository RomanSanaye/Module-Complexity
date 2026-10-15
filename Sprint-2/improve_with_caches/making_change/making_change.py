from typing import List

# Defined once globally to avoid recreation overhead
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


# ===============> change function <============
def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    # Initialize a cache dictionary
    cache = {}
    # Passing 0 (the starting index) instead of the full list
    return ways_to_make_change_helper(total, 0, cache)


# =================> change helper function <==============
def ways_to_make_change_helper(total: int, start_index: int, cache: dict) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    # Create unique key for this subproblem
    cache_key = (total, start_index)

    # Return cached result if already calculated
    if cache_key in cache:
        return cache[cache_key]

    if total == 0 or start_index >= len(COINS):
        return 0

    ways = 0
    # Iterate through the global COINS list using the integer index
    for i in range(start_index, len(COINS)):
        coin = COINS[i]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                # Just pass an integer (i + 1)
                intermediate = ways_to_make_change_helper(
                    total - total_from_coins, start_index=i + 1, cache=cache
                )
                ways += intermediate
            count_of_coin += 1

    cache[cache_key] = ways
    return ways
