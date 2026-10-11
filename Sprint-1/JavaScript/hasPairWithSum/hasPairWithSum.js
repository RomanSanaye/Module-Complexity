/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Inefficiency: the original used a loop inside a loop to check every
 * possible pair of numbers.
 *
 * Originally:
 * Time Complexity: O(n²) - for each number, the inner loop scans the
 *   remaining numbers, so about n * (n - 1) / 2 pair checks.
 * 
 * Space Complexity: O(1) - only the loop counters i and j are used.
 * 
 * Optimal Time Complexity: O(n) - every number must be read at least once,
 *   and a Set gives O(1) average lookups, so one pass is enough
 *
 * After Refactor (reduced from quadratic to linear time by remembering the
 * numbers already seen in a Set instead of re-scanning the list):
 * 
 * Time Complexity: O(n) - one loop, with O(1) average has() and add().
 * 
 * Space Complexity: O(n) - visitedNumbers can hold up to n numbers.
 * 
 * Optimal Time Complexity: O(n) - every number must be read at least once,
 *   so we can't do better than linear.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const visitedNumbers = new Set();

  for (let num of numbers) {
    const partnerNum = target - num;

    if (visitedNumbers.has(partnerNum)) {
      return true;
    }
    visitedNumbers.add(num);
  }

  return false;
}