def sumarIVA(Costo):
  #time.wait(120)
  for item in Costo:
    nuevoValor = Costo[item] + (Costo[item]*.16)
    Costo[item] = round(nuevoValor)
    print(item,": $",nuevoValor)

def restarIVA(Costo):
  #time.wait(120)
  for item in Costo:
    nuevoValor = Costo[item] + (Costo[item]*.16)
    Costo[item] = round(nuevoValor)
    print(item,": $",nuevoValor)