const nums = [58, 64, 22, 36, 59];
const target = 100;
let result = [];

for (let i = 0; i < nums.length; i++) {
    if (result.length !== 2) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                result.push(i);
                result.push(j);
                break;
            }
        }
    }
    else {
        break;
    }
}

console.log(result);