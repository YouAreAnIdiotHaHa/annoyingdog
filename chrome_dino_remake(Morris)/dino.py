import pygame
class Dino:
    def __init__(self):
        self.clickCooldown = 0
        self.direction = 1
        self.img = pygame.image.load("img/dino1.png")
        self.playerSpeed = 18.75/2
        self.playerVelocity = 0
        self.jumpStrength = -30
        self.GRAVITY = 7.5
        self.stamina = 40
        self.healthCap = 10
        self.health = 10
        self.flippedImage = pygame.transform.flip(self.img,flip_x= True, flip_y= False)
        self.staminaRegenCooldown = 0
        self.hitsound = pygame.mixer.Sound("sfx/sfx_hitsound.mp3")
        self.collisionrect = self.img.get_rect(topleft=(0, 640))