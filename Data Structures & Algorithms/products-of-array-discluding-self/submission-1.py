class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for num in nums:
            if num:
                product *= num
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        out = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero:
                out[i] = 0 if c else product
            else: 
                out[i] = product // c
        return out