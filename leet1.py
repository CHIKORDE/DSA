nums = []

def twoSum(nums, target):
    hashmap = {}  # value : index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

n = int(input("Enter the array size: "))

for i in range(n):
    num = int(input("Enter the number: "))
    nums.append(num)

print("Your array:", nums)

target = int(input("Enter the target number: "))

result = twoSum(nums, target)
print("Indices:", result)
