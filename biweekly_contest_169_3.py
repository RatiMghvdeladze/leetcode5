class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lstSize = len(nums)

        if lstSize <= 1:
            return lstSize

        left = [1] * lstSize
        for i in range(1, lstSize):
            if nums[i] >= nums[i-1]:
                left[i] = left[i-1] + 1

        right = [1] * lstSize
        for i in range(lstSize - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1] + 1
        
        maxLength = 0
        for runLength in left:
            maxLength = max(maxLength, runLength)
        
        for i in range(lstSize):
            if i > 0:
                maxLength = max(maxLength, left[i-1] + 1)
            
            if i < lstSize - 1:
                maxLength = max(maxLength, right[i+1] + 1)
            
            if i > 0 and i < lstSize - 1:
                if nums[i-1] <= nums[i+1]:
                    maxLength = max(maxLength, left[i-1] + 1 + right[i+1])

        return min(maxLength, lstSize)