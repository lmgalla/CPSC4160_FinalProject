import pygame

xVar = 0
ZERO = 0
FRAME_RATE = 60
running = True
clock = pygame.time.Clock()
# counter for live score
counter = ZERO
# Create an array for Cop Cars 
CopCars = []
#used in clamp
top = pygame.Rect(ZERO, ZERO, 1400, 800)
#used for the speed of cop cars
#speedVar = .05