from scripts.solver import trapz, simps
from sympy import sympify
from sympy.utilities.lambdify import lambdify
from latex2sympy2 import latex2sympy
from pylatexenc.latex2text import LatexNodes2Text
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Welcome to integral solver'


@app.route('/solve-trapez', methods=['POST'])
def solve_trapez():
    data = request.get_json()
    equation = latex2sympy(data['equation'])
    upperLimit = int(data['upperLimit'])
    downLimit = int(data['downLimit'])
    accuracy = int(data['accuracy'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result = trapz(f, downLimit, upperLimit, accuracy)
    return result


@app.route('/solve-simps', methods=['POST'])
def solve_simps():
    data = request.get_json()
    equation = latex2sympy(data['equation'])
    upperLimit = int(data['upperLimit'])
    downLimit = int(data['downLimit'])
    accuracy = int(data['accuracy'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result = simps(f, downLimit, upperLimit, accuracy)
    return result


@app.route('/solve-with-all', methods=['POST'])
def solve_with_all():
    data = request.get_json()
    equation = latex2sympy(data['equation'])
    upperLimit = int(data['upperLimit'])
    downLimit = int(data['downLimit'])
    accuracy = int(data['accuracy'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result_simps = simps(f, downLimit, upperLimit, accuracy)
    result_trapz = trapz(f, downLimit, upperLimit, accuracy)
    result = {'simpsons': result_simps, 'trapez': result_trapz}
    return result


@app.route('/convert-expression', methods=['POST'])
def convert_expression():
    data = request.get_json()
    try:
        equation = LatexNodes2Text().latex_to_text(data['equation'])
        is_valid = latex2sympy(data['equation'])
        if is_valid:
            return equation
    except:
        result = {'error': 'Greška pri unosu'}
        return result


if __name__ == '__main__':
    app.run()
