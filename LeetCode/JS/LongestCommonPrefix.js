const strs = ["flower","flow","flight"];
let prefix = strs[0];

function string() {
    for (let i = 0; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            
            if (prefix === "") return "";
        } 
    }

    return prefix
}

string();

// console.log(strs[1 + 1][2]);