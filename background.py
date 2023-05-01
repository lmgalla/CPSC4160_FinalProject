import pygame

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