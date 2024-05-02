import pygame, sys
width = 800
height = 400
#Inicializa módulos (archivos.py)
#Devuelve en tupla: (módulos inicializados, número de módulos que fallaron la inicialización)
check_errors = pygame.init()
game_loop = True
direction = ""
pause = False
center = [width/2, height/2]
#   _________________ Checa errores de inicialización _________________
if check_errors[1] > 0:
    game_loop = False
    print("Inicialization error")
    sys.exit(-1)
else:
    print("Juego interpretado sin errores")
#   _______________ Instancia título, pantalla y reloj _______________

pygame.display.set_caption("Roomie")
window = pygame.display.set_mode((width, height))
fps_controller = pygame.time.Clock()

#   ____________________________ Colores ____________________________
#Color [R, G, B]
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(185, 32, 40)
green = pygame.Color(10, 160, 20)
blue = pygame.Color(20, 187, 215)

#   _______________ Lógica del juego _______________
#   *Ciclo infinito frenado por la variable de reloj fps_controller
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pause == True:
                direction = ""
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                direction = "UP"
            if event.key == ord('a'):
                direction = "LEFT"
            if event.key == ord('d'):
                direction = "RIGHT"
            if event.key == ord('s'):
                direction = "DOWN"
            if event.key == ord('q'):
                direction = "DIAGONAL"

    #Llena toda la pantalla de color
    window.fill(white)

    if direction == "UP":
        center[1] -= 5
        
    if direction == "LEFT":
        center[0] -= 5
        
    if direction == "RIGHT":
        center[0] += 5
        
    if direction == "DOWN":
        center[1] += 5
    
    if direction == "DIAGONAL":
        center[1] -= 5
        center[0] -= 5
        
    #Obtiene la posición del cursor
    cursor_posicion = pygame.mouse.get_pos()
    print(cursor_posicion)
    if cursor_posicion[0] >= center[0] - 20 and cursor_posicion[0] <= center[0] + 20 and cursor_posicion[1] >= center[1] - 20 and cursor_posicion[1] <= center[1] + 20:
        pygame.draw.rect(window, green, pygame.Rect(center[0] - 20, center[1] - 20, 40, 40))
        pause = True
    else:
        pygame.draw.circle(window, red, (center[0], center[1]), 20, 20)
        pause = False
    #Dibuja o actualiza los dibujos
    pygame.display.flip()
    fps_controller.tick(20)

#   _______________ Cierra pygame _______________
pygame.quit()
sys.exit()