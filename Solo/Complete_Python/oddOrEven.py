def odd_or_even(arr: list) -> str:
    # If the array is empty, consider it as [0]
    if not arr:
        return "even"
    
    # Sum up all the elements in the array
    total = sum(arr)
    
    # Return "odd" or "even" based on the sum
    return "odd" if total % 2 != 0 else "even"

# Test cases
print(odd_or_even([0]))        # Output: "even"
print(odd_or_even([0, 1, 4]))  # Output: "odd"
print(odd_or_even([0, -1, -5]))# Output: "even"
