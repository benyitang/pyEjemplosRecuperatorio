def ej12():
  
   fecha = int(input("Ingrese DDMMAAAA persona1"))
   año = fecha % 10000
   fecha = int(fecha / 10000)
   mes = fecha % 100
   dia = fecha 
   
   
   fecha2 = int(input("Ingrese DDMMAAAA persona2"))
   año2 = fecha2 % 10000
   fecha2 = int(fecha2 / 10000)
   mes2 = fecha2 % 100
   dia2 = fecha2
  
   fecha = año * 10000 + mes * 100 + dia
   fecha2 = año2 * 10000 + mes2 * 100 + dia2
   
   if fecha < fecha2:
    print("sera atendida la persona1")

   elif fecha >fecha2:
    print("sera atentidad primero la persona2")
    
   else : 
    print("seran atendidas ambos")    

ej12()