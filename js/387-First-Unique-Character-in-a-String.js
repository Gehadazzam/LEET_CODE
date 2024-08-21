/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let res = -1;
    for (let idx = 0; idx < s.length; idx++){
        if (s.indexOf(s[idx]) === s.lastIndexOf(s[idx])){
            res = idx;
            break
        }
    }
    return res;
};