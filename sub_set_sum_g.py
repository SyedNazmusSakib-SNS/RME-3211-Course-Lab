import sys

# Increase recursion depth for potentially deep recursive calls
sys.setrecursionlimit(2000)

def find_subsets_with_sum(
    index,  # Current index in the set
    set_arr, # The input set of numbers
    target_sum, # The target sum we are looking for
    current_subset, # The current subset being built
    simulation_output # List to store simulation steps
):
    """
    Recursively finds subsets that sum up to the target_sum and logs simulation steps.

    Args:
        index: The current index to consider in the set_arr.
        set_arr: The input list of non-negative integers.
        target_sum: The remaining target sum.
        current_subset: The list representing the current subset being built.
        simulation_output: A list to store the detailed simulation steps.
    """

    # Add current state to simulation output
    simulation_output.append(f"Exploring: Index={index}, Current Subset={current_subset}, Remaining Sum={target_sum}")

    # Base Case 1: If the target sum is reached
    if target_sum == 0:
        simulation_output.append(f"SUCCESS: Found a subset with sum 0. Subset: {current_subset}")
        # Return a list containing the found subset
        return [list(current_subset)]

    # Base Case 2: If we have considered all elements or remaining sum is negative
    if index >= len(set_arr) or target_sum < 0:
        simulation_output.append(f"FAIL: Index out of bounds or Remaining Sum < 0. Backtracking.")
        # Return an empty list as no valid subset found in this path
        return []

    # Recursive Step 1: Include the element at the current index
    simulation_output.append(f"Decision: Including element {set_arr[index]} at index {index}")
    # Add the current element to the subset
    current_subset.append(set_arr[index])
    # Recursively call with the next index and reduced target sum
    results_including = find_subsets_with_sum(
        index + 1,
        set_arr,
        target_sum - set_arr[index],
        current_subset,
        simulation_output
    )
    # Backtrack: Remove the element to explore other possibilities
    simulation_output.append(f"Backtracking: Removing element {set_arr[index]} at index {index}")
    current_subset.pop()

    # Recursive Step 2: Exclude the element at the current index
    simulation_output.append(f"Decision: Excluding element {set_arr[index]} at index {index}")
    # Recursively call with the next index and the same target sum
    results_excluding = find_subsets_with_sum(
        index + 1,
        set_arr,
        target_sum,
        current_subset,
        simulation_output
    )

    # Combine results from both branches
    return results_including + results_excluding

def get_subsets_with_sum_and_simulation(set_arr, target_sum):
    """
    Finds all subsets that sum up to the target_sum and returns the subsets
    along with the detailed simulation output.

    Args:
        set_arr: The input list of non-negative integers.
        target_sum: The target sum we are looking for.

    Returns:
        A tuple containing:
            - A list of lists, where each inner list is a subset that sums to target_sum.
            - A list of strings detailing the simulation steps.
    """
    simulation_output = []
    found_subsets = find_subsets_with_sum(
        0, # Start from index 0
        set_arr,
        target_sum,
        [], # Start with an empty current subset
        simulation_output
    )
    return found_subsets, simulation_output

# Example Usage:
set1 = [1, 2, 1]
sum1 = 3
subsets1, simulation1 = get_subsets_with_sum_and_simulation(set1, sum1)

print(f"Set: {set1}, Target Sum: {sum1}")
print("Found Subsets:", subsets1)
print("\n--- Simulation Output ---")
for step in simulation1:
    print(step)

print("\n" + "="*30 + "\n")

set2 = [3, 34, 4, 12, 5, 2]
sum2 = 30
subsets2, simulation2 = get_subsets_with_sum_and_simulation(set2, sum2)

print(f"Set: {set2}, Target Sum: {sum2}")
print("Found Subsets:", subsets2)
print("\n--- Simulation Output ---")
for step in simulation2:
    print(step)

