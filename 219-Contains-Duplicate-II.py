class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for idx, num in enumerate(nums):
            if num in hash_table and abs(idx - hash_table[num]) <= k:
                return True
            hash_table[num] = idx
        return False