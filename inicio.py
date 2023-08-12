#print("...")
#name = "Mariana"
#nota = 2
#print(name)
#print("Hola " + name + " 12234567")
#print(f"Hola {name} tu nota final es de {nota}")

#if nota > 3:
 #   print(f"Felicitaciones su nota es: {nota}")
#else:
#    print(f"Felicitaciones usted perdió")
    
#Precio y cantidad, calcular el subtotal, si el subtotal es meaor de un millon
# clacular descuento del 25% de lo contrario el descuento es de 0%
# calcular el iva y el neto a pagar.

#price = 100000
#cantidad = 2
#subtotal = 0
#iva = 0.19
#neto = 0

#subtotal = price * cantidad

#if subtotal < 10000000:
 #   subtotal = subtotal * 0.25
#else:
 #   subtotal = subtotal + 0

#neto = subtotal + price * iva

#print(f"El descuento es de: {subtotal} y el neto a pagar es de: {neto}")

#Sumar dos numeros


#name = input("Digite su nombre: ")
#num1 = float(input("Digite el primer numero: ")) 
#num2 = float(input("Digite el segundo numero: "))
#suma = num1 + num2
#print(f"Señor {name} la suma de los numeros {num1} {num2} es = a {suma}")

#Condicionales

nota = float(input("Digite la nota entre 0 y 5: "))

if nota > 0 and nota < 2:
    print("Usted reprobo")
elif nota >= 2 and nota < 3:
    print("Puede recuperar")
elif nota >= 3 and nota < 4:
    print("Eres muy bueno")
elif nota >= 4 and nota <= 5:
    print("Eres genial")
else:
    print("El numero debe estar entre 0  5")
