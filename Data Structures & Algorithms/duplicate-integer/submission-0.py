class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # I know that the array is nums and I know that I need to return true if any
        # numbers appears twice. 
        # Now what I have to think about is what will be easier logically. 
        # why do I use a hashset for this problem?

        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False