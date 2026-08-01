class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        length = len(nums)
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = length - 1
                diff = 0 - n
                while l < r:
                    if nums[l] + nums[r] > diff:
                        r -= 1
                    elif nums[l] + nums[r] < diff:
                        l += 1
                    else:
                        out.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return out