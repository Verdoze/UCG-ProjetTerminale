import pygame

class Player():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("square.png").convert_alpha()
        self.transformed_image = None
        self.velocity_y = 0
        self.const_height = 60
        self.IsOnGround = True
        self.velocity_x = 0.8

    def render(self, screen):
        self.calculate_transformed_image()

        screen.blit(self.transformed_image, (self.x, self.y))

    def update(self, window_height):
        global camera_x
        self.y += self.velocity_y # a chaque instant, on ajoute la vitesse a la position du player (pour qu'il tombe)

        self.velocity_y += 0.1 # a chaque instant, on fait augmenter la vitesse
        
        self.x += self.velocity_x
        camera_x = self.x
        
        if self.y >= window_height - Player.get_const_height(self):
            self.set_velocity_y(0)
            self.y = window_height - Player.get_const_height(self)

    def calculate_transformed_image(self):
        self.transformed_image = pygame.transform.scale(self.img, (40, 40))

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.y = new_y

    def get_velocity_y(self):
        return self.velocity_y

    def set_velocity_y(self, new_velocity_y):
        self.velocity_y = new_velocity_y

    def get_const_height(self):
        return self.const_height

    def get_IsOnGround(self, window_height):
        if self.y >= window_height - Player.get_const_height(self):
            self.IsOnGround = True
        elif self.y <= window_height - Player.get_const_height(self):
            self.IsOnGround = False
        return self.IsOnGround