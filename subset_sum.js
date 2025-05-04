function subsetSumWithTrace(set, targetSum) {
    const results = [];
    let traceDepth = 0;
    const traceIndent = () => ' '.repeat(traceDepth * 2);
  
    // Helper function for backtracking
    function backtrack(index, currentSum, currentSubset) {
      // Print the current state
      console.log(`${traceIndent()}Checking index ${index}, current sum: ${currentSum}, current subset: [${currentSubset}]`);
      
      // Base case: we've reached our target sum
      if (currentSum === targetSum) {
        console.log(`${traceIndent()}✓ Found valid subset: [${currentSubset}] with sum ${currentSum}`);
        results.push([...currentSubset]);
        return;
      }
      
      // Base case: sum exceeded or we've checked all elements
      if (currentSum > targetSum || index >= set.length) {
        console.log(`${traceIndent()}✗ Dead end: ${currentSum > targetSum ? 'Sum exceeded' : 'No more elements'}`);
        return;
      }
      
      // Include current element and recurse
      traceDepth++;
      console.log(`${traceIndent()}→ Including element ${set[index]}`);
      currentSubset.push(set[index]);
      backtrack(index + 1, currentSum + set[index], currentSubset);
      
      // Exclude current element and recurse (backtrack)
      console.log(`${traceIndent()}← Backtracking: remove ${currentSubset.pop()} and try without it`);
      backtrack(index + 1, currentSum, currentSubset);
      traceDepth--;
    }
    
    // Start the backtracking process
    console.log(`Finding subsets that sum to ${targetSum} from set [${set}]`);
    backtrack(0, 0, []);
    
    // Print results
    if (results.length === 0) {
      console.log(`No subsets found that sum to ${targetSum}`);
      return [];
    } else {
      console.log(`Found ${results.length} subset(s) that sum to ${targetSum}:`);
      results.forEach(subset => console.log(`[${subset}]`));
      return results;
    }
  }
  
  // Test cases
  console.log("\nTest Case 1:");
  subsetSumWithTrace([1, 2, 1], 3);
  
  console.log("\nTest Case 2:");
  subsetSumWithTrace([3, 34, 4, 12, 5, 2], 30);
  
  // Additional test case for clarity
  console.log("\nTest Case 3:");
  subsetSumWithTrace([1, 3, 5, 7], 8);