import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def check_collision(self, CircleShape):
        positionnumerique_objet1 = pygame.math.Vector2.distance_to(self.position,CircleShape.position)
        #print(f"{positionnumerique_objet1}")
        if(positionnumerique_objet1 < self.radius + CircleShape.radius):
            #print(f"collision {self.radius} {CircleShape.radius}")
            return True
        return False

