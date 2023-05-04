import background, pygame

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


# Create Acceleration character
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

#Class for cop cars
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

#Class for obstacles 
class cone():
    def initCone(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        new_size = (75, 75)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        

    def draw(self, surface):
        pygame.Surface.blit(surface, self.image, self.rect)

    
    def update(self, speed):
        self.rect.x -= -speed