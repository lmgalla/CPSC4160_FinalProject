import background, pygame

#screen = pygame.display.set_mode(SCREEN_SIZE)

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
        background.screen.blit(self.image, self.rect)


# Create Character
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
        background.screen.blit(self.image, self.rect)

    
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