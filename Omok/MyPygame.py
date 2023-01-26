import pygame

class MyPygame():
    def __init__(self):
        pygame.init()
    
    def screen_set(self,width,height):
        return pygame.display.set_mode((width,height))

    def screen_name(self, name:str):
        pygame.display.set_caption(name)

    def image_load(self,path:str):
        return pygame.image.load(path)

    def color_transparents(self,target:pygame.Surface,r,g,b):
        target.set_colorkey((r,g,b))
    
    def get_size(self, target:pygame.Surface) -> int:
        size = target.get_rect().size
        return size[0], size[1]
    
    def bilt(self,screen:pygame.Surface,target:pygame.Surface,x,y):
        screen.blit(target,(x,y))

    def mouse_click_pos(self) -> int:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        return x,y
    
    def max_min_click_range(self,args,max):
        if args[0] > max:
            args[0] = max
        elif args[0] < 0:
            args[0] = 0

        if args[1] > max:
            args[1] = max
        elif args[1] < 0:
            args[1] = 0
        return args[0],args[1]
        
    def event_get(self):
        event = pygame.event.get()
        return event

    def event_occur(self, event):
        state = ""
        if event.type == pygame.MOUSEBUTTONUP:
            state = "mouse"
            return state
        elif event.type == pygame.QUIT:
            state = "quit"
            return state
    
    def update(self):
        pygame.display.update()
    
    def finish(self):
        pygame.time.wait(1000)
        pygame.quit()
    

