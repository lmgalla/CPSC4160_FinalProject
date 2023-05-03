
import pygame, turtle, character, background, sys, loop, vars

# global variable for game loop
running = True
clock = pygame.time.Clock()
        

# counter for live score
counter = vars.ZERO

# Initialize Game
pygame.init()
screenColor = (255, 255, 255)
background.screen.fill(screenColor)
screen_rect = background.screen.get_rect()

#init track and characters 
background.Track.initTrack(background.Track, "images.png", 0, 0)
character.Car.initCar(character.Car, "racecar.svg", 200, 200, 10)
character.CarAcc.initCar(character.CarAcc, "racecar3.png", 40, 125, 10)
character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, 100, 100)

# Show start screen
background.start_screen()

# Game Loop
loop.game_loop()

# Loop Exited
# pygame.quit()
pygame.time.wait(100)
