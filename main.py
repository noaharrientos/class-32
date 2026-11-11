import pygame
import random 
pygame.init()
screenwidth,screenheight=500,400
movementspeed=5
fontsize=72
backgroundimage=pygame.transform.scale(pygame.image.load("nebula.webp"),(screenwidth,screenheight))
font=pygame.font.SysFont("Times New Roman",fontsize)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("Lime"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x=max(min(self.rect.x+xchange,screenwidth-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+ychange,screenheight-self.rect.height),0)
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("spritecollolision")
allsprites=pygame.sprite.Group()
s1=Sprite(pygame.Color("black"),20,30)
s1.rect.x,s1.rect.y=random.randint(0,screenwidth-s1.rect.width),random.randint(0,screenheight-s1.rect.height)
allsprites.add(s1)
s2=Sprite(pygame.Color("red"),20,30)
s2.rect.x,s2.rect.y=random.randint(0,screenwidth-s2.rect.width),random.randint(0,screenheight-s2.rect.height)
allsprites.add(s2)
running=True
won=False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_x):
            running=False
    if not won:
        keys=pygame.key.get_pressed()
        xchange=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movementspeed
        ychange=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movementspeed
        s1.move(xchange,ychange)
        if s1.rect.colliderect(s2.rect):
            allsprites.remove(s2)
            won=True
    screen.blit(backgroundimage,(0,0))
    allsprites.draw(screen)
    if won:
        text=font.render("you win!",True,pygame.Color("White"))
        screen.blit(text,((screenwidth-text.get_width())//2,(screenheight-text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()