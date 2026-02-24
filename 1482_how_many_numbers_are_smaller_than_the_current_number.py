class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # temp = sorted(nums)
        # d = {}

        # for i, num in enumerate(temp):
        #     if num not in d:
        #         d[num] = i
        # ret = []
        # for i in nums:
        #     ret.append(d[i])
        # return ret

        # sol 2 
        count = [0]*102
        for num in nums:
            count[num+1] = count[num+1]+1
        for i in range(1,102):
            count[i] += count[i-1]
        return [count[num] for num in nums]