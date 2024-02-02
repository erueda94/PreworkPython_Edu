#1. Ejercicio: Dado un número, imprime si es positivo o negativo.
x=5
if x>0:
  print('El numero es positivo')
else:
  print('El numero es negativo)')

#2. Ejercicio: Dado un número, imprime si es par o impar.
if x % 2==0:
  print('El numero es par')
else:
  print('El numero es impar')

#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
x = 5
y = 2
z = 9
numeros = [x,y,z]
if x>y and x>z:
  print("El mayor número es 'x'")
elif y>x and y>z:
  print("El mayor número es 'y'")
elif(z>x and z>y):
  print("El mayor número es 'z'")
  