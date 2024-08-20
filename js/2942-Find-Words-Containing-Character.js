/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    let res = [];
    for (let w = 0; w < words.length; w++) {
        if (words[w].includes(x)) {
            res.push(w);
        }
    }
    return res;
};