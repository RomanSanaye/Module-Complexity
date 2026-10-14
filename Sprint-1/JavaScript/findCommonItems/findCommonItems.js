/**
* Finds common items between two arrays.
 
* Inefficiency: the original used secondArray.includes() inside firstArray
filter(), which is a loop inside a loop.
  
* Originally:
* Time Complexity: O(n × m) - filter runs n times and each includes call can
* scan up to m items (O(n²) if the arrays are the same size).
  
* Space Complexity: O(n) - the filtered array and the Set hold up to n items.
  
* Optimal Time Complexity: O(n + m) - every item in both arrays must be read at
least once.
  
* After refactor (the complexity was reduced from quadratic to linear time by
using a Set for O(1) average lookups instead of includes):
  
* Time Complexity: O(n + m) - building secondSet is O(m); the loop over
firstArray is O(n) with O(1) average  has() checks.

* Space Complexity: O(n + m) - secondSet holds up to m items; commonElements
and the final Set hold up to n    items.

* Optimal Time Complexity: O(n + m) - every item in both arrays must be read at least once, so we can't do better than linear
* 
* @param {Array} firstArray - First array to compare
* @param {Array} secondArray - Second array to compare
* @returns {Array} - Array containing unique common items
*/
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  let commonElements = [];

  for (let ele of firstArray) {
    if (secondSet.has(ele)) {
      commonElements.push(ele);
    }
  }
  return [...new Set(commonElements)];
};
