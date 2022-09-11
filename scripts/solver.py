import numpy as np
from sympy.utilities.lambdify import lambdify
from sympy import sympify


def trapz_numpy(f, down_limit, upper_limit, n=50):
    x = np.linspace(down_limit, upper_limit, n+1)
    y = f(x)
    y_right_endpoint = y[1:]
    y_left_endopint = y[:-1]
    dx = (upper_limit - down_limit)/n
    result = (dx/2) * np.sum(y_right_endpoint + y_left_endopint)
    return str(result)


def trapz(f, down_limit, upper_limit, n=50):
    distance = upper_limit - down_limit
    subinterval = down_limit
    x = []
    x.append(subinterval)
    i = 0
    while i < n:
        subinterval = subinterval + distance/n
        x.append(subinterval)
        i += 1
    y = []
    for interval in x:
        try:
            if isinstance(f(round(interval)), float or int) or isinstance(f(round(interval)), int):
                y.append(f(interval))
        except:
            error = {
                'error': 'Funkcija nije definirana ili ima prekid u točki ' + str(int(interval)) + '.', 'isCommon': True}
            return error

    y_right_endpoint = y[1:]
    y_left_endpoint = y[:-1]
    right_endpoint_sum = 0
    left_endpoint_sum = 0
    for interval_result in y_right_endpoint:
        right_endpoint_sum += interval_result
    for interval_result in y_left_endpoint:
        left_endpoint_sum += interval_result
    endpoint_sum = right_endpoint_sum + left_endpoint_sum
    dx = (upper_limit - down_limit)/n
    result = (dx/2) * endpoint_sum
    return str(result)


def simps_numpy(f, down_limit, upper_limit, n=50):
    if n % 2 == 1:
        error = {
            'error': 'Broj podintervala mora biti paran za računanje pomoću simpsonove metode.'}
        return error
    dx = (upper_limit-down_limit)/n
    x = np.linspace(down_limit, upper_limit, n+1)
    y = f(x)
    result = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return str(result)


def simps(f, down_limit, upper_limit, n=50):
    if n % 2 == 1:
        error = {
            'error': {
                'isCommon': False,
                'message': 'Broj podintervala mora biti paran za računanje po Simpsonovoj metodi.'
            }
        }
        return error
    x = []
    distance = upper_limit - down_limit
    subinterval = down_limit
    x.append(subinterval)
    i = 0
    while i < n:
        subinterval = subinterval + distance/n
        x.append(subinterval)
        i += 1
    y = []
    for interval in x:
        try:
            print(f(round(interval)))
            if isinstance(f(round(interval)), float) or isinstance(f(round(interval)), int):
                y.append(f(interval))
        except:
            error = {
                'error': {
                    'isCommon': True,
                    'message': 'Funkcija nije definirana ili ima prekid u točki ' + str(int(interval)) + '.'
                }
            }
            return error
    dx = (upper_limit-down_limit)/n
    y_first_endpoints = y[0:-1:2]
    y_second_endpoints = y[1::2]
    y_third_endpoints = y[2::2]
    first_endpoints_sum = 0
    second_endpoints_sum = 0
    third_endpoints_sum = 0
    for interval_result in y_first_endpoints:
        first_endpoints_sum += interval_result
    for interval_result in y_second_endpoints:
        second_endpoints_sum += 4*interval_result
    for interval_result in y_third_endpoints:
        third_endpoints_sum += interval_result
    endpoint_sum = first_endpoints_sum + second_endpoints_sum + third_endpoints_sum
    result = dx/3 * endpoint_sum
    return str(result)
