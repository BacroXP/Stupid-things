import time


def get_minimum_sum(nums: list[int]) -> int:
    """ 
    Brute-force approach (nested loops)
    Complexity: O(n³) (where n is the size of the input array)

    This method calculates the sum of the minimal number in all subarrays by
    generating all possible subarrays and finding their minimum values.

    Args:
        nums (list[int]): array to get the minimal sum of

    Returns:
        int: The sum of the minimal number in all subarrays
    """
    
    temp = 0
    
    # Generate all possible subarrays
    for i in range(len(nums) + 1):
        for j in range(len(nums) - i):
            # For each subarray, calculate the minimum and add it to the total sum
            if nums[j: j + i + 1] != []:
                temp += min(nums[j: j + i + 1])
    
    return temp


def get_minimum_sum1(arr: list[int]) -> int:
    """ 
    Optimized approach using monotonic stack
    Complexity: O(n) (where n is the size of the input array)

    This method calculates the sum of the minimal number in all subarrays
    efficiently using two monotonic stacks to find the Previous Less Element (PLE)
    and Next Less Element (NLE) for each element in the array.

    Args:
        arr (list[int]): array to get the minimal sum of

    Returns:
        int: The sum of the minimal number in all subarrays modulo 10^9 + 7
    """
    
    n = len(arr)
    
    # Arrays to store Previous Less Element (PLE) and Next Less Element (NLE) indices
    ple = [-1] * n  # Initialize PLE with -1 (no element to the left initially)
    nle = [n] * n   # Initialize NLE with n (no element to the right initially)
    
    # Monotonic stack to calculate PLE (Previous Less Element)
    stack = []
    for i in range(n):
        # Maintain a monotonic increasing stack (remove elements greater than current)
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            ple[i] = stack[-1]  # The top of the stack is the PLE for arr[i]
        stack.append(i)
    
    # Monotonic stack to calculate NLE (Next Less Element)
    stack = []
    for i in range(n-1, -1, -1):
        # Maintain a monotonic increasing stack (remove elements greater than current)
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            nle[i] = stack[-1]  # The top of the stack is the NLE for arr[i]
        stack.append(i)
    
    # Calculate the result using PLE and NLE
    result = 0
    for i in range(n):
        # Left count: number of subarrays where arr[i] is the minimum and ends at arr[i]
        left_count = i - ple[i]
        # Right count: number of subarrays where arr[i] is the minimum and starts at arr[i]
        right_count = nle[i] - i
        # Contribution of arr[i] as the minimum in all subarrays that include arr[i]
        result += arr[i] * left_count * right_count
        result %= MOD  # Use modulo to handle large sums
    
    return result


depth = 10000
m, c = [], []
arr = [11, 81, 94, 43, 3]
MOD = 10**9 + 7

if __name__ == "__main__":
    for i in range(depth):
        # Measure time for brute-force solution
        t = time.time()
        get_minimum_sum(arr)
        m.append(time.time() - t)
        
        # Measure time for optimized solution
        t = time.time()
        get_minimum_sum1(arr)
        c.append(time.time() - t)

        # Progress bar
        print(''.join(map(str, ["#" for _ in range(i * 10 // depth)])) + ''.join(map(str, ["." for _ in range(10 - (i * 10 // depth))])) + "   " + str(i / depth * 100)[:5] + " %")

    # Print average time for both approaches
    print("Average time for brute-force (O(n³)):", sum(m) / depth)
    print("Average time for optimized (O(n)):", sum(c) / depth)
