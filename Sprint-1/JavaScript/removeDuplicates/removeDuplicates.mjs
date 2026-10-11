/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
/**
* Originally (nested loops):
* Time Complexity: O(n²) - the outer loop runs n times and the inner loop
*   scans uniqueItems, which can grow up to n items (about n(n - 1) / 2
*   checks in the worst case, when all items are unique)
* Space Complexity: O(n) - uniqueItems can hold up to n items
* Optimal Time Complexity: O(n) - every item must be read at least once, and
*   a Set gives O(1) average lookups

* After refactor ([...new Set(inputSequence)]):
* Time Complexity: O(n) - building the Set visits each item once with O(1)
*   average inserts; spreading it into an array is also O(n)
* Space Complexity: O(n) - the Set and the result array each hold up to n items
* Optimal Time Complexity: O(n) - every item must be read at least once, so we
*   can't do better than linear
* /
 * 
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  
  return [... new Set(inputSequence)];
}
