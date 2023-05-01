
import pygame, turtle, random, character, background, sys

ZERO = 0
# global variable for game loop
running = True;
speedVar = .075
FRAME_RATE = 60
clock = pygame.time.Clock()
        

# counter for live score
counter = ZERO


def start_screen():
    # Set up the start screen
    font = pygame.font.SysFont(None, 50)
    title = font.render("Racing Simulator", True, (255, 255, 255))
    start_button = pygame.Rect(background.SCREEN_WIDTH/2 - 200/2, background.SCREEN_HEIGHT/2, 200, 50)
    button_color = (ZERO, ZERO, 255)
    text_color = (255, 255, 255)

    # Wait for the user to click the start button
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if start_button.collidepoint(event.pos):
                    return  # Start the game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Draw the start screen
        background.screen.fill((ZERO, ZERO, ZERO))
        background.screen.blit(title, (background.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        pygame.draw.rect(background.screen, button_color, start_button)

        font = pygame.font.SysFont(None, 30)
        start_text = font.render("Start", True, text_color)
        background.screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                                  start_button.y + start_button.height // 2 - start_text.get_height() // 2))
        
        pygame.display.update()


# Initialize Game
pygame.init()
screenColor = (255, 255, 255)
background.screen.fill(screenColor)
screen_rect = background.screen.get_rect()

top = pygame.Rect(ZERO, ZERO, 1400, 800)
grass = pygame.Rect(ZERO, 400, 1000, 100)
background.Track.initTrack(background.Track, "track.webp", 0, 0)

character.Car.initCar(character.Car, "racecar.svg", 200, 200, 10)
character.CarAcc.initCar(character.CarAcc, "racecar3.png", 40, 125, 10)
character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, 100, 100)

# Show start screen
start_screen()

# Create an array for Cop Cars 
CopCars = []


# Car movements
def moveCar(speed):
    keys = pygame.key.get_pressed()
    # move left, right, up, down
    if keys[pygame.K_LEFT]:
        character.Car.rect.move_ip(-speed, ZERO)
        character.CarAcc.rect.move_ip(-speed, ZERO)


    elif keys[pygame.K_RIGHT]:
        character.Car.rect.move_ip(speed, ZERO)
        character.CarAcc.rect.move_ip(speed, ZERO)
        character.CarAcc.draw(character.CarAcc, background.screen)

    elif keys[pygame.K_UP]:
        character.Car.rect.move_ip(ZERO, -speed)
        character.CarAcc.rect.move_ip(ZERO, -speed)


    elif keys[pygame.K_DOWN]:
        character.Car.rect.move_ip(ZERO, speed)
        character.CarAcc.rect.move_ip(ZERO, speed)




# Function to end the game when collision detected
def game_over():
    end_screen = pygame.Surface(background.SCREEN_SIZE)
    end_screen.fill((0,0,0))
    font = pygame.font.Font(None, 50)

    text = font.render("CRASH! GAME OVER!", True, (255, ZERO, ZERO))
    text_rect = text.get_rect(center=(background.SCREEN_WIDTH / 2, (background.SCREEN_HEIGHT / 2) - 100))
    #text2 = font.render("PRESS R TO RESTART", True, (255, ZERO, ZERO))
    #text2_rect = text.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 100))
    text3 = font.render("PRESS M TO RETURN TO MAIN MENU", True, (255, ZERO, ZERO))
    text3_rect = text.get_rect(center=(background.SCREEN_WIDTH / 2, (background.SCREEN_HEIGHT / 2) + 200))
    
    background.screen.blit(end_screen, (0,0))
    background.screen.blit(text, text_rect)
    #screen.blit(text2, text2_rect)
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
    pygame.display.set_caption("Air Time: " + str(counter))
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background.Track.draw(background.Track)
    character.Car.draw(character.Car, background.screen)
    moveCar(character.Car.speed)

    #This part is for the Cop Cars 
    if (len(CopCars) < 1):
        character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, random.randint(10, 790), 10)
        #CopCar.initCar(CopCar, "p-car-top-view-hi.png", SCREEN_WIDTH, 10, 100)

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
