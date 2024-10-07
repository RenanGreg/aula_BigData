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





from scipy.optimize import linprog

C = [-1, -2]
A = [[-1, 2], [1, -1]]
B = [2, 2]

result = linprog(c, A_uB=A, B_uB=B, bounds=(0,None))
print('Solução otima:', result.x)
print ('Valor otimo da função:', result.fun)







from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 4
    eq2 = x**2 - y - 1
    return [eq1, eq2]

initial_guess = [1, 1]

solution = fsolve(equations, initial_guess)
print ('Soluçoes: x =', solution[0], ', y =', solution[1])






from scipy.integrate import quad

def func(x):
    return x**2

result, error = quad(func, 0, 1)
print ('Valor integral:', result)
print ('Erro estimado', error)







from scipy.integraten import quad_vec

def func(x):
    return [x**2, x**3]

result = quad_vec(func, 0, 1)
print ('Valor da integral vetorizada:', result)







from scipy.integrate import odeint

def dydt(y, t):
    return -2 * y

t = np.linspace (0, 5, 100)

y0 = 1

solution = odeint(dydt, y0, t)
print ('Solução correspondente y(t):', solution.flatten())







import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

f = interp1d (x, y, kind='linear')

x_new = np.linspace(0, 4, 50)
y_new = f(x_new)

plt.plot(x, y, 'o', label='Dados originais')
plt.plot(x_new, y_new, '-', label='Iterpretação Linear')
plt.legend()
plt.show()







from scipy.iterpolate import interp2d

x = np.linspace(0, 4, 5)
y = np.linspace(0, 4, 5)
z = np.array([[0, 1, 4, 9, 16],
              [1, 2, 5, 10, 17],
              [4, 5, 8, 13, 20],
              [9, 10, 13, 18, 25],
              [16, 17, 20, 25, 32]])

f = interp2d(x, y, z, kind='Linear')

x_new = np.linspace(0, 4, 30)
y_new = np.linspace(0, 4, 30)
z_new = f(x_new, y_new)

x, y = np.meshgrind(x_new, y_new)
plt.contourf(x, y, z_new, levels=20)
plt.colobar()
plt.show()


