const express = require('express');
const Calculator = require('../node_calculator/Calculator');

const app = express();
const calculator = new Calculator();

app.listen(8080, () => {
    console.log('listen on port 8080');
});

app.get('/', (req, res) => {
    res.send(`did u know 1 + 2 = ${calculator.add(1, 2)}`);
});