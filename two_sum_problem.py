
nums = [1, 2, -2, 5,  -10]
target = 3

pairs = []

def pair_in_pairs(num, test):
    for pair in pairs:
        if (num in pair and  test in pair):
            return True

    return False

for num in nums:
    for index in range(1,len(nums)):
        test = nums[index]
        if (num + test == 3):
            pairs.append((num, test))


print(pairs)

# return value -> [(2, 1), (-2, 5)]
