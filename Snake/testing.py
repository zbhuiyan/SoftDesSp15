import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
direction = 0

screen = pygame.display.set_mode(size)


ballrect = pygame.Rect(50,50,10,10)

while 1:
	for event in pygame.event.get():
           if event.type == pygame.QUIT: sys.exit()

        if pygame.key.get_pressed()[pygame.K_UP] != 0 and direction != 0:
        	direction = 2

        if pygame.key.get_pressed()[pygame.K_DOWN] != 0 and direction != 2:
        	direction = 0

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and direction != 1:
        	direction = 3

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and direction != 3:
        	direction = 1

        #ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        pygame.draw.rect(screen, (0,0,255), ballrect)
        #screen.blit(ball,ballrect)
        pygame.display.flip()