import pygame
from constants import * 
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    base_clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    Player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField_1 = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(("black"))
        
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(Player_1):
                print("Kolizja, naura")
                return

        pygame.display.flip()
        dt = base_clock.tick(60) / 1000

    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()