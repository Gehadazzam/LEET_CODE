/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let setNums = new Set(nums);
    for (let idx = 0; idx < setNums.size + 1; idx++){
        if (!setNums.has(idx)){
            return idx;
        }
    }
    return setNums.size
};