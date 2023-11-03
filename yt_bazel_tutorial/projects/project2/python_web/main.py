from projects.project2.python_calculator.calculator import Calculator
from flask import Flask
from random import randint
import sys


app = Flask(__name__)
calc = Calculator()


@app.route("/")
def hello_world():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    print(sys.version_info)
    return "嗨~ 你這白癡一定不知道 {} + {} = {} 吧！".format(num1, num2, calc.add(num1, num2))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
