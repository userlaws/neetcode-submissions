class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # I know that the array is nums and 
        # I know that I need to return true if any
        # numbers appears twice. 
        # Now what I have to think about is what will be easier logically. 
        # why do I use a hashset for this problem?
        # we use a hashset for this problem because 
        # By using a hash set, 
        # you can scan the list of numbers only once, 
        # making the overall time complexity O(N),

        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False