from scripts.solver import trapz, simps, trapz_numpy, simps_numpy
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
    upper_limit = int(data['upperLimit'])
    down_limit = int(data['downLimit'])
    subintervals = int(data['subintervals'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result = trapz(f, down_limit, upper_limit, subintervals)
    return result


@app.route('/solve-simps', methods=['POST'])
def solve_simps():
    data = request.get_json()
    equation = latex2sympy(data['equation'])
    upper_limit = int(data['upperLimit'])
    down_limit = int(data['downLimit'])
    subintervals = int(data['subintervals'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result = simps(f, down_limit, upper_limit, subintervals)
    return result


@app.route('/solve-with-all', methods=['POST'])
def solve_with_all():
    data = request.get_json()
    equation = latex2sympy(data['equation'])
    upper_limit = int(data['upperLimit'])
    down_limit = int(data['downLimit'])
    subintervals = int(data['subintervals'])
    integrate_by = sympify('x')
    f = lambdify(integrate_by, equation)
    result_simps = simps(f, down_limit, upper_limit, subintervals)
    result_trapz = trapz(f, down_limit, upper_limit, subintervals)
    result_simps_numpy = simps_numpy(
        f, down_limit, upper_limit, subintervals)
    result_trapz_numpy = trapz_numpy(
        f, down_limit, upper_limit, subintervals)
    result = {'simpsons': result_simps, 'trapez': result_trapz,
              'simpsons_numpy': result_simps_numpy, 'trapz_numpy': result_trapz_numpy}
    return result


@app.route('/convert-expression', methods=['POST'])
def convert_expression():
    data = request.get_json()
    try:
        equation = LatexNodes2Text().latex_to_text(data['equation'])
        return equation
    except:
        error = {'error': 'Pogreška pri unosu funkcije, molim vas unesite ponovno.'}
        return error


if __name__ == '__main__':
    app.run()
