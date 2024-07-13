/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    let greedFactor = 0;
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let childIdx = 0;
    let cookiesIdx = 0;
    while (childIdx < g.length && cookiesIdx < s.length){
        if (s[cookiesIdx] >= g[childIdx]){
            greedFactor ++;
            childIdx++;
        }
            cookiesIdx++;
    }
    return greedFactor;
};