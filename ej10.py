def ej10():
  A = int (input("ingrese calificacion de examen parcial"))
  B = int (input(" ingrese califiacion por TPs"))
  C = int (input("ingrese calificacion del examen integrador"))
  calificacionA = A * 0.3
  calificacionB = B * 0.2
  calificacionC = C * 0.5
   
  Notafinal = calificacionA + calificacionB + calificacionC
  
  print("el promedio del estudiante es: ", Notafinal)
ej10 ()