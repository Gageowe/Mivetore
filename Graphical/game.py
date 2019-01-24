import pygame,time
def main():
	pygame.init()
	logo = pygame.image.load("logo32x32.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("minimal program")
	
	screen = pygame.display.set_mode((960,270))
	
	running = True
	
	background = pygame.image.load("background02.png")
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
	
	lastTime=time.process_time()
	newTime=time.process_time()
	while running:
				newTime=time.process_time()
				since = newTime - lastTime
				if since >= 30 :
						for event in pygame.event.get():
								if event.type == pygame.QUIT:
										running = False
		#screen.blit(background, (0,0))
		#screen.blit(image01, (xpos,ypos))
		
		#pygame.display.flip()
						if xpos >928 or xpos < 0:
								step_x = -step_x
						if ypos >688 or ypos<0 :
								step_y = -step_y
						xpos +=step_x
						ypos +=step_y
						_update.draw()
						lastTime = newTime
		
		
if __name__ == "__main__":
	main()
