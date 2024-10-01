import time


def get_minimum_sum(nums: list[int]) -> int:
    temp = 0
    
    for i in range(len(nums) + 1):
        for j in range(len(nums) - i):
            if nums[j: j + i + 1] != []:
                temp += min(nums[j: j + i + 1])
    
    return temp


depth = 10000
m, c = [], []
arr = [11, 81, 94, 43, 3]

if __name__ == "__main__":
    for i in range(depth):
        t = time.time()
        get_minimum_sum(arr)
        m.append(time.time() - t)

        print(''.join(map(str, ["#" for _ in range(i * 10 // depth)])) + ''.join(map(str, ["." for _ in range(10 - (i * 10 // depth))])) + "   " + str(i / depth * 100)[:5] + " %")

    print(sum(m) / depth)
