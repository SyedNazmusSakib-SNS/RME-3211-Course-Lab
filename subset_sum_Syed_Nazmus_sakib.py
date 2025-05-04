def find_subsets_with_sum(numbers, target_sum):

    result = []

    current_subset = []

    def backtrack(start_index, current_sum):
        if current_sum == target_sum:
            result.append(current_subset.copy())
            return
        
        if current_sum > target_sum or start_index >= len(numbers):
            return
        
        for i in range(start_index, len(numbers)):
            current_subset.append(numbers[i])
            backtrack(i + 1, current_sum + numbers[i])
            current_subset.pop()
            
    backtrack(0, 0)
    return result

# Test case 1
test_set1 = [1, 2, 1]
target1 = 3
print(f"Set: {test_set1}, Target sum: {target1}")
result1 = find_subsets_with_sum(test_set1, target1)
if result1:
    print(f"Subsets with sum {target1}: {result1}")
else:
    print(f"No subsets with sum {target1}")

# Test case 2
test_set2 = [3, 34, 4, 12, 5, 2]
target2 = 30
print(f"\nSet: {test_set2}, Target sum: {target2}")
result2 = find_subsets_with_sum(test_set2, target2)
if result2:
    print(f"Subsets with sum {target2}: {result2}")
else:
    print(f"No subsets with sum {target2}")

