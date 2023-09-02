#Los diccionarios en phyton deben tener una key:value
#listas []
#tuplas ()
#diccionarios {}

carro = {
    'marca':'Renault',
    'modelo':'2018',
    'cc':'1300',
    'gasolina':'corriente'
    
}

carro1 = {
    'marca':'Land Rover',
    'modelo':'2018',
    'cc':'1300',
    'gasolina':'corriente'
}

carro1['precio'] = 2000000

print(carro1)

#Phyton no maneja posicionamientos numericas.
print(carro['marca'])
print(carro1['marca'])
