from typing import List

# ===============> change function <============
def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    # Initialize a cache dictionary
    cache = {}
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], cache)

# =================> change helper function <==============
def ways_to_make_change_helper(total: int, coins: List[int], cache: dict) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    # Create unique key for this subproblem
    cache_key = (total, tuple(coins))

    # Return cached result if already calculated
    if cache_key in cache:
        return cache[cache_key]

    if total == 0 or len(coins) == 0:
        return 0

    ways = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                intermediate = ways_to_make_change_helper(total - total_from_coins, coins=coins[coin_index+1:], cache=cache)
                ways += intermediate
            count_of_coin += 1

    # Save result before returning
    cache[cache_key] = ways
    return ways
