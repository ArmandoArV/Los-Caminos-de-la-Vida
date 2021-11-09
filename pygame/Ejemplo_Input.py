import Input
from pygame import *
import pygame

init()
textinput = Input.TextInput(font_family="Calibri", font_size=40, text_color=(0, 0, 0),initial_string="")
screen = pygame.display.set_mode((1000, 200))
k=1
while True:
    screen.fill((225, 225, 225))

    eventos = pygame.event.get() 
    for e in eventos:
        if e.type == QUIT: exit()
    
    if textinput.update(eventos):
        print(eventos)
        print("Enter presionado")
        print(textinput.get_text())
        textinput.clear_text()
    if k==1:            
        screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.flip()