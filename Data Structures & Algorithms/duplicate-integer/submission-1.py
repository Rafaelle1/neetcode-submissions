class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if list(dict.fromkeys(nums)) != nums:
            return True
        return False