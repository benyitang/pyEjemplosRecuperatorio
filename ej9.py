def ej9():
   fecha = int(input("Ingrese DDMMAAAA"))
   año = fecha % 10000
   fecha = int(fecha / 10000)
   mes = fecha % 100
   dia =  int(fecha / 100)
   print(dia)
   print(año)
   print(mes)
ej9()