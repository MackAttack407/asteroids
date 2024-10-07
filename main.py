import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	#add player objects to groups updatable and drawable
	updatable.add(player)
	drawable.add(player)
	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	#main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			player.shoot()
			
		#clears the screen before drawing new lines
		screen.fill("black")


		for obj in updatable:
			obj.update(dt)
		
		#checks if player collides with asteroid and closes game if true
		for obj in asteroids:
			if obj.collisions(player):
				print("Game over!")
				pygame.quit()
				sys.exit()

		for obj in drawable:
			obj.draw(screen)
	
		#checks if bullet collides with asteroid
		for bullet in shots:
			for asteroid in asteroids:
				if bullet.collisions(asteroid):
					bullet.kill()
					asteroid.split()
		

		pygame.display.flip()
		
		#limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000	

if __name__ == "__main__":
	main()


