/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let hash = {};
    let res = [];
    for (let num of nums) {
        hash[num] = true;
    }
    for (let i = 1; i <= nums.length; i++) {
        if (!hash[i]) {
            res.push(i);
        }
    }
    return res;
};
