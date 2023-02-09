def calcularDispositivoBebe(edad, peso, altura):
  if(0 <= edad <= 1 and 0 <= peso <= 13 and 0 <= altura <= 75):
    print("Portabebé")
  elif(1 <= edad <= 4 and 9 <= peso <= 18 and 75 <= altura <= 110):
    print("Silla")
  elif(4 <= edad <=6 and 15 <= peso <= 25 and 110 <= altura <= 145):
   print("Asiento con respaldar")
  elif(6 <= edad <= 12 and 22 <= peso <= 36 and 110 <= altura <= 145):
   print("Asiento sin respaldar") 
  else:
    print("no ocupa silla")
  
calcularDispositivoBebe(0.5, 9, 60)
calcularDispositivoBebe(2, 12, 75)
calcularDispositivoBebe(5,22.5,135)
calcularDispositivoBebe(12, 35, 140.5)