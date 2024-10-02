import time


def largest_rectangle_area(nums: list[int]) -> int:
    """ 
    My Attempt:
    Brute-force approach (nested loops to find the largest rectangle)
    Complexity: O(n^3) (where n is the size of the input array)

    Args:
        nums (list[int]): The array to find the biggest rectangle of.

    Returns:
        int: The volume of the biggest rectangle.
    """
    
    rect = 0

    # Generate all possible subarrays
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            # For each subarray, calculate the minimum and use it to compute rectangle area
            temp = min(nums[j:j + i + 1]) * (i + 1)
            if rect < temp:
                rect = temp
    
    return rect


def largest_rectangle_area2(nums: list[int]) -> int:
    """ 
    My Second Attempt:
    Brute-force approach (nested loops to find the largest rectangle)
    Complexity: O(n^3) (where n is the size of the input array)

    Args:
        nums (list[int]): The array to find the biggest rectangle of.

    Returns:
        int: The volume of the biggest rectangle.
    """
    
    rect = 0

    # Generate all possible subarrays
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            # For each subarray, calculate the minimum and use it to compute rectangle area
            temp = min(nums[j:j + i + 1]) * (i + 1)
            if rect < temp:
                rect = temp
    
    return rect


def largest_rectangle_area1(heights: list[int]) -> int:
    """
    ChatGPT's optimized attempt using a monotonic stack.
    Complexity: O(n) (where n is the size of the input array)

    Args:
        heights (list[int]): The array to find the largest rectangle.

    Returns:
        int: The area of the largest rectangle.
    """
    
    stack = []
    max_area = 0
    n = len(heights)

    # Traverse through all the heights
    for i in range(n):
        # Maintain a stack of indices with increasing height order
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            # Calculate width: the distance between the current index and the new top of the stack
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    # Process remaining elements in the stack
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area
            

depth = 10000
m, m1, c = [], [], []

# Test array with heights
arr = list(range(1, 100))

if __name__ == "__main__":
    for i in range(depth):
        # Measure time for brute-force solution
        t = time.time()
        largest_rectangle_area(arr)
        m.append(time.time() - t)
        
        # Measure time for optimized solution
        t = time.time()
        largest_rectangle_area1(arr)
        c.append(time.time() - t)
        
        # Measure time for optimized solution
        t = time.time()
        largest_rectangle_area2(arr)
        m1.append(time.time() - t)

        # Progress bar for visual feedback
        print(''.join(map(str, ["#" for _ in range(i * 10 // depth)])) + ''.join(map(str, ["." for _ in range(10 - (i * 10 // depth))])) + "   " + str(i / depth * 100)[:5] + " %")

    # Print average time for both approaches
    print("Average time for brute-force (O(n³)):", sum(m) / depth)
    print("Average time for optimized (O(n)):", sum(c) / depth)
    print("Average time for optimized (O(r)):", sum(m1) / depth)
