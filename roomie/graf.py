import pygame, sys, time, random

difficulty = 20
# Variables del tamaño de la pantalla
frame_size_x = 500
frame_size_y = 500

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Had errors")
    #Cierra el programa
    sys.exit(-1)
else:
    print("Game successfully interpreted")

#Título del juego
pygame.display.set_caption('Test game')
#Características de la pantalla
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

#Color [R, G, B]
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(250, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock()



# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            pass

    # GFX
    game_window.fill(white)

    # Snake food
    #pygame.draw.rect(game_window, black, pygame.Rect(100, 100, 10, 10))
    
    for y in range(0, 500, 50):
        pygame.draw.line(game_window, black, (0, y), (500, y), 2)
    for x in range(0, 500, 50):
        pygame.draw.line(game_window, red, (x, 0), (x, 500), 2)

    # Refresh game screen for specific area in the frame if any arguments are added
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)