print('"Hola buenas tardes"')
#Tema: Salto de Linea
print("Salto de linea", end = " ")
print("salta la liena de forma automatica")
#Tema: Caracteres de Escape
print("Linea 1 \nLínea 2 \nLínea 3")
print("Imprimir entre \"comillas\"")
#Tema: Imprimir multiples lineas
print("""
-----------Pregunta 1-------------
-Indique l edad del usuario.....-
----------------------------------
""")
#Tema: Variables
x=15
y=20
print(x+y)
z="Wenas noshies"
print(z)
print(1,"El resultado es:",x+y)
print ("El tipo de variable x es:", type(x))
#"int" = Entero
#"float" = Numeros fraccionarios
x = 20
y = 25
z = x + y
print("La suma de", x, "mas", y, "es", z)

#"bol" = Falso(0)/Verdadero(1)

x = True
y = False
print("X es igual a:",x,"Y es igual a:",y)

#"str" = Caracter

a = "@"
b = "pacodiaz"
c = a + b
print("Mi correo es:", c)

#Operacion division

r = 10/3
print("El valor de r es:",round(r,3))

#Operacion residuo

r = 10%3
print("El valor de r en el residuo es:",r)

#OPeracion division entera

r = 10//3
print("El valor de r es:",r)

#Jerarquia y operadores aritmeticos
r = 10 + 2 * 5
print(r)

r = (10 + 2) * 5
print (r)

#input con caracteres

print("Indica el valor de X:")
x = input()
print("Indica el valor de Y:")
y = input()
r = x + y
print("El valor de r:", r)

#input con valores numericos enteros

print("Indica el valor de X:")
x = int(input())
print("Indica el valor de Y:")
y = int(input())
r = x + y
print("El valor de r:", r)

#input con valores numericos fraccionarios

x = float(input("Indica el valor de X: "))
y = float(input("Indica el valor de Y: "))

rsum = x + y
rrest = x - y
rmul = x * y
rdiv = x / y
rres = x % y

print("La suma de ", x, "más ", y, "es ", rsum)
print("La resta de ", x, "menos ", y, "es ", rrest)
print("La multiplicacion de ", x, "por ", y, "es ", rmul)
print("La división de ", x, "entre ", y, "es ", rdiv)
print("El residuo de ", x, "entre ", y, "es ", rres)
