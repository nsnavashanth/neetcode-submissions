class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=set()
        res=0
        for i in range(len(nums)):
            if nums[i] not in n:
                n.add(nums[i])
                nums[res]=nums[i]
                res+=1
        return res

        