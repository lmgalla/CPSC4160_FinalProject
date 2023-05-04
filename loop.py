import pygame, character, background, random, sys, vars, time

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

        pygame.display.set_caption("Distance: " + str(vars.counter))
        vars.counter += 1
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
            if(character.CopCar.rect.x < 0):
                vars.CopCars.remove(character.CopCar)

        character.CopCar.draw(character.CopCar, background.screen)

        #This is nearly identical to the code for the cop cars except for the speed
        if (len(vars.Cones) < 1):
            pygame.time.wait(10)
            character.cone.initCone(character.cone, "cone.png", background.SCREEN_WIDTH, random.randint(25, 725), 10)
            vars.Cones.append(character.cone)

        for character.cone in vars.Cones:
            character.cone.update(character.cone, -10)
            if(character.cone.rect.x < 0):
                vars.Cones.remove(character.cone)

        character.cone.draw(character.cone, background.screen)
        pygame.display.update()
        
        character.Car.rect.clamp_ip(vars.top)  # ensure player is inside screen
        
        #Code for collisions of objects 
        if character.CopCar.rect.colliderect(character.Car.rect):
            print("cop car collision")
            background.game_over()

        if character.cone.rect.colliderect(character.CopCar.rect):
            vars.Cones.remove(character.cone)

        if character.cone.rect.colliderect(character.Car.rect):
            print("cone collision")
            background.game_over()
            

#used to reset the game upon reset
def reset():
    character.Car.rect.x = 150
    character.Car.rect.y = 75
    character.CarAcc.rect.x = 0
    character.CarAcc.rect.y = 0
    vars.counter = 0
    vars.CopCars = []
    vars.Cones = []

