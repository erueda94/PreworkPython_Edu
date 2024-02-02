#1.  Define una función que tome dos números y retorne su suma.
def suma (a,b):
  return a + b
resultado = suma (15, 40)
print(resultado)


#2. Define una función que tome un número y retorne su factorial.
num = 9
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
x = factorial (num)
print(x)


#Define una función que tome un número y determine si es primo
n = 4
def primo(numero):
  for n in range (2,numero):
    if numero % n == 0:
      print("El numero", n, "no es primo")
    else:
      print("Es primo")
primo(n)


'''4.Define una función que reciba una lista de números y retorne la suma
de ellos'''
lista = [55, 13, 17, 65]
def sumatorio(numeros):
  suma = 0
  for num in numeros:
    suma += num
  return suma
print (sumatorio(lista))


#5. Define una función que reciba una cadena de texto y retorne la cadena en reversa
mensaje = "Paz entre los mundos"
def invertir(texto):
  return  mensaje[::-1]
print (invertir(mensaje))
