import time


def find_pair(nums: list[int]) -> int:
    """ 
    Brute-force approach:
    1. First, it sorts the array.
    2. Then, it looks for consecutive duplicates after sorting.
    
    Time Complexity: O(n log n), due to the sorting step.
    
    Args:
        nums (list[int]): List of integers that may contain duplicates.

    Returns:
        int: The first duplicate number found.
    """
    
    nums.sort()  # Sort the list (O(n log n))
    for i in range(len(nums) - 1):  # Traverse through the sorted list
        if nums[i] == nums[i + 1]:  # Check for consecutive duplicates
            return nums[i]


def find_pair1(nums: list[int]) -> int:
    """ 
    Optimized approach using a set:
    1. Traverse the array and use a set to keep track of the numbers seen.
    2. Return the first number that is found twice.
    
    Time Complexity: O(n), since each element is added/checked in the set in constant time.
    
    Args:
        nums (list[int]): List of integers that may contain duplicates.

    Returns:
        int: The first duplicate number found.
    """
    
    seen = set()  # Initialize an empty set to track seen numbers
    for num in nums:
        if num in seen:  # If the number is already in the set, it's a duplicate
            return num
        seen.add(num)  # Otherwise, add the number to the set


depth = 10000
m, c = [], []

# Create a list with numbers from 1 to 499,999 and append a duplicate
arr = list(range(1, 500000))
arr.append(200)  # Append a duplicate to test both methods

if __name__ == "__main__":
    for i in range(depth):
        # Measure time for brute-force solution
        t = time.time()
        find_pair(arr)
        m.append(time.time() - t)
        
        # Measure time for optimized solution
        t = time.time()
        find_pair1(arr)
        c.append(time.time() - t)

        # Progress bar for visual feedback
        print(''.join(map(str, ["#" for _ in range(i * 10 // depth)])) + ''.join(map(str, ["." for _ in range(10 - (i * 10 // depth))])) + "   " + str(i / depth * 100)[:5] + " %")

    # Print average time for both approaches
    print("Average time for brute-force (O(n log n)):", sum(m) / depth)
    print("Average time for optimized (O(n)):", sum(c) / depth)
