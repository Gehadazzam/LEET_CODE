/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let freq = {};
    for (let idx of nums){
        freq[idx] = (freq[idx] || 0) + 1;
        if (freq[idx] > nums.length / 2){
            return idx;
        }
    }
};