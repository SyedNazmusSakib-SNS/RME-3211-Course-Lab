def subset_sum_with_trace(numbers, target_sum):
    results = []
    trace_depth = 0
    
    def backtrack(index, current_sum, current_subset):
        nonlocal trace_depth
        
        # Create indentation based on recursion depth for better visualization
        indent = '  ' * trace_depth
        
        # Print current state
        print(f"{indent}Checking index {index}, current sum: {current_sum}, current subset: {current_subset}")
        
        # Base case: found a valid subset
        if current_sum == target_sum:
            print(f"{indent}✓ Found valid subset: {current_subset} with sum {current_sum}")
            results.append(current_subset.copy())
            return
        
        # Base case: sum exceeded or no more elements
        if current_sum > target_sum or index >= len(numbers):
            reason = 'Sum exceeded' if current_sum > target_sum else 'No more elements'
            print(f"{indent}✗ Dead end: {reason}")
            return
        
        # Include current element and recurse
        trace_depth += 1
        print(f"{indent}→ Including element {numbers[index]}")
        current_subset.append(numbers[index])
        backtrack(index + 1, current_sum + numbers[index], current_subset)
        
        # Exclude current element and recurse (backtrack)
        removed = current_subset.pop()
        print(f"{indent}← Backtracking: remove {removed} and try without it")
        backtrack(index + 1, current_sum, current_subset)
        trace_depth -= 1
    
    # Start the backtracking process
    print(f"Finding subsets that sum to {target_sum} from set {numbers}")
    backtrack(0, 0, [])
    
    # Print results summary
    if not results:
        print(f"No subsets found that sum to {target_sum}")
    else:
        print(f"Found {len(results)} subset(s) that sum to {target_sum}:")
        for subset in results:
            print(f"{subset}")
    
    return results

# Test cases
print("\nTest Case 1:")
subset_sum_with_trace([1, 2, 1], 3)

print("\nTest Case 2:")
subset_sum_with_trace([3, 34, 4, 12, 5, 2], 30)

# Additional test case for clarity
print("\nTest Case 3:")
subset_sum_with_trace([1, 3, 5, 7], 8)