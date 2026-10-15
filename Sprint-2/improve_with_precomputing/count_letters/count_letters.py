from typing import Set


def count_letters(s: str) -> int:
    """
    Returns the number of alphabetic letters that only occur in upper case in the passed string.
    Optimized to O(N) time complexity using sets.
    """
    if not s:
        return 0

    # Collect all unique upper-case and lower-case characters
    upper_chars: Set[str] = {char for char in s if char.isupper()}
    lower_chars: Set[str] = {char.lower() for char in s if char.islower()}

    # Find upper-case letters whose lower-case versions do not exist in the string
    only_upper = {char for char in upper_chars if char.lower() not in lower_chars}

    return len(only_upper)


# Time and Space Complexity Comparison:
#
# Original version:
# - Time Complexity: O(N^2). It used a loop to look at every character, and inside the loop, it searched the entire string s (letter.lower() not in s). This nested search makes it quadratic and slow for long texts.
# - Space Complexity: O(N). It stored unique letters in a set.
#
# Refactored version (with Sets):
# - Time Complexity: O(N). It passes through the string to collect uppercase and lowercase characters into sets first. Because checking a set takes O(1) time, looking up the lowercase letter is instant.
# - Space Complexity: O(N). It uses extra memory to store unique characters in sets, but this is a minor trade-off for a massive increase in speed.
#
# Result: The time complexity drops from O(N^2) to O(N), making the code much faster and more efficient for large inputs.
