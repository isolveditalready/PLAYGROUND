#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

#mySolution = Solution([1,2,5,9], 6)
mySolution = Solution()
mySolutionF = mySolution.twoSum([1,2,5,9], 6)
print(f"mysolution is {mySolutionF}")