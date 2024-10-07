import numpy as np

from scipy.linalg import solve

A = np.array ([[3, 2], [4,1]])
B = np.array([5, 6])

X = solve(A, B)
print(X)

A = np.array ([[1, 2], [3, 4]])



from scipy.linalg import inv

A_inv = inv(A)
print(A_inv)



from scipy.linal import det

determinante = det(A)
print(determinante)



from scipy.linalg import eig

A = np.array ([1, 2],[2, 1])

valores, vetores = eig(A)
print('Autovalores:', valores)
print('Autovetores:', vetores)



from scipy.linalg import svd

U, S, Vh = svd(A)
print('U:', U)
print('S:', S)
print('Vh:', Vh)



from scipy.linalg import cholesky

A = np.array ([[4, 12], [12, 37]])


L = cholesky(A, lower = true )
print('L:', L)





from scipy.linalg import qr

A = np.array([[12, -51], [6, 167]])

Q, R = qr(A)
print('Q:', Q)
print('R:', R)





from scipy.linalg import lu

A = np.array ([[4, 3], [6, 3]])

P, L, U = lu(A)
print('P:', P)
print('L:', L)
print('U:', U)





from scipy.optimize import minimize

def func(x):
    return (x[0] -2)**2 + (x[1] -3)**2


x0 = [0, 0]
result = minimize (func, x0, method='BFGS')
print('Ponto de minimo:', result.x)
print('Valor minimo da função:', result.fun)






from scipy.optimize import minimize_scalar

def func(x):
    return (x - 3)**2 + np.sin(x)


result = minimize_scalar(func)
print('Ponto de minimo:', result.x)
print('Valor minimo da função:', result.fun)





from scipy.optimize import root

def func(x):
    return x**2 - 4

x0 = 1.0

result = root(func, x0)
print('Raiz encontrada:', result.x)






from scipy.optimize import curve_fit
import numpy as np

x_data = np.array ([0, 1, 2, 3, 4])
y_data = np.array ([2.1, 2.9, 4.2, 5.1, 6.2])

def linear(x, A, B):
    return A * x + B

params, covariance = curve_fit(linear, x_data, y_data)
A, B = params
print('Coeficiente ajustados: A=', A, 'B=', B)






from scipy.optimize import least_squares

x_data = np.array ([0, 1, 2, 3, 4])
y_data = np.array ([1, 1.8, 3.3, 4.5, 6.1])

def residuals(params, x, y):
    A, B, C = params
    return y - (A * x**2 + B * x + C)

initial_params = [1, 1, 1]

result = least_squares(residuals, initial_params, args=(x_data, y_data))
print('Parametros ajustados:', result.x)

#pagina 23 