/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let total = new Map();
    for (let idx = 0;  idx < nums.length; idx++){
        let complete = target - nums[idx];
        if (total.has(complete)){
            return [total.get(complete), idx]
        }
        total.set(nums[idx], idx);
    }
    return [];
};