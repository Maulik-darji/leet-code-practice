class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sq_arr = []
        # for i in nums:
        #     squ = i*i
        #     sq_arr.append(squ)
        # sq_arr.sort()
        # return sq_arr

        # edge case
        if not nums:
            return nums
        
        if nums[0] >= 0:
            return [num**2 for num in nums]
            
        if nums[-1] < 0:
            return [num*num for num in reversed(nums)]


        # finding first positive 
        m = 0
        for i,n in enumerate(nums):
            if n>=0:
                m = i
                break
        A, B = nums[m:], [-1*n for n in reversed(nums[:m])]
        
        def merge(A,B):
            a = b = 0
            ret = []
            while a<len(A) and b<len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a = a+1
                else:
                    ret.append(B[b])
                    b = b+1
            if a<len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            return[n**2 for n in ret]
        return(merge(A,B))