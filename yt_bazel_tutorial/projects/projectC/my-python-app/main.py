from flask import Flask
from random import randint

from projects.calculator.calculator import Calculator

app = Flask(__name__)
my_calculatro = Calculator()


@app.route("/")
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = f"{num1} + {num2} = {my_calculatro.add(num1, num2)}"
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
