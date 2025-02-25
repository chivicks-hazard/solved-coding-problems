let number = [1, 2, 3, 4, 5];

for (let num in number) {
    if (num % 3 === 0) {
        console.log(`${num} fizz`);
    } else {
        console.log(num);
    }
}