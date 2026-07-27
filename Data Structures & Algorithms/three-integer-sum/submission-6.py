class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        out = []
        for i, n in enumerate(nums):
            if i == 0 or (nums[i] != nums[i-1]):
                l, r = i + 1, length - 1
                target = 0 - n
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l +=1
                    else:
                        out.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        

        return out