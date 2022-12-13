import pygame
import caméraUCG
import Utils
from Player import Player

player = None
bg = None
new_bg = None
camera_x = None
camera_y = None
window_width = 1280 
window_height = 720


def main():
    global new_bg, player, bg, window_width, window_height, camera_x, camera_y
    pygame.init()
   
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("UNTITLED CUBE GAME")

    last_update_date = Utils.get_current_time_millis()
    bg = pygame.image.load("background.jpg").convert()
    new_bg = pygame.transform.scale(bg, (1280, 720))
    player = Player(20, 20)
     
    window_width = pygame.display.get_surface().get_size()[0]
    window_height = pygame.display.get_surface().get_size()[1]
    camera_x = window_width / 2
    camera_y = window_height / 2
        
    run = True
    while run:
        pos_playerx= player.get_x()
        pos_playerx += 0.1
        camera_x = camera_x + 0.1
    
        time_diff = Utils.get_current_time_millis() - last_update_date
        if time_diff >= 1000 / 120:
            last_update_date = Utils.get_current_time_millis()
            player.update(window_height)
            render(screen)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if player.get_IsOnGround(window_height):
                    if event.key == pygame.K_SPACE:
                         player.set_velocity_y(-3.5)
    

def render(screen):
    global player
    screen.blit(new_bg, (0,0))
    player.render(screen)

def get_render_x(world_x):
    global window_width, camera_x
    return window_width / 2 + world_x - camera_x
    

def get_render_y(world_y):
    global window_height, camera_y
    return window_height / 2 + world_y - camera_y
    
if __name__ == "__main__":
    main()

