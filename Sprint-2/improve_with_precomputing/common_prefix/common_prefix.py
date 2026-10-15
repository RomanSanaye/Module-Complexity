from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    if not strings or len(strings) < 2:
        return ""

    # Pre-computation: Sort the strings lexicographically.
    # The longest common prefix of any two strings in the collection
    # will always be shared by at least one pair of adjacent strings in the sorted list.
    sorted_strings = sorted(strings)

    longest = ""

    for i in range(len(sorted_strings) - 1):
        common = find_common_prefix(sorted_strings[i], sorted_strings[i + 1])
        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]


# Time Complexity Comparison:
# Original version: It used a nested loop to check every possible pair of strings.
# This gave it a slow quadratic time complexity (O(N^2)), which gets very heavy
# and slow as the list grows larger.
#
# New version: We sort the strings alphabetically first. When a list is sorted,
# any two strings with the longest common prefix will always be right next to each other.
# Because of this, we only need a single loop to check neighbor pairs.
#
# Result: This changes the time complexity from O(N^2) to O(N log N),
# making the code much faster and more efficient.
