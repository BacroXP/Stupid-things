import time


def find_smallest_missing_positive(nums: list[int]) -> int:
    """ 
    Brute-force approach:
    1. Create an auxiliary array from 1 to n (where n is the length of the input list).
    2. For each positive number in the input, mark the corresponding index in the auxiliary array.
    3. Return the first missing positive integer.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The smallest missing positive integer.
    """
    
    length = len(nums)
    # Create an array of numbers from 1 to n
    num_array = [i + 1 for i in range(length)]

    # Mark the corresponding index in num_array for each valid number in nums
    for num in nums:
        if 0 < num < length:
            num_array[num - 1] = 0
    
    # Return the first non-zero value in num_array
    for b in num_array:
        if bool(b):
            return b


def find_smallest_missing_positive1(nums: list[int]) -> int:
    """ 
    Optimized approach:
    1. Rearrange the array by placing each number in its correct index (nums[i] = i + 1).
    2. Return the first number that is not in its correct position.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The smallest missing positive integer.
    """
    
    n = len(nums)
    
    # Step 1: Place numbers in their correct positions (nums[i] = i + 1)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Step 2: Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all numbers are in the correct positions, return n + 1
    return n + 1


def find_smallest_missing_positive2(nums: list[int]) -> int:
    """ 
    Sorting-based approach:
    1. Sort the array and find the first missing positive integer.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    
    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The smallest missing positive integer.
    """
    
    nums.sort()  # Sort the input list
    for i in range(len(nums)):
        # Return the first number not found in the sorted list
        if i not in nums:
            return i


depth = 10000  # Number of iterations for timing
m, m1, c = [], [], []

# Create a large array with a missing number (500000)
arr = list(range(1, 500000)) + list(range(500001, 1000001))

if __name__ == "__main__":
    for i in range(depth):
        # Measure time for the brute-force solution
        t = time.time()
        find_smallest_missing_positive(arr)
        m.append(time.time() - t)
        
        # Measure time for the optimized solution
        t = time.time()
        find_smallest_missing_positive1(arr)
        c.append(time.time() - t)
        
        # Measure time for the sorting-based solution
        t = time.time()
        find_smallest_missing_positive2(arr)
        m1.append(time.time() - t)

        # Progress bar for feedback
        print(''.join(map(str, ["#" for _ in range(i * 10 // depth)])) + ''.join(map(str, ["." for _ in range(10 - (i * 10 // depth))])) + "   " + str(i / depth * 100)[:5] + " %")

    # Print average times for each approach
    print("Average time for brute-force (O(n)): ", sum(m) / depth)
    print("Average time for sorting-based (O(n log n)): ", sum(m1) / depth)
    print("Average time for optimized (O(n)): ", sum(c) / depth)
