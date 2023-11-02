const express = require('express');
const Calculator = require('../node_calculator/Calculator');

const app = express();
const calc = new Calculator();

app.listen(8080, () => {
    console.log('listen on port 8080');
});

app.get('/', (_req, res) => {
    const rnd1 = Math.floor(Math.random()*100);
    const rnd2 = Math.floor(Math.random()*100);

    res.send(`你這智障肯定不知道 ${rnd1} + ${rnd2} = ${calc.add(rnd1, rnd2)}`);
});