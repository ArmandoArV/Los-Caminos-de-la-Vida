import Input
from pygame import *
import sys
import pygame
import random
import time


init()
screenPrincipal = pygame.display.set_mode((1250, 650))  # Tamaño de la pantalla
myFont = pygame.font.SysFont("Now", 100, bold=False, italic=False)
myFontIndicadores = pygame.font.SysFont("Now", 70, bold=False, italic=False)
presionado = False



def dibujarIndicadores():
    screenPrincipal.blit(Indicador_Dinero, (0, 0))
    textoDineroActual = myFontIndicadores.render(str(dineroActual),True,(255,255,255))
    screenPrincipal.blit(textoDineroActual, (140,15))
    pygame.display.flip()
def dibujarInventario():
    screenPrincipal.blit(Indicador_inventario,(385,120))
    pygame.display.flip()
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1
        return(num_of_secs)

def escenaInicio(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_inicial, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        if Area_Boton_Jugar_Inicio.collidepoint(x, y):
            return 2
        if Area_Boton_Instrucciones_Inicio.collidepoint(x, y):
            return 3
        pygame.display.flip()

def escenaInicio_BotonJugar(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_boton_jugar_Inicio, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Jugar_Inicio.collidepoint(x, y):
                return 7
        if Area_Boton_Jugar_Inicio.collidepoint(x, y) == False:
            return 1
        pygame.display.flip()

def escenaInicio_BotonInstrucciones(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_boton_instrucciones_Inicio, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Instrucciones_Inicio.collidepoint(x, y):
                return 4
        if Area_Boton_Instrucciones_Inicio.collidepoint(x, y) == False:
            return 1
        pygame.display.flip()

def escenaInstrucciones_Instrucciones(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Instrucciones_Instrucciones, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Siguiente_Instrucciones_Instrucciones.collidepoint(x, y):
                return 5
        pygame.display.flip()

def escenaInstrucciones_ComoJugar(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Instrucciones_ComoJugar, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Siguiente_Instrucciones_ComoJugar.collidepoint(x, y):
                return 6
        pygame.display.flip()

def escenaInstrucciones_Recuerda(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Instrucciones_Recuerda, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Jugar_Instrucciones_Recuerda.collidepoint(x, y):
                return 1
        pygame.display.flip()

def escenaHistoria_Bienvenido(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Historia_Bienvenido, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Historia_Bienvenido.collidepoint(x, y):
                return 8
        pygame.display.flip()

def Casa(screen):
    while True:
        if key.get_pressed()[K_e]:
            print("Pito")
            dibujarInventario()
        screen.fill((255, 255, 255))
        screen.blit(fondo_Casa, (0, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_LEFT:
                return 9
            if e.type == KEYDOWN and e.key == K_RIGHT:
                return 10
        dibujarIndicadores()
        pygame.display.flip()



def Transicion_Casa_Super_Izquierda(screen, velocidad):
    xTransicion = -1250
    xFondo_Supermercado = -2500
    xFondo_Casa = 0
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Transicion_Casa_Supermercado, (xTransicion, 0))
        screen.blit(fondo_Supermercado, (xFondo_Supermercado, 0))
        screen.blit(fondo_Casa, (xFondo_Casa, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        dibujarIndicadores()
        pygame.display.flip()
        if xTransicion < 1250:
            xTransicion += velocidad
        if xFondo_Supermercado < 0:
            xFondo_Supermercado += velocidad
        if xFondo_Casa < 1250:
            xFondo_Casa += velocidad
        if xFondo_Supermercado == 0:
            print("He llegado")
            return 11

def Supermercado(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Supermercado, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_RIGHT:
                return 12
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Entrar_Supermercado.collidepoint(x, y) or Area_Puerta_Entrar_Supermercado.collidepoint(x, y)):
                return 15  # LLeva al interior del supermercado
        dibujarIndicadores()
        pygame.display.flip()

def Transicion_Casa_Super_Derecha(screen, velocidad):
    xTransicion = 1250
    xFondo_Supermercado = 0
    xFondo_Casa = 2500
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Transicion_Casa_Supermercado, (xTransicion, 0))
        screen.blit(fondo_Supermercado, (xFondo_Supermercado, 0))
        screen.blit(fondo_Casa, (xFondo_Casa, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        dibujarIndicadores()
        pygame.display.flip()
        if xTransicion > -1250:
            xTransicion -= velocidad
        if xFondo_Supermercado > -2500:
            xFondo_Supermercado -= velocidad
        if xFondo_Casa > 0:
            xFondo_Casa -= velocidad
        if xFondo_Casa == 0:
            return 8

def Transicion_Casa_Liverpool_Derecha(screen, velocidad):
    xTransicion = 1250
    xFondo_Liverpool = 2500
    xFondo_Casa = 0
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Transicion_Casa_Liverpool, (xTransicion, 0))
        screen.blit(fondo_Liverpool, (xFondo_Liverpool, 0))
        screen.blit(fondo_Casa, (xFondo_Casa, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        dibujarIndicadores()
        pygame.display.flip()
        if xTransicion > -1250:
            xTransicion -= velocidad
        if xFondo_Casa > -2500:
            xFondo_Casa -= velocidad
        if xFondo_Liverpool > 0:
            xFondo_Liverpool -= velocidad
        if xFondo_Liverpool == 0:
            return 13

def Liverpool(screen):
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Liverpool, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_LEFT:
                return 14
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Entrar_Liverpool.collidepoint(x, y) or Area_Puerta_Entrar_Liverpool.collidepoint(x, y)):
                return 20  # LLeva al interior de Liverpool
        dibujarIndicadores()
        pygame.display.flip()

def Transicion_Casa_Liverpool_Izquierda(screen, velocidad):
    xTransicion = -1250
    xFondo_Casa = -2500
    xFondo_Liverpool = 0
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_Transicion_Casa_Liverpool, (xTransicion, 0))
        screen.blit(fondo_Casa, (xFondo_Casa, 0))
        screen.blit(fondo_Liverpool, (xFondo_Liverpool, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        dibujarIndicadores()
        pygame.display.flip()
        if xTransicion < 1250:
            xTransicion += velocidad
        if xFondo_Casa < 0:
            xFondo_Casa += velocidad
        if xFondo_Liverpool < 1250:
            xFondo_Liverpool += velocidad
        if xFondo_Casa == 0:
            return 8

def OpcionesSupermercado(screen, trabajar):
    while True:
        screen.fill((255, 255, 255))
        if trabajar == True:  # Mostrar entre botones habilitados o botones deshabilitados
            screen.blit(fondo_OpcionesHabilitadas_Supermercado, (0, 0))
        else:
            screen.blit(fondo_OpcionesDeshabilitadas_Supermercado, (0, 0))
            texto = myFont.render("5 Min", True, (255, 255, 255))
            screen.blit(texto, ((xTiempo_BotonDeshabilitadoTrabajar_Supermercado+(144-texto.get_width())/2),
                        (yTiempo_BotonDeshabilitadoTrabajar_Supermercado+(45-texto.get_height())/2)))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Comprar_Supermercado.collidepoint(x, y):
                return 16
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Trabajar_Supermercado.collidepoint(x, y) and trabajar == True:
                return 17
        dibujarIndicadores()
        pygame.display.flip()

def Supermercado_Comprar(screen,dinero):
    cantidadLeche = 0
    cantidadManzana = 0
    cantidadHuevo = 0
    cantidadPastel = 0
    precioLeche = random.randint(10,18)
    precioManzana = random.randint(3,7)
    precioHuevo = random.randint(10,18)
    precioPastel = random.randint(25,40)
    total = 0
    while True:
        screen.fill((255, 255, 255))
        if total <= dinero:
            screen.blit(fondo_CajeroComprar_Supermercado, (0, 0))
        else:
            screen.blit(fondo_CajeroComprarSinDinero_Supermercado, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return 11,dinero
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_ComprarArticulos_Supermercado.collidepoint(x, y)) and total > 0:
                dineroActual = dinero - total
                return 11,dineroActual
            #Aumenta contador leche
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Subir_Leche.collidepoint(x, y)):
                cantidadLeche += 1
            #Dismuniye contador leche
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Bajar_Leche.collidepoint(x, y)):
                if (cantidadLeche > 0):
                    cantidadLeche -= 1
            #Aumenta contador manzana
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Subir_Manzana.collidepoint(x, y)):
                cantidadManzana += 1
            #Disminuye Contador Manzana
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Bajar_Manzana.collidepoint(x, y)):
                if (cantidadManzana > 0):
                    cantidadManzana -= 1
            #Aumenta contador Huevo
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Subir_Huevo.collidepoint(x, y)):
                cantidadHuevo += 1
            #Disminuye Contador Huevo
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Bajar_Huevo.collidepoint(x, y)):
                if (cantidadHuevo > 0):
                    cantidadHuevo -= 1
            #Aumenta contador Pastel
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Subir_Pastel.collidepoint(x, y)):
                cantidadPastel += 1
            #Disminuye Contador Pastel
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Bajar_Pastel.collidepoint(x, y)):
                if (cantidadPastel > 0):
                    cantidadPastel -= 1
        textoContadorLeche = myFont.render(str(cantidadLeche),True,(255,255,255))
        textoContadorManzana = myFont.render(str(cantidadManzana),True,(255,255,255))
        textoContadorHuevo = myFont.render(str(cantidadHuevo),True,(255,255,255))
        textoContadorPastel = myFont.render(str(cantidadPastel),True,(255,255,255))
        textoPrecioLeche = myFont.render(str(cantidadLeche*precioLeche),True,(255,255,255))
        textoPrecioManzana = myFont.render(str(cantidadManzana*precioManzana),True,(255,255,255))
        textoPrecioHuevo = myFont.render(str(cantidadHuevo*precioHuevo),True,(255,255,255))
        textoPrecioPastel = myFont.render(str(cantidadPastel*precioPastel),True,(255,255,255))
        total = (cantidadLeche*precioLeche) + (cantidadManzana*precioManzana) + (cantidadHuevo*precioHuevo) + (cantidadPastel*precioPastel)
        textoTotal = myFont.render(str(total),True,(255,255,255))
        screen.blit(textoContadorLeche, (600,210))
        screen.blit(textoContadorManzana, (600,300))
        screen.blit(textoContadorHuevo, (600,380))
        screen.blit(textoContadorPastel, (600,460))
        screen.blit(textoPrecioLeche, (850,210))
        screen.blit(textoPrecioManzana, (850,300)) 
        screen.blit(textoPrecioHuevo, (850,380))
        screen.blit(textoPrecioPastel, (850,460))
        screen.blit(textoTotal, (850,540))
        dibujarIndicadores()
        pygame.display.flip()

def preciosParaTrabajar(nivel):

    leche_precio = random.randint((18*nivel)//2,(25*nivel)//2)
    cereal_precio = random.randint((28*nivel)//2,(35*nivel)//2)
    raid_precio = random.randint((37*nivel)//2,(56*nivel)//2)
    kn95_precio = random.randint((30*nivel)//2,(40*nivel)//2)

    #Cantidades de productos
    leche_cant = random.randint(nivel,10*nivel)  
    cereal_cant = random.randint(nivel,3*nivel)  
    raid_cant = random.randint(nivel,3*nivel)  
    kn95_cant = random.randint(nivel,15*nivel) 

    t_leche = leche_cant * leche_precio
    t_cereal = cereal_cant * cereal_precio
    t_raid = raid_cant * raid_precio
    t_kn95 = kn95_cant * kn95_precio
    t_final = t_leche + t_cereal + t_raid + t_kn95
    #print(t_final,"=",t_leche,t_cereal,t_raid,t_kn95)
    opcionBoton = random.randint(1,3)
    return [[leche_cant,cereal_cant,raid_cant,kn95_cant],[leche_precio,cereal_precio,raid_precio,kn95_precio],t_final,opcionBoton]

def Supermercado_TrabajarNivel1(screen):
    buenas = 0
    malas = 0
    precio = preciosParaTrabajar(1)
    precioIncorrecto1 = random.randint(precio[2]-random.randint(10,15),precio[2]+random.randint(10,15))
    precioIncorrecto2 = random.randint(precio[2]-random.randint(15,20),precio[2]+random.randint(15,20))
    print(precio[3])
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_CajeroTrabajar_Supermercado, (0, 0))
        textoCantidadLeche = myFont.render(str(precio[0][0]),True,(255,255,255))
        textoCantidadCereal = myFont.render(str(precio[0][1]),True,(255,255,255))
        textoCantidadRaid = myFont.render(str(precio[0][2]),True,(255,255,255))
        textoCantidadKN95 = myFont.render(str(precio[0][3]),True,(255,255,255))
        textoPrecioLeche = myFont.render(str(precio[1][0]),True,(255,255,255))
        textoPrecioCereal = myFont.render(str(precio[1][1]),True,(255,255,255))
        textoPrecioRaid = myFont.render(str(precio[1][2]),True,(255,255,255))
        textoPrecioKN95 = myFont.render(str(precio[1][3]),True,(255,255,255))
        textoTotal = myFontIndicadores.render(str(precio[2]),True,(255,255,255))
        textoIncorrecto1 = myFontIndicadores.render(str(precioIncorrecto1),True,(255,255,255))
        textoIncorrecto2 = myFontIndicadores.render(str(precioIncorrecto2),True,(255,255,255))
        screen.blit(textoCantidadLeche, (525,190))
        screen.blit(textoCantidadCereal, (525,275))
        screen.blit(textoCantidadRaid, (525,360))
        screen.blit(textoCantidadKN95, (525,430))
        screen.blit(textoPrecioLeche, (860,190))
        screen.blit(textoPrecioCereal, (860,275))
        screen.blit(textoPrecioRaid, (860,360))
        screen.blit(textoPrecioKN95, (860,430))
        if precio[3] == 1:
            screen.blit(textoTotal, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion2_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion3_Trabajar_Supermercado,570))
        elif precio[3] == 2:
            screen.blit(textoTotal, (X_Boton_Opcion2_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion3_Trabajar_Supermercado,570))
        elif precio[3] == 3:
            screen.blit(textoTotal, (X_Boton_Opcion3_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion2_Trabajar_Supermercado,570))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 1 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                return 18,buenas,malas,2
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 2 and Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                return 18,buenas,malas,2
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 3 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                return 18,buenas,malas,2
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and ((precio[3] == 1 and (Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 1 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 2 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 2 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 3 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 3 and Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)))):
                malas += 1
                return 18,buenas,malas,2
        dibujarIndicadores()
        pygame.display.flip()

def Supermercado_TrabajarNivel2(screen,buenas,malas,nivel):
    print(buenas,malas)
    precio = preciosParaTrabajar(nivel)
    precioIncorrecto1 = random.randint(precio[2]-random.randint(10,15),precio[2]+random.randint(10,15))
    precioIncorrecto2 = random.randint(precio[2]-random.randint(15,20),precio[2]+random.randint(15,20))
    print(precio[3])
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_CajeroTrabajar_Supermercado, (0, 0))
        textoCantidadLeche = myFont.render(str(precio[0][0]),True,(255,255,255))
        textoCantidadCereal = myFont.render(str(precio[0][1]),True,(255,255,255))
        textoCantidadRaid = myFont.render(str(precio[0][2]),True,(255,255,255))
        textoCantidadKN95 = myFont.render(str(precio[0][3]),True,(255,255,255))
        textoPrecioLeche = myFont.render(str(precio[1][0]),True,(255,255,255))
        textoPrecioCereal = myFont.render(str(precio[1][1]),True,(255,255,255))
        textoPrecioRaid = myFont.render(str(precio[1][2]),True,(255,255,255))
        textoPrecioKN95 = myFont.render(str(precio[1][3]),True,(255,255,255))
        textoTotal = myFontIndicadores.render(str(precio[2]),True,(255,255,255))
        textoIncorrecto1 = myFontIndicadores.render(str(precioIncorrecto1),True,(255,255,255))
        textoIncorrecto2 = myFontIndicadores.render(str(precioIncorrecto2),True,(255,255,255))
        screen.blit(textoCantidadLeche, (525,190))
        screen.blit(textoCantidadCereal, (525,275))
        screen.blit(textoCantidadRaid, (525,360))
        screen.blit(textoCantidadKN95, (525,430))
        screen.blit(textoPrecioLeche, (860,190))
        screen.blit(textoPrecioCereal, (860,275))
        screen.blit(textoPrecioRaid, (860,360))
        screen.blit(textoPrecioKN95, (860,430))
        if precio[3] == 1:
            screen.blit(textoTotal, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion2_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion3_Trabajar_Supermercado,570))
        elif precio[3] == 2:
            screen.blit(textoTotal, (X_Boton_Opcion2_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion3_Trabajar_Supermercado,570))
        elif precio[3] == 3:
            screen.blit(textoTotal, (X_Boton_Opcion3_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto1, (X_Boton_Opcion1_Trabajar_Supermercado,570))
            screen.blit(textoIncorrecto2, (X_Boton_Opcion2_Trabajar_Supermercado,570))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 1 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                if nivel < 5:
                    nivel += 1
                    return 18,buenas,malas,nivel
                else:
                    return 19,buenas,malas,nivel
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 2 and Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                if nivel < 5:
                    nivel += 1
                    return 18,buenas,malas,nivel
                else:
                    return 19,buenas,malas,nivel
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (precio[3] == 3 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)):
                buenas += 1
                if nivel < 5:
                    nivel += 1
                    return 18,buenas,malas,nivel
                else:
                    return 19,buenas,malas,nivel
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and ((precio[3] == 1 and (Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 1 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 2 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 2 and Area_Boton_Opcion3_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 3 and Area_Boton_Opcion1_Trabajar_Supermercado.collidepoint(x,y)) or (precio[3] == 3 and Area_Boton_Opcion2_Trabajar_Supermercado.collidepoint(x,y)))):
                malas += 1
                if nivel < 5:
                    nivel += 1
                    return 18,buenas,malas,nivel
                else:
                    return 19,buenas,malas,nivel
        dibujarIndicadores()
        pygame.display.flip()

def JuegoFinalizado(screen,buenas):
    print(buenas)
    while True:
        screen.fill((255, 255, 255))
        screen.blit(fondo_TrabajoFinalizado_Supermercado, (0, 0))
        dineroRecibido = (buenas*1000)/5
        textoBuenas = myFont.render(str(buenas),True,(255,255,255))
        textoDinero = myFont.render(str(dineroRecibido),True,(255,255,255))
        screen.blit(textoBuenas, (491, 244))
        screen.blit(textoDinero, (560, 415))
        Area_Boton_Continuar_TrabajarFinalizado = Rect(541,483,168,59)
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and Area_Boton_Continuar_TrabajarFinalizado.collidepoint(x, y):
                return 11,int(dineroRecibido+dineroActual)
        pygame.display.flip()

def InteriorLiverpool(screen,dinero):
    cantidadLeche = 0
    precioLeche = 30000
    total = 0
    while True:
        
        screen.fill((255, 255, 255))
        if total <= dinero:
            screen.blit(fondo_BotonHabilitado_Liverpool, (0, 0))
        else:
            screen.blit(fondo_BotonDeshabilitado_Liverpool, (0, 0))
        x, y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return 13,dinero
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_ComprarArticulos_Supermercado.collidepoint(x, y)) and total > 0:
                dineroActual = dinero - total
                return 21,dineroActual
            #Aumenta contador leche
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Subir_Leche.collidepoint(x, y)):
                cantidadLeche += 1
            #Dismuniye contador leche
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and (Area_Boton_Bajar_Leche.collidepoint(x, y)):
                if (cantidadLeche > 0):
                    cantidadLeche -= 1
        textoContadorLeche = myFont.render(str(cantidadLeche),True,(0,0,0))
        textoPrecioLeche = myFont.render(str(cantidadLeche*precioLeche),True,(0,0,0))
        total = (cantidadLeche*precioLeche)
        textoTotal = myFont.render(str(total),True,(0,0,0))
        screen.blit(textoContadorLeche, (600,210))
        screen.blit(textoPrecioLeche, (850,210))
        screen.blit(textoTotal, (850,540))
        dibujarIndicadores()
        pygame.display.flip()

def EscenaFinal(screen):
    while True:
            screen.fill((255, 255, 255))
            screen.blit(fondo_final, (0, 0))
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
            pygame.display.flip()
# ----------------------------------------------------------------------------------------------------------------------------------------

# Fondos de la página del Inicio
fondo_inicial = pygame.image.load(
    "Inicio/Inicio Normal.png")  # Fondo del inicio normal
fondo_final = pygame.image.load("Juego Finalizado.png")

fondo_boton_jugar_Inicio = pygame.image.load(
    "Inicio/Inicio Boton Jugar.png")  # Fondo del boton jugar seleccionado
Area_Boton_Jugar_Inicio = Rect(492, 184, 266, 95)  # Area del boton jugar

fondo_boton_instrucciones_Inicio = pygame.image.load(
    "Inicio/Inicio Boton Instrucciones.png")  # Fondo del boton instrucciones seleccionado
Area_Boton_Instrucciones_Inicio = Rect(
    492, 336, 266, 95)  # Area del boton instrucciones

# Fondos de la página de las Instrucciones (nombre del boton_Area actual del juego_pagina actual del juego)
fondo_Instrucciones_Instrucciones = pygame.image.load(
    "Instrucciones/Instrucciones.png")
Area_Siguiente_Instrucciones_Instrucciones = Rect(1141, 33, 44, 65)

fondo_Instrucciones_ComoJugar = pygame.image.load(
    "Instrucciones/Como Jugar.png")
Area_Siguiente_Instrucciones_ComoJugar = Rect(1141, 33, 44, 65)

fondo_Instrucciones_Recuerda = pygame.image.load("Instrucciones/Recuerda.png")
Area_Jugar_Instrucciones_Recuerda = Rect(1068, 33, 182, 65)

# Fondos Historia
fondo_Historia_Bienvenido = pygame.image.load("Historia/Bienvenido.png")
Area_Boton_Historia_Bienvenido = Rect(625, 526, 250, 89)

# Fondo Casa
fondo_Casa = pygame.image.load("Lugares/Casa.png")

# Fondo Transiciones
fondo_Transicion_Casa_Supermercado = pygame.image.load(
    "Transicion/Casa-Supermercado.png")
fondo_Transicion_Casa_Liverpool = pygame.image.load(
    "Transicion/Casa-Liverpool.png")

# Fondo Supermercado Exterior
fondo_Supermercado = pygame.image.load("Lugares/Supermercado.png")
Area_Boton_Entrar_Supermercado = Rect(314, 404, 144, 51)
Area_Puerta_Entrar_Supermercado = Rect(290, 455, 190, 100)

# Fondo Liverpool
fondo_Liverpool = pygame.image.load("Lugares/Liverpool.png")
Area_Boton_Entrar_Liverpool = Rect(716, 384, 144, 51)
Area_Puerta_Entrar_Liverpool = Rect(676, 435, 224, 120)
fondo_BotonDeshabilitado_Liverpool = pygame.image.load("Liverpool/Liverpool Boton Deshabilitado.png")
fondo_BotonHabilitado_Liverpool = pygame.image.load("Liverpool/Liverpool Boton Habilitado.png")

# Fondos Supermercado Interior
fondo_OpcionesHabilitadas_Supermercado = pygame.image.load(
    "Supermercado/Elección del super habilitado.png")
fondo_OpcionesDeshabilitadas_Supermercado = pygame.image.load(
    "Supermercado/Elección del super deshabilitado.png")
fondo_CajeroTrabajar_Supermercado = pygame.image.load(
    "Supermercado/Interior Supermercado trabajar.png")
fondo_CajeroComprar_Supermercado = pygame.image.load(
    "Supermercado/Interior Supermercado Comprar.png")
fondo_CajeroComprarSinDinero_Supermercado = pygame.image.load(
    "Supermercado/Interior Supermercado Sin Suficiente Dinero.png")
fondo_TrabajoFinalizado_Supermercado = pygame.image.load("Supermercado/Interior Supermercado Finalizado.png")
Area_Boton_Comprar_Supermercado = Rect(99, 245, 312, 160)
Area_Boton_Trabajar_Supermercado = Rect(812, 245, 312, 160)
xTiempo_BotonDeshabilitadoTrabajar_Supermercado = 897
yTiempo_BotonDeshabilitadoTrabajar_Supermercado = 512

# Personajes
Personaje_Silla_Width = 260
Personaje_Silla_Height = 300
Personaje_Silla_Derecha = pygame.image.load("Harper/Harper Silla Derecha.png")
Personaje_Silla_Derecha = pygame.transform.scale(Personaje_Silla_Derecha, (Personaje_Silla_Width, Personaje_Silla_Height))

# Areas de botones comprar Supermercado
Area_Boton_Subir_Leche = Rect(729,205,32,32)
Area_Boton_Bajar_Leche = Rect(729,237,32,32)
Area_Boton_Subir_Manzana = Rect(729,294,32,32)
Area_Boton_Bajar_Manzana = Rect(729,325,32,32)
Area_Boton_Subir_Huevo = Rect(729,374,32,32)
Area_Boton_Bajar_Huevo = Rect(729,407,32,32)
Area_Boton_Subir_Pastel = Rect(729,453,32,32)
Area_Boton_Bajar_Pastel = Rect(729,485,32,32)
Area_Boton_ComprarArticulos_Supermercado = Rect(404,531,167,59)

#Area de botones trabajar Supermercado
Area_Boton_Opcion1_Trabajar_Supermercado = Rect(502,567,141,51)
Area_Boton_Opcion2_Trabajar_Supermercado = Rect(687,567,141,51)
Area_Boton_Opcion3_Trabajar_Supermercado = Rect(878,567,141,51)
X_Boton_Opcion1_Trabajar_Supermercado = 535
X_Boton_Opcion2_Trabajar_Supermercado = 720
X_Boton_Opcion3_Trabajar_Supermercado = 910

#Indicadores
Indicador_Dinero = pygame.image.load("Indicadores/Dinero.png")
Indicador_Dinero = pygame.transform.scale(Indicador_Dinero, (250, 75))
Indicador_inventario = pygame.image.load("Indicadores/inventario.png")
inv_anc = 600
inv_alt = 500
Indicador_inventario = pygame.transform.scale(Indicador_inventario,(inv_anc,inv_alt))
# ----------------------------------------------------------------------------------------------------------------------------------------

dineroActual = 100
escena = 1
velocidadTransiciones = 10
while True:

    if escena == 1:
        escena = escenaInicio(screenPrincipal)
    if escena == 2:
        escena = escenaInicio_BotonJugar(screenPrincipal)
    if escena == 3:
        escena = escenaInicio_BotonInstrucciones(screenPrincipal)
    if escena == 4:
        escena = escenaInstrucciones_Instrucciones(screenPrincipal)
    if escena == 5:
        escena = escenaInstrucciones_ComoJugar(screenPrincipal)
    if escena == 6:
        escena = escenaInstrucciones_Recuerda(screenPrincipal)
    if escena == 7:
        escena = escenaHistoria_Bienvenido(screenPrincipal)
    if escena == 8:
        escena = Casa(screenPrincipal)
    if escena == 9:
        escena = Transicion_Casa_Super_Izquierda(screenPrincipal, velocidadTransiciones)
    if escena == 10:
        escena = Transicion_Casa_Liverpool_Derecha(screenPrincipal, velocidadTransiciones)
    if escena == 11:
        escena = Supermercado(screenPrincipal)
    if escena == 12:
        escena = Transicion_Casa_Super_Derecha(screenPrincipal, velocidadTransiciones)
    if escena == 13:
        escena = Liverpool(screenPrincipal)
    if escena == 14:
        escena = Transicion_Casa_Liverpool_Izquierda(screenPrincipal, velocidadTransiciones)
    if escena == 15:
        escena = OpcionesSupermercado(screenPrincipal, True)
    if escena == 16:
        escena,dineroActual = Supermercado_Comprar(screenPrincipal,dineroActual)
    if escena == 17:
        escena,buenas,malas,nivel = Supermercado_TrabajarNivel1(screenPrincipal)
    if escena == 18:
        escena,buenas,malas,nivel = Supermercado_TrabajarNivel2(screenPrincipal,buenas,malas,nivel)
    if escena == 19:
        escena,dineroActual = JuegoFinalizado(screenPrincipal,buenas)
    if escena == 20:
        escena,dineroActual = InteriorLiverpool(screenPrincipal,dineroActual)
    if escena == 21:
        escena = EscenaFinal(screenPrincipal)