from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = velocity 
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)