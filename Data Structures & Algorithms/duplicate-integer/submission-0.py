class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=list()
        for ch in nums:
            if ch in seen:
                return True
            seen.append(ch)
        else:
            return False
        