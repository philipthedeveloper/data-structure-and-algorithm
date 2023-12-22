function calPoints(ops) {
  let record = []; // Declare an empty record
  for (let op of ops) {
    let isOpConvertible = !isNaN(op); // Check if op is convertible to int
    if (isOpConvertible) {
      record.push(Number(op));
    } else {
      let lastIndex = record.length - 1;
      switch (op) {
        case "+":
          // Since it is guaranteed there will always be two previous scores
          let lastScore = record[lastIndex];
          let secondToLastScore = record[lastIndex - 1];
          record.push(lastScore + secondToLastScore);
          break;
        case "D":
          // Since it is guaranteed there will always be a previous score
          let doublePrevScore = 2 * record[lastIndex];
          record.push(doublePrevScore);
          break;
        case "C":
          // Since it is guaranteed there will always be a previous score
          record.pop();
        default:
          break;
      }
    }
  }
  let total = record.reduce(
    (prevValue, currentValue) => prevValue + currentValue,
    0
  );
  return total;
}

// TEST EXAMPE 1
let output_1 = calPoints(["5", "2", "C", "D", "+"]);
console.log(output_1); // 30

// TEST EXAMPLE 2
let output_2 = calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]);
console.log(output_2); // 27
