import pygame


# Create Character
class rectangle:
    def char_init(newcolor, height, width, xpos, ypos):
        char = pygame.Rect(xpos, ypos, width, height);
        pygame.draw.rect(pygame.Surface, newcolor, char)




