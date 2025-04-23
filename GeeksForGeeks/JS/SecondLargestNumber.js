let numbers = [12, 35, 1, 10, 34, 1];

function findSecondLargestgNumber(array) {
  for (let i = 0;  i < array.length; i++) {
	  for (let j = 0; j <= i; j++) {
		  if (array[i] > array[j]) {
			  let temp = array[i];
			  array[i] = array[j];
			  array[j] = temp;
		  }
	  }
  }
  
  console.log(array[1]);
}

findSecondLargestgNumber(numbers);
