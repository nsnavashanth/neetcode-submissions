class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pr={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in pr:
                return[pr[diff],i]
            pr[n]=i
        return


        