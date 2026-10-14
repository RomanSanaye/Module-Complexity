/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(n) - one loop through the list (the original used two
 * loops, 2n steps, which is also O(n)).
 *
 * Space Complexity: O(1) - only two variables (sum, product), regardless of
 * input size
 *
 * Optimal Time Complexity: O(n) - every number must be read at least once, so * we can't do better than linear time
 *
 * Refactor: the complexity can't be reduced, but merging the two loops into
 * one makes the code cleaner and does half the steps.
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}
