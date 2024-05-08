class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                res.append(mid)
                idx = mid - 1
                while idx >= l and nums[idx] == target:
                    res.append(idx)
                    idx -= 1
                idx = mid + 1
                while idx <= r and nums[idx] == target:
                    res.append(idx)
                    idx += 1
                break        
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return sorted(res)
