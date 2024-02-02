'''1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda'''





''' 2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.'''


'''3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos. PISTA: Para convertir un número a string usa el método str(). Te recordamos que para saber la longitud de una cadena utilizamos len()'''


'''4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.'''


'''5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado'''


'''6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM'''


'''7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo'''


'''8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero'''


'''9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra'''



'''10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.'''



'''11. Crea una función que, dado un número, verifique si un número es primo'''
'''def esprimo(num):
  x =int(input("Ingrese el número: "))
  if num % x == 0:
    print ("Este numero no es primo")
  else:
    print("Este número es primo")'''
      
    
def es_primo(numero): 
  if numero <= 1:
    return False 
  for i in range(2, numero): 
    if numero % i == 0: 
      return False 
    return True 
num = int(input("Ingresa un número: ")) 
if es_primo(num): 
  print("Es un número primo.") 
else: print("No es un número primo.")



'''12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números
def MCD(a, b):
  resto = 0
  while (b>0):
    resto = b
    b = a % b
    a = resto
  return a
num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", MCD(num1, num2))
#El código de los apuntes no me daba el resultado correcto, tras muchas pruebas y buscar encontré esta manera, pero no entiendo bien el razonamiento dentro del "while"'''
