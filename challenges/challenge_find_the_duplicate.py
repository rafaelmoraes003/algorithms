from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    if (
        not nums
        or isinstance(nums[0], str)
        or nums[0] < 0
    ):
        return False

    merge_sort(nums)

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
