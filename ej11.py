def ej11():
    auto = []
    
    numrep = int(input("ingrese el numero de autos que quiere ingresar"))
    
    for y in range (numrep):
    
        precioauto= float(input("ingrese el precio del auto"))
    
        auto.append (precioauto)
    
    comision = numrep * 200
    comisionventa = sum(auto) * 0.05
    sueldo = comision + comisionventa + 5500
    print("el sueldo es: ", sueldo)
    
    
ej11()