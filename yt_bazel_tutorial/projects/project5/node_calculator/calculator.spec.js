const Calculator = require('./calculator.js');
const calc = new Calculator();

it('1 + 2 = 3 >', () => {
    expect(calc.add(1, 2)).toEqual(3);  
})