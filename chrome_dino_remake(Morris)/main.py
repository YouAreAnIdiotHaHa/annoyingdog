# Game setup
import pygame
from dino import Dino
from enemies import Enemies

# pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
isRunning = False
dino = Dino()
birdstate = 0
dino.img_original = dino.img
ground = pygame.image.load("img/ground.png")
obstacle = pygame.image.load("img/obstacle.png")
attack = pygame.image.load("img/attack.png")
pygame.font.init()
textFont = pygame.font.SysFont("Comic Sans MS", 25)
text_surface = textFont.render("Health:"+str(dino.health)  , False, (255,0,0))

bird_img0 = pygame.image.load("img/bird0.png")

attack_rect = attack.get_rect()
enemies_spawned = []


pygame.mixer.music.load("mus/mus_normal.mp3")
pygame.mixer.music.play(loops=-1)
test_variable = 0
###################################################################################################################


while running:
    # Game main code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # player_pos = sheet_rect

    # if event.type == pygame.KEYDOWN:
    #     if event.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        dino.x -= dino.playerSpeed
        dino.direction = 0
        dino.playerSpeed = 18.75/2
        dino.img = dino.flippedImage

    if keys[pygame.K_d]:
        dino.x += dino.playerSpeed
        dino.direction = 1
        dino.playerSpeed = 18.75/2
        dino.img = dino.img_original
    if keys[pygame.K_LSHIFT]:
        if dino.stamina > 1:
            dino.playerSpeed = 18.75
            dino.stamina -= 1
            dino.jumpStrength = -50
            isRunning = True
        else:
            if dino.stamina < 20:
                dino.stamina += 1
            dino.staminaRegenCooldown = 5
            isRunning = False
    if keys[pygame.K_z]:
        bird = Enemies(img="img/bird0.png",img2="img/bird1.png",spawnRangeMin=0,spawnRangeMax=5,attack=1,health=5,speed=10)
        enemies_spawned.append(bird)
        print(enemies_spawned)

#CLick
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        if dino.clickCooldown == 0:
            dino.clickCooldown = 5
            dino.hitsound.play()

#CLick.end

    if dino.y == 640:
        if keys[pygame.K_SPACE]:
            dino.playerVelocity = dino.jumpStrength

    if keys[pygame.K_DOWN]:
        pass

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    if dino.y >= 641:
        dino.y = 640
        dino.playerVelocity = 0
    else:
        if dino.y < 640:
            dino.y += dino.GRAVITY

    screen.blit(ground, (0, 650))
    dino.y += dino.playerVelocity
    if dino.playerVelocity != 0:
        dino.playerVelocity += dino.GRAVITY

    screen.blit(dino.img, (dino.x, dino.y) )
    pygame.draw.rect(screen, "blue", pygame.Rect(30, 30, 202, 30), border_radius= 8)
    pygame.draw.rect(screen, "darkblue", pygame.Rect(31, 31, 200, 28), border_radius=8)
    pygame.draw.rect(screen, "lightblue", pygame.Rect(31, 31, dino.stamina*5, 28), border_radius=8)
    screen.blit(text_surface, (1000, 30))
    pygame.time.delay(50)
    if not isRunning and dino.staminaRegenCooldown == 0 and not keys[pygame.K_LSHIFT]:
        if 40 > dino.stamina:
            dino.stamina += 0.5
    isRunning = False

    if dino.clickCooldown > 0:
        if dino.direction == 0:
            attack_rect.topleft = (dino.x - 40, dino.y)
        else:
            attack_rect.topleft = (dino.x + 40, dino.y)
        dino.clickCooldown -= 1
    if dino.clickCooldown >= 3:
        screen.blit(attack, attack_rect)

    dino.jumpStrength = -30
    if len(enemies_spawned):
        if birdstate%2 == 0:
            screen.blit(enemies_spawned[0].img, (enemies_spawned[0].spawnLocation_x, 500))
        else:
            screen.blit(enemies_spawned[0].img2, (enemies_spawned[0].spawnLocation_x, 500))
        birdstate += 1
        enemies_spawned[0].spawnLocation_x -= 10

    if dino.staminaRegenCooldown > 0:
        dino.staminaRegenCooldown -= 1



    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
