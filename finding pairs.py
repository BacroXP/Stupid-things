import time


# ME
def find_pair(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i + 1]:
            return nums[i]


# CHAT GPT
def find_pair1(nums: list[int]) -> int:
    seen = set()  # This set will store the numbers we encounter
    for num in nums:
        if num in seen:
            return num  # Return the duplicate as soon as we find it
        seen.add(num)


m = []
c = []

input = list(range(1, 500000))
input.append(200)

print(find_pair1(input))


if __name__ == "__main__":
    for i in range(10000):
        t = time.time()
        find_pair(input)
        m.append(time.time() - t)

        t = time.time()
        find_pair1(input)
        c.append(time.time() - t)

        print(''.join(map(str, ["#" for j in range(i // 1000)])) + ''.join(map(str, ["." for j in range(10 - (i // 1000))])) + "   " + str(i / 100) + " %")
    
    
    print(sum(m) / 10000)
    print(sum(c) / 10000)
