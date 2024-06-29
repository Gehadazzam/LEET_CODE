/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function (s1, s2) {
    let firstStr = s1.split(' ');
    let seconedStr = s2.split(' ');
    const countFrequencies = (strings) => {
        let freq = {};
        for (let word of strings) {
            if (freq[word]) {
                freq[word]++;
            } else {
                freq[word] = 1;
            }
        }
        return freq;
    }
    let freq1 = countFrequencies(firstStr);
    let freq2 = countFrequencies(seconedStr);
    let output = [];
    for (let word in freq1) {
        if (freq1[word] === 1 && !(word in freq2)) {
            output.push(word);
        }
    }
    for (let word in freq2) {
        if (freq2[word] === 1 && !(word in freq1)) {
            output.push(word);
        }
    }
    return output;
};