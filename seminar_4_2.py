# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

a = 1
b = 5
c = 4
# discr = (b**2) - (4*a*c)
# print(discr)
# # x = (-b ± √D)/2a, где. D = b − 4ac (D-дискриминант)
# x = ((b*-1)+(discr**0.5))/2*a
# x2 = ((b*-1)-(discr**0.5))/2*a
# print(x, x2)
import sympy
x = sympy.Symbol('x')
ans = sympy.solve(((a*x)**2) + (b*x) + c, x)
print(ans)



