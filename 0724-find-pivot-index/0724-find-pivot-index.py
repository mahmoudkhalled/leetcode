class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        before = 0 
        after = 0
        for j in range(len(nums)):
            s = sum(nums)
            if before == (s-before-nums[j]):
                return j
            else:
                print(s-before-nums[j])
                before +=nums[j]


        return -1


             