class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        n = len(nums)

        for i in range(n):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            else:
                left_sum +=nums[i]
        return -1