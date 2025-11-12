class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lstSize = len(nums)
        qualifyingSubarrayCount = 0
        
        for startIndex in range(lstSize):
            targetFrequency = 0
            for endIndex in range(startIndex, lstSize):
                if nums[endIndex] == target:
                    targetFrequency += 1
                
                subarrayLength = endIndex - startIndex + 1
                
                if targetFrequency > subarrayLength / 2.0:
                    qualifyingSubarrayCount += 1
                    
        return qualifyingSubarrayCount
        