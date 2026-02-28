class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_arr = []
        for i in nums:
            squ = i*i
            sq_arr.append(squ)
        sq_arr.sort()
        return sq_arr