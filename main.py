
import pygame, turtle, random, character, background, sys, vars

# global variable for game loop
running = True;
speedVar = .075
FRAME_RATE = 60
clock = pygame.time.Clock()
        

# counter for live score
counter = vars.ZERO

# Initialize Game
pygame.init()
screenColor = (255, 255, 255)
background.screen.fill(screenColor)
screen_rect = background.screen.get_rect()

top = pygame.Rect(vars.ZERO, vars.ZERO, 1400, 800)
grass = pygame.Rect(vars.ZERO, 400, 1000, 100)
background.Track.initTrack(background.Track, "images.png", 0, 0)


character.Car.initCar(character.Car, "racecar.svg", 200, 200, 10)
character.CarAcc.initCar(character.CarAcc, "racecar3.png", 40, 125, 10)
character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, 100, 100)

# Show start screen
background.start_screen()

# Create an array for Cop Cars 
CopCars = []


# Car movements
def moveCar(speed):
    keys = pygame.key.get_pressed()
    # move left, right, up, down
    if keys[pygame.K_LEFT]:
        character.Car.rect.move_ip(-speed, vars.ZERO)
        character.CarAcc.rect.move_ip(-speed, vars.ZERO)


    elif keys[pygame.K_RIGHT]:
        character.Car.rect.move_ip(speed, vars.ZERO)
        character.CarAcc.rect.move_ip(speed, vars.ZERO)
        character.CarAcc.draw(character.CarAcc, background.screen)

    elif keys[pygame.K_UP]:
        character.Car.rect.move_ip(vars.ZERO, -speed)
        character.CarAcc.rect.move_ip(vars.ZERO, -speed)


    elif keys[pygame.K_DOWN]:
        character.Car.rect.move_ip(vars.ZERO, speed)
        character.CarAcc.rect.move_ip(vars.ZERO, speed)




# Function to end the game when collision detected
def game_over():
    end_screen = pygame.Surface(background.SCREEN_SIZE)
    end_screen.fill((0,0,0))
    font = pygame.font.Font(None, 50)

    text = font.render("CRASH! GAME OVER!", True, (255, vars.ZERO, vars.ZERO))
    text_rect = text.get_rect(center=(background.SCREEN_WIDTH / 2, (background.SCREEN_HEIGHT / 2) - 100))
    text3 = font.render("PRESS M TO RETURN TO MAIN MENU", True, (255, vars.ZERO, vars.ZERO))
    text3_rect = text.get_rect(center=(background.SCREEN_WIDTH / 2, (background.SCREEN_HEIGHT / 2) + 200))
    
    background.screen.blit(end_screen, (0,0))
    background.screen.blit(text, text_rect)
    background.screen.blit(text3, text3_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    start_screen()
                    exit()




# Game Loop
obstacle_timer = pygame.time.get_ticks()

while running:
    clock.tick(FRAME_RATE)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_x:
                pygame.quit()
                sys.exit()

    pygame.display.set_caption("Air Time: " + str(counter))
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    vars.xVar-=10
    background.Track.draw(background.Track)
    character.Car.draw(character.Car, background.screen)
    moveCar(character.Car.speed)

    #This part is for the Cop Cars 
    if (len(CopCars) < 1):
        character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, random.randint(10, 750), 10)
        CopCars.append(character.CopCar)

    for character.CopCar in CopCars:
        #CopCar.update(CopCar, 10 - (counter*speedVar))
        character.CopCar.update(character.CopCar, -10)
        if(character.CopCar.rect.x < 0):
            CopCars.remove(character.CopCar)
    
    character.CopCar.draw(character.CopCar, background.screen)

    pygame.display.update()
    

    character.Car.rect.clamp_ip(top)  # ensure player is inside screen
    
    if character.CopCar.rect.colliderect(character.Car.rect):
        print("collision")
        game_over()
        running = False
    

# Loop Exited
# pygame.quit()
pygame.time.wait(100)
