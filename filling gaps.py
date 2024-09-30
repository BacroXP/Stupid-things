import time


# ME
def find_smallest_missing_positive(nums: list[int]) -> int:
    l = len(nums)
    num_array = [i + 1 for i in range(l)]

    for num in nums:
        if 0 < num < l:
            num_array[num - 1] = 0
    
    for b in num_array:
        if bool(b):
            return b


# CHAT GPT
def find_smallest_missing_positive1(nums: list[int]) -> int:
    n = len(nums)
    
    # Step 1: Rearrange the array by placing numbers in their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Step 2: Find the first index where the number is not in the correct position
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all numbers are in the correct position, return n + 1
    return n + 1


m = []
c = []


if __name__ == "__main__":
    for i in range(10000):
        t = time.time()
        find_smallest_missing_positive(list(range(1, 500000)) + list(range(500001, 1000001)))
        m.append(time.time() - t)

        t = time.time()
        find_smallest_missing_positive1(list(range(1, 500000)) + list(range(500001, 1000001)))
        c.append(time.time() - t)

        print(i / 10000 * 100)
    
    print(sum(m) / 10000)
    # 0.18391254336833954
    print(sum(c) / 10000)
    # 0.2438297017812729

    # Mine is three quarters of ChatGPTs time
