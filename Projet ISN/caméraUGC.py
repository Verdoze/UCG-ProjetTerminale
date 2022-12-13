import pygame

window_width = None
window_height = None
camera_x = None
camera_y = None

def main():
    global window_width, window_height, camera_x, camera_y

    pygame.init()
    screen = pygame.display.set_mode((1550,800))
    pygame.display.set_caption("Le nom de ton jeu")
    
    window_width = pygame.display.get_surface().get_size()[0]
    window_height = pygame.display.get_surface().get_size()[1]
    camera_x = window_width / 2
    camera_y = window_height / 2
    
    image = pygame.image.load("bg.jpg").convert()
    
    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        camera_x = camera_x + 0.1

        screen.blit(image, (get_render_x(0), get_render_y(0)))
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (get_render_x(camera_x-window_height+250), get_render_y(camera_y+175), 50, 50))
        pygame.display.update()
        
        


def get_render_x(world_x):
    global window_width, camera_x
    return window_width / 2 + world_x - camera_x
    

def get_render_y(world_y):
    global window_height, camera_y
    return window_height / 2 + world_y - camera_y
    



if __name__ == "__main__":
    main()