class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_hash = {}

        for i in nums:
            if i not in dict_hash:
                dict_hash[i] = 1
            else:
                dict_hash[i] += 1
        spisok = sorted(dict_hash.keys(), key=lambda k: dict_hash[k])

        return spisok[-k:]
