import pygame

class Enemies:
    def __init__(self, img, img2, spawnRangeMin, spawnRangeMax, attack, health, speed, location_y):
        self.img = pygame.image.load(img)
        self.img2 = pygame.image.load(img2)
        self.spawnRangeMin = spawnRangeMin
        self.spawnRangeMax = spawnRangeMax
        self.attack = attack
        self.health = health
        self.speed = speed
        self.location_x = 1300
        self.location_y = location_y
        self.collisionrect = self.img.get_rect(topleft = (1300, location_y))

    # def attack(self):
    #     return attack