from projects.project2.py_calculator.calculator import Calculator
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"嗨~ 你這白癡一定不知道 2 + 3 = {Calculator.add(2, 3)} 吧！\n"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
