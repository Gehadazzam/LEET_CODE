class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        good_pairs = 0
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num, freq in counter.items():
            good_pairs += (freq * (freq - 1)) // 2
        
        return good_pairs
