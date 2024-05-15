def ej5():
   n1sg = int(input("ingrese horas"))
   n2min = int(input("ingrese minutos"))
   n3hrs = int(input("ingrese segundos"))
   
   resultado = n3hrs * 3600
   resultado2 = n2min * 60
   
   Ensegundos = resultado + resultado2 + n1sg
   
   print("el resultado expresado es: ", Ensegundos)
   
ej5()