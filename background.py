import pygame, vars, loop, sys

# Create Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(SCREEN_SIZE)


class CoverImage:
    def initImage(self, image_path):
        self.image = pygame.image.load(image_path)
        new_size = (1400, 800)
        self.image = pygame.transform.scale(self.image, new_size)

    def drawImage(self):
        screen.blit(self.image, (0,0))

#class for the background / track
class Track: 
    def initTrack(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        new_size = (800, 1400)
        self.image = pygame.transform.scale(self.image, new_size)
        self.image = pygame.transform.rotate(self.image, 90)
        self.width = 800
        self.height = 1400
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #screen.blit(self.image, self.rect)

    def draw(self):
        if vars.xVar < -self.width:
            vars.xVar = 0
    
        screen.blit(self.image, (vars.xVar,0))
        screen.blit(self.image, (vars.xVar + self.width, 0))
        

#function needed to display and use start screen
def start_screen():
    CoverImage.initImage(CoverImage, "gameBackground.png")
    CoverImage.drawImage(CoverImage)

    # Set up the start screen
    font = pygame.font.SysFont(None, 100)
    title = font.render("Racing Simulator", True, (vars.ZERO, vars.ZERO, vars.ZERO))
    start_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT-100, 200, 50)
    button_color = (vars.ZERO, vars.ZERO, vars.ZERO)
    text_color = (255, 255, 255)

    # Calculate the center of the screen
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Calculate the position of the start button to center it
    start_button.center = (center_x, SCREEN_HEIGHT-100)

    # Wait for the user to click the start button
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if start_button.collidepoint(event.pos):
                    loop.game_loop()
                    return  # Start the game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Draw the start screen
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        pygame.draw.rect(screen, button_color, start_button)

        font = pygame.font.SysFont(None, 30)
        start_text = font.render("Start", True, text_color)
        screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                                  start_button.y + start_button.height // 2 - start_text.get_height() // 2))
        
        pygame.display.update()


# Function to end the game when collision detected and display the end screen 
def game_over():
    end_screen = pygame.Surface(SCREEN_SIZE)
    end_screen.fill((0,0,0))
    crashFont = pygame.font.Font(None, 100)
    font = pygame.font.Font(None, 50)

    #display text
    text = crashFont.render("CRASH! GAME OVER!", True, (255, vars.ZERO, vars.ZERO))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 200))
    text2 = font.render("PRESS M TO RETURN TO MAIN MENU", True, (255, vars.ZERO, vars.ZERO))
    text2_rect = text.get_rect(center=((SCREEN_WIDTH / 2)+50, (SCREEN_HEIGHT / 2)+100))
    text3 = font.render("PRESS X or ESC to EXIT", True, (255, vars.ZERO, vars.ZERO))
    text3_rect = text.get_rect(center=((SCREEN_WIDTH / 2)+150, (SCREEN_HEIGHT/2) + 200))
    
    screen.blit(end_screen, (0,0))
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    pygame.display.update()

    #loop for end screen awaiting user action 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    loop.reset()
                    start_screen()
                    exit()
                if event.key == pygame.K_x:
                    exit()
                if event.key == pygame.K_ESCAPE:
                    exit()