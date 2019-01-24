import pygame
def main():
	pygame.init()
	logo = pygame.image.load("logo32x32.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("minimal program")
	
	screen = pygame.display.set_mode((240,180))
	
	running = True
	
	background = pygame.image.load("background.png")
	screen.blit(background, (0,0))
	image01 = pygame.image.load("01_image.png")
	
	image01.set_colorkey((255,255,255))
	#screen.blit(image01, (50,50))
	pygame.display.flip()
	xpos = 50
	ypos = 50
	step_x = 10
	step_y = 10
	
	_update = pygame.sprite.RenderUpdates()
	_update.add(image01)
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		#screen.blit(background, (0,0))
		#screen.blit(image01, (xpos,ypos))
		
		#pygame.display.flip()
		if xpos >208 or xpos < 0:
			step_x = -step_x
		if ypos >148 or ypos<0 :
			step_y = -step_y
		xpos +=step_x
		ypos +=step_y
		_update.draw()
		
		
if __name__ == "__main__":
	main()
