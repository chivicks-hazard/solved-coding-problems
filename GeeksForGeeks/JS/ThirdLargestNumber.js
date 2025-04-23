let numbers = [1, 14, 2, 16, 10, 20];
let numbers1 = [19, -10, 20, 14, 2, 16, 10];

function findThirdLargestgNumber(array) {
  for (let i = 0;  i < array.length; i++) {
	  for (let j = 0; j <= i; j++) {
		  if (array[i] > array[j]) {
			  let temp = array[i];
			  array[i] = array[j];
			  array[j] = temp;
		  }
	  }
  }
  
  console.log(array[2]);
}

findThirdLargestgNumber(numbers);
findThirdLargestgNumber(numbers1);