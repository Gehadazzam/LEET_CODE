class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def getMapIdx(mapping, num):
            stringNum = str(num)
            mapped = ''
            for n in stringNum:
                mapped_n = mapping[int(n)]
                mapped += str(mapped_n)
            mapped_num = int(mapped)
            return mapped_num

        numMapped = [(num, getMapIdx(mapping, num)) for num in nums]
        numMapped.sort(key=lambda x: x[1])
        sortedNums = [x[0] for x in numMapped]
        
        return sortedNums