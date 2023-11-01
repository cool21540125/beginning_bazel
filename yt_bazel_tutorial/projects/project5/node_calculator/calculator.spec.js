const Calculator = require('./calculator.js');
const calculator = new Calculator();

it('1 + 2 = 3 >', () => {
    expect(calculator.add(1, 2)).toEqual(3);  
})