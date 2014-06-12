import pygame

class Game(object):
	def main(self, screen):
		clock = pygame.time.Clock()
		image = pygame.image.load('naruto.png')

		naruto_title_image = pygame.image.load('naruto_shippuden.png')
		naruto_title_image = pygame.transform.scale(naruto_title_image,(int(600/1.2),int(340/1.2)))
		differenece = 500
		pygame.mixer.music.load('naruto_battle_music.mp3')
		pygame.mixer.music.play(0)
		while 1:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN \
					and event.key == pygame.K_ESCAPE:
					return

			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				image_x -= differenece
			if key[pygame.K_RIGHT]:
				image_x += differenece
			if key[pygame.K_UP]:
				image_y -=  differenece
			if key[pygame.K_DOWN]:
				image_y +=  differenece

			screen.fill((255,255,255))
			screen.blit(image,((400,0)))
			screen.blit(naruto_title_image,(100,400))
			pygame.display.flip()



if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((1614,1025))
	Game().main(screen)