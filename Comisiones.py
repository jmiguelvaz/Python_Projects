nombre=input("diga su nombre: ")
venta=int(input("Mencione su monto de venta de este mes:$"))
comision=round(venta*0.13,2)
print("Hola, {} tu comision de este mes es: ${}".format(nombre,comision))