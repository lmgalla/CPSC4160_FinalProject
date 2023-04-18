
import pygame, turtle, random

ZERO = 0
# global variable for game loop
running = True;
speedVar = .075

# Create Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(SCREEN_SIZE)


#class for the background / track
class Track: 
    def initTrack(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        new_size = (800, 1400)
        self.image = pygame.transform.scale(self.image, new_size)
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)
        


# Create Car Class
class Car:
    def initCar(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        new_size = (200, 100)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed

    def draw(self, surface):
        screen.blit(self.image, self.rect)


class CarAcc:
    def initCar(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        new_size = (500, 250)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        

    def draw(self, surface):
        screen.blit(self.image, self.rect)

    
    def update(self, speed):
        self.rect.x -= -speed

#Class for cop cars / obstacles 
class CopCar():
    def initCar(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        new_size = (200, 100)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        

    def draw(self, surface):
        pygame.Surface.blit(surface, self.image, self.rect)

    
    def update(self, speed):
        self.rect.x -= -speed

# counter for live score
counter = ZERO


def start_screen():
    # Set up the start screen
    font = pygame.font.SysFont(None, 50)
    title = font.render("Racing Simulator", True, (255, 255, 255))
    start_button = pygame.Rect(SCREEN_WIDTH/2 - 200/2, SCREEN_HEIGHT/2, 200, 50)
    button_color = (ZERO, ZERO, 255)
    text_color = (255, 255, 255)

    # Calculate the center of the screen
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Calculate the position of the start button to center it
    start_button.center = (center_x, center_y)

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
        screen.fill((ZERO, ZERO, ZERO))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        pygame.draw.rect(screen, button_color, start_button)
        font = pygame.font.SysFont(None, 30)
        start_text = font.render("Start", True, text_color)
        screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                                  start_button.y + start_button.height // 2 - start_text.get_height() // 2))
        
        pygame.display.update()


# Initialize Game
pygame.init()
screenColor = (255, 255, 255)
screen.fill(screenColor)
screen_rect = screen.get_rect()

top = pygame.Rect(ZERO, ZERO, 1400, 800)
grass = pygame.Rect(ZERO, 400, 1000, 100)
Track.initTrack(Track, "track.webp", 0, 0)

Car.initCar(Car, "racecar.svg", 200, 200, 10)
CarAcc.initCar(CarAcc, "racecar3.png", 40, 125, 10)
CopCar.initCar(CopCar, "p-car-top-view-hi.png", SCREEN_WIDTH, 100, 100)

# Show start screen
start_screen()

# Create an array for Cop Cars 
CopCars = []


# Car movements
def moveCar(speed):
    keys = pygame.key.get_pressed()
    # move left, right, up, down
    if keys[pygame.K_LEFT]:
        Car.rect.move_ip(-speed, ZERO)
        CarAcc.rect.move_ip(-speed, ZERO)


    elif keys[pygame.K_RIGHT]:
        Car.rect.move_ip(speed, ZERO)
        CarAcc.rect.move_ip(speed, ZERO)
        CarAcc.draw(CarAcc, screen)

    elif keys[pygame.K_UP]:
        Car.rect.move_ip(ZERO, -speed)
        CarAcc.rect.move_ip(ZERO, -speed)


    elif keys[pygame.K_DOWN]:
        Car.rect.move_ip(ZERO, speed)
        CarAcc.rect.move_ip(ZERO, speed)




# Function to end the game when collision detected
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("CRASH! GAME OVER!", True, (255, ZERO, ZERO))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.update()


# Game Loop
obstacle_timer = pygame.time.get_ticks()

while running:
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
    
    Track.draw(Track)
    Car.draw(Car,screen)
    moveCar(Car.speed)

    #This part is for the Cop Cars 
    if (len(CopCars) < 1):
        CopCar.initCar(CopCar, "p-car-top-view-hi.png", SCREEN_WIDTH, random.randint(10, 790), 10)
        #CopCar.initCar(CopCar, "p-car-top-view-hi.png", SCREEN_WIDTH, 10, 100)

        CopCars.append(CopCar)

    for CopCar in CopCars:
        #CopCar.update(CopCar, 10 - (counter*speedVar))
        CopCar.update(CopCar, -10)
        if(CopCar.rect.x < 0):
            CopCars.remove(CopCar)
        
    if CopCar.rect.colliderect(Car.rect):
        print("collision")
        game_over()
        
    
    
    CopCar.draw(CopCar, screen)

    pygame.display.update()
    

    Car.rect.clamp_ip(top)  # ensure player is inside screen

# Loop Exited
pygame.quit()