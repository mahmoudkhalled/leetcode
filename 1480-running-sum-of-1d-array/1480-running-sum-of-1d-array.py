class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls = [nums[0]]
        for i in nums[1:]:
            ls.append(i+ls[-1])
        return ls