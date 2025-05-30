const romanNumerals = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
};

let ordinal = "MCMXCIV";

function romanToInt(s) {
    let result = 0;
    for (let i = 0; i < s.length; i++) {
        if (romanNumerals[s[i]] < romanNumerals[s[i + 1]]) {
            result -= romanNumerals[s[i]];
        } else {
            result += romanNumerals[s[i]];
        }
    }

    return result;
}

console.log(romanToInt(ordinal));