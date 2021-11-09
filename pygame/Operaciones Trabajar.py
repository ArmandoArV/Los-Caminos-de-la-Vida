import random
#Lista de items
items = [
    "Leche",
    "Cereal",
    "Aceite de cocina",
    "Raid",
    "Cubrebocas KN95",
]

#Precios de los productos
leche_p = random.randint(18,25)
aceite_p= random.randint(20,33)
raid_p = random.randint(37,56)
cereal_p = random.randint(28,35)
kn95_p = random.randint(30,40)

#Cantidades de productos
leche_cant = random.randint(1,10)  # Esta aparece cuando el contador es menor a 3 o mayor
aceite_cant = random.randint(1,5)  # Esta aparece cuando el contador es menor a 3 o mayor
raid_cant = random.randint(1,3)  # Esta aparece cuando el contador es mayor o igual a 3
cereal_cant = random.randint(1,3)  # Esta aparece cuando el contador es mayor o igual a 3
kn95_cant = random.randint(1,15)  # DIFICIL: SOLO APARECE CUANDO SUPERA LAS 5 CORRECTAS

#Totales
t_leche = leche_cant * leche_p
t_aceite = aceite_cant * aceite_p
t_raid = raid_cant * raid_p
t_cereal = cereal_cant * cereal_p
t_kn95 = kn95_cant * kn95_p
t_final = t_leche + t_aceite + t_raid + t_cereal + t_kn95

#Respuestas correctas
buenas = 0
malas = 0

#Instrucciones
print("Al cobrar los productos anota los totales, ya que al final se te pedirá calcular el total final.")
print("Recuerda que los precios están en pesos mexicanos ($MXN.")

#Aquí comienzan los niveles dependiendo del número de aciertos
if malas < 3:
    print("El precio por litro de leche es:", leche_p, "\nEl cliente se llevará", leche_cant, "litro(s) de leche.")
    total1 = int(input("¿Cuál es el total de los productos?: "))
    if total1 == t_leche:
        print("¡Correcto!")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1
        

if malas < 3:
    print("El precio por litro de aceite es:", aceite_p, "\nEl cliente se llevará", aceite_cant, "litro(s) de aceite.")
    total2 = int(input("¿Cuál es el total de los productos?: "))
    if total2 == t_aceite:
        print("¡Correcto!")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1
        
if malas < 3:
    print("El precio por lata de Raid es:", raid_p, "\nEl cliente se llevará", raid_cant, "lata(s) de Raid.")
    total3 = int(input("¿Cuál es el total de los productos?: "))
    if total3 == t_raid:
        print("¡Correcto!")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1
        
if  malas < 3:
    print("El precio por caja de cereal es:", cereal_p, "\nEl cliente se llevará", cereal_cant, "caja(s) de cereal.")
    total4 = int(input("¿Cuál es el total de los productos?: "))
    if total4 == t_cereal:
        print("¡Correcto!")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1

if  malas < 3:
    print("El precio por cubreboca KN95 es:", kn95_p, "\nEl cliente se llevará", kn95_cant, "cubreboca(s) KN95.")
    total5 = int(input("¿Cuál es el total de los productos?: "))
    if total5 == t_kn95:
        print("¡Correcto!")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1

if  malas < 3:
    TOTAL = int(input("¿Cuál es el total final de los productos? \n(Corrigiendo tus errores, si es que los tuviste): "))
    if TOTAL == t_final:
        print("¡Correcto! Has acertado a la pregunta final.")
        buenas += 1
    else:
        print("Respuesta incorrecta...")
        malas += 1

#Si hay 3 errores, se acaba el juego
if malas == 3:
    print("Has tenido bastantes errores. \nEl juego ha terminado.")
    exit()
    
print("Has tenido", buenas, "aciertos.")
print("Has tenido", malas, "errores.")
print("¡Vuelve pronto a trabajar y aprender!")
