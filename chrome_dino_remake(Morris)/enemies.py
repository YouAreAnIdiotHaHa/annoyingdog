import pygame

class Enemies:
    def __init__(self, img, img2, spawnRangeMin, spawnRangeMax, attack, health, speed):
        self.img = pygame.image.load(img)
        self.img2 = pygame.image.load(img2)
        self.spawnRangeMin = spawnRangeMin
        self.spawnRangeMax = spawnRangeMax
        self.attack = attack
        self.health = health
        self.speed = speed
        self.spawnLocation_x = 1300

    # def attack(self):
    #     return attack