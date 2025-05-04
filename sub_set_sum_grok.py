def subset_sum(set_arr, target_sum, index=0, current_subset=None, current_sum=0, depth=0):
    # Initialize current_subset on first call
    if current_subset is None:
        current_subset = []
    
    # Print current state
    indent = "  " * depth
    print(f"{indent}Index {index}, Element {set_arr[index] if index < len(set_arr) else 'N/A'}, "
          f"Current Subset {current_subset}, Current Sum {current_sum}, Target Remaining {target_sum - current_sum}")
    
    # Base case: if sum is 0 and we've processed all elements, found a valid subset
    if index == len(set_arr):
        if current_sum == target_sum:
            print(f"{indent}✓ Valid subset found: {current_subset}")
        else:
            print(f"{indent}✗ End reached, sum {current_sum} ≠ {target_sum}, backtracking")
        return
    
    # Check if current sum exceeds target (pruning)
    if current_sum > target_sum:
        print(f"{indent}✗ Sum {current_sum} > {target_sum}, backtracking")
        return
    
    # Include current element
    print(f"{indent}Trying to include {set_arr[index]}")
    subset_sum(set_arr, target_sum, index + 1, current_subset + [set_arr[index]], 
               current_sum + set_arr[index], depth + 1)
    
    # Exclude current element
    print(f"{indent}Trying to exclude {set_arr[index]}")
    subset_sum(set_arr, target_sum, index + 1, current_subset, current_sum, depth + 1)

# Test cases
def test_subset_sum():
    # Test case 1
    print("\nTest Case 1: set = [1, 2, 1], sum = 3")
    set1 = [1, 2, 1]
    sum1 = 3
    subset_sum(set1, sum1)
    
    # Test case 2
    print("\nTest Case 2: set = [3, 34, 4, 12, 5, 2], sum = 30")
    set2 = [3, 34, 4, 12, 5, 2]
    sum2 = 30
    subset_sum(set2, sum2)

# Run tests
test_subset_sum()