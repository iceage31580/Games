#pygame module to be used
import pygame
#starts pygame
pygame.init()

#windows function open window to play game in
#width and height of game
win = pygame.display.set_mode((1000, 1000))

#We want to give our program a proper na         me
pygame.display.set_caption('First Game')

#screenWidth = 500

#pygame.path.join for using other folders
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png')]
bg = pygame.image.load(r'C:\Users\Isaac\PyCharmMiscProject\bg.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self,win):
        if self.walkCount + 1>= 27:
            self.WalkCount = 0


        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.WalkCount//3],(self.x,self.y))
                self.WalkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                    win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))
            ## win.blit(char, (self.x,self.y))

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png')]
    walkLeft = [pygame.image.load('L1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end] #character will be moving on x axis, if it were up and down, it would move y axis
        self.walkCount = 0
        self.vel = 3

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 33: #how we determine where the animation is going (left or right)
            self.walkCount = 0

        if self.vel > 0: #moving right
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        #pass
        #instance needs to be created



    def move(self):
        if self.vel > 0: #character moving right
            if self.x + self.vel < self.path[1]: #basically when we get to the end of the path
                self.x += self.vel
            else:
                self. vel = self.vel * -1
                self.walkCount = 0
        else:           # character starts moving left after "runs out"
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
        pass


def redraw_game_window() :
    win.blit(bg, (0, 0))#must go before other functions
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    ##global walkCount
    # win.fill((0, 0, 0))

    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    ##if man.walkCount + 1 >= 27:
    ##    man.walkCount = 0
    ##if man.left:
    ##    win.blit(walkLeft[man.walkCount // 3], (man.x, man.y))
    ##    man.walkCount += 1
    ##elif man.right:
    ##    win.blit(walkRight[man.walkCount // 3], (man.x, man.y))
    ##    man.walkCount += 1
    ##else:
    ##    win.blit(char, (man.x, man.y))

    pygame.display.update()


#main loop

#All Pygames have a main loop
#Delay to keep window closed
#event checks for events
#pygame.quit is the red x button
man = player(300,410,64,64)#instance of the sprite
goblin = enemy(100, 410, 64, 64,450)#instance of enemy created in main loop
bullets = [] #List for projectiles
run = True
while run:
    #pygame.time.delay(27) #framerate
    clock.tick(27)
    redraw_game_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0: #500 comes from the width of the screen
            bullet.x -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) # bullets will be deleted(pop deletes)

#keys will allow movement
#0,0 is top left
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
             facing = -1
        else:
            facing = 1
        if len(bullets) < 5: # how many projectiles on screen
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height), 6 , (0,255,0), facing))  #round so it won't mess up (13:36 https://www.youtube.com/watch?v=PVY46hUp2EM&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=5)

    #adding "and" statements to constrict square
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False#stablize character
    #I can use a global variable for Screen Width to put here. I'll comment in a global variable
    #from if to elif so I can add an else
        man.standing = False # was added after projectile function
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        #man.right = False
        #man.left = False
        #If we reset these, then we won't know what way he is looking
        man.walkCount =0


    if not(man.isJump):
        #if keys[pygame.K_UP] and y > vel:
            #y -= vel
        #if keys[pygame.K_DOWN] and y < 500 - height - vel:
            #y += vel
    #will be adding code to use space for jumping
    #uses math y = mx + b
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1 # first part of jump nothing is going on
            if man.jumpCount < 0:
                neg = -1 # this is declared so we can multiply it after the jump to bring it down
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
            #this moves character up, now we gotta make character come down
        else:
            man.isJump = False
            man.jumpCount = 10



pygame.quit()


##notes from Character Animation Sprite

##For people who have custom sprites I suggest this at the beginning of the file:
##from pygame import image as img
##Then instead of
##walk_right = [pygame.image.load("Custom sprite.png")]
##It's
##walk_right = [img.load("Custom sprite.png")]"

##just for anyone having trouble with the images if you are storing the image in the same folder as the python program
##I created a variable for  directory path using
##folder = os.path.dirname(__file__)
##and then
##pygame.image.load(os.path.join(folder,'bg.png'))
##also dont forget to import the os module
##I was having trouble with this as well so hope this helps

#notes from Optimization & OOP
#Character needs to have a width and a height
#character needs a velocity
#needs to fit inside window
#x = 50
#y = 440
#width = 64
#height = 64
#vel = 10
#left = False
#right = False
#walkCount = 0
#jumpcode
#isJump = False
#jumpCount = 10
