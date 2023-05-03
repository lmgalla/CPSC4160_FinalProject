import pygame, vars

# Create Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(SCREEN_SIZE)
#x = 0

#class for the background / track
class Track: 
    def initTrack(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        new_size = (800, 1400)
        self.image = pygame.transform.scale(self.image, new_size)
        self.image = pygame.transform.rotate(self.image, 90)
        self.width = 800
        self.height = 14000
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #screen.blit(self.image, self.rect)

    def draw(self):
        if vars.xVar < -self.width:
            vars.xVar = 0
    
        screen.blit(self.image, (vars.xVar,0))
        screen.blit(self.image, (vars.xVar + self.width, 0))
        