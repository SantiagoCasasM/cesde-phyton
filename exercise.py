def calcularfactura():
    producto = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto (categoria1, categoria2, categoria3): ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    descuento = 0.05
    
    if (categoria == "categoria1" and cantidad > 20) or (categoria == "categoria2" and cantidad > 20) or (categoria == "categoria3" and cantidad > 21):
        if categoria == "categoria1" or categoria == "categoria2":
            descuento = 0.30
            
            subtotal = precio * cantidad
            desciento_total = subtotal * descuento
            subtotal_con_descuento = subtotal - desciento_total
            iva = subtotal_con_descuento * 0.16
            precio_neto = subtotal_con_descuento + iva
            
            print("\nFactura:")
            print("Producto:", producto)
            print("Categoria:", categoria)
            print("Subtotal:", subtotal)
            print("Descuento:", desciento_total)
            print("Subtotal con descuento", subtotal_con_descuento)
            print("IVA (16%)", iva)
            print("Precio neto", precio_neto)
            
calcularfactura()