let array = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1];

function maxNumOfConsecutiveOnesOrZeros(array) {
	let zeroCount = 1;
	let zeroPostion = 0;
	let oneCount = 1;
	let onePosition = 0;
	
	for (let i = 0; i < array.length; i++) {
		if (array[i] === array[i + 1]) {
			if (array[i] === 1) {
				onePosition = i;
				zeroPostion = 0;
				oneCount++;
				zeroCount = 1;
			} else {
				onePosition = 0;
				zeroPostion = i
				oneCount = 0;
				zeroCount++;
			}
		}
	}
	
	console.log(`zeroCount = ${zeroCount}
onePosition = ${onePosition}
zeroPostion = ${zeroPostion}
oneCount = ${oneCount}
	`);
	
	/*
	if (oneCount > zeroCount) {
		console.log(`The maximum number of consecutive 1’s in the array is ${oneCount}`);
	} else if (zeroCount > oneCount) {
		console.log(`The maximum number of consecutive 0’s in the array is ${zeroCount}`);
	} else {
		console.log("The maximum number of consecutive 1's and 0's");
	}
	*/
}

maxNumOfConsecutiveOnesOrZeros(array);