class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a,b=-1,-1
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
               l.append(i)
               
        if len(l)>0:
            a=min(l)
            b=max(l)
        del l
        c=[]
        c.append(a)
        c.append(b)

        return c  
        