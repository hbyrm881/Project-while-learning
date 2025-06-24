let a = 32;
let b = 12;
let c = a + b;
console.log(c);

function add(x, y) { 
  return x + y;
}
console.log(add(5, 7)); 
function subtract(x, y) {
  return x - y;
}
console.log(subtract(10, 4));           
function multiply(x, y) {
    return x * y;
}
console.log(multiply(18, 32))

function divide (x, y) {
    if (y === 0) {
        return "Error: Division by zero is not allowed.";
    }
    return x / y;
}
console.log(divide(20, 4)); // Should return 5
console.log(divide(20, 0)); // Should return "Error: Division by zero

//todo is not allowed."
function modulus(x, y) {
    return x % y;
}

console.log(modulus(10, 3)); // Should return 1