import pygame, character, background, random, sys, vars

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


def game_loop():
    while vars.running:
        vars.clock.tick(vars.FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

        pygame.display.set_caption("Air Time: " + str(vars.counter))
        vars.counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        vars.xVar-=10
        background.Track.draw(background.Track)
        character.Car.draw(character.Car, background.screen)
        moveCar(character.Car.speed)

        #This part is for the Cop Cars 
        if (len(vars.CopCars) < 1):
            character.CopCar.initCar(character.CopCar, "p-car-top-view-hi.png", background.SCREEN_WIDTH, random.randint(50, 700), 10)
            vars.CopCars.append(character.CopCar)

        for character.CopCar in vars.CopCars:
            character.CopCar.update(character.CopCar, -8)
            #character.CopCar.update(character.CopCar, -5)
            if(character.CopCar.rect.x < 0):
                vars.CopCars.remove(character.CopCar)
        
        character.CopCar.draw(character.CopCar, background.screen)

        pygame.display.update()
        

        character.Car.rect.clamp_ip(vars.top)  # ensure player is inside screen
        
        if character.CopCar.rect.colliderect(character.Car.rect):
            print("collision")
            background.game_over()
        
def reset():
    character.Car.rect.x = 150
    character.Car.rect.y = 75
    character.CarAcc.rect.x = 0
    character.CarAcc.rect.y = 0
    vars.counter = 0
    vars.CopCars = []

