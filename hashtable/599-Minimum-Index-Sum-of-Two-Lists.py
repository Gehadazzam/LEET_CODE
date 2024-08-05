class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash = {}
        minimumIdxSum = float('inf')
        result = []
        for idx, restaurant in enumerate(list1):
            hash[restaurant] = idx
        for idx2, restaurant in enumerate(list2):
            if restaurant in hash:
                idx1 = hash[restaurant]
                index_sum = idx1 + idx2
                if index_sum < minimumIdxSum:
                    minimumIdxSum = index_sum
                    result = [restaurant]
                elif index_sum == minimumIdxSum:
                    result.append(restaurant)
        
        return result
