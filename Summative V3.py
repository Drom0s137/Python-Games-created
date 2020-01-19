from pygame import * 
import random
init()
#screen and variables initialization setup**************************************
size = width, height = 1000, 700
screen = display.set_mode(size)
button = 0
pos = 0
page = 0
charx = 500
chary= 350
gameTimer = 0
vitality = 100
#booleans setup*****************************************************************
running = True
up = False
left = False 
down = False
right = False
fire = False
rightfire = False
leftfire = False
upfire = False
downfire = False

#colors*************************************************************************
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,180,4)

#font and clock setup***********************************************************
myFont = font.SysFont("Times New Roman",20)
myClock = time.Clock()
#list setup*********************************************************************
bulletx = []
bullety = []
directionList = [] 
monsterx = [] 
monstery = []
enemyPic = []
potionx = []
potiony = []
#file setup
#numFile = open ("in.dat", "w")
#image setup********************************************************************
#character face right setup***********************
characterr = image.load("survivor-idle_knife_0.png")
characterr = transform.scale(characterr, (70, 70))
#character face right setup***********************
characterd = image.load("survivor-idle_knife_0 down.png")
characterd = transform.scale(characterd, (70, 70))
#character face right setup***********************
characterl = image.load("survivor-idle_knife_left.png")
characterl = transform.scale(characterl, (70, 70))
#character face right setup***********************
characteru = image.load("survivor-idle_knife_up.png")
characteru = transform.scale(characteru, (70, 70))
#ewaste setup*************************************
ewaste = image.load("ewaste-newsletter-300x236.png")
ewaste = transform.scale(ewaste, (100, 100))
#menu background setup****************************
background = image.load("garbage_city_1274105.jpg")
background = transform.scale(background,(1000,700))
#field background setup***************************
mainbackground = image.load("dirt.jpg")
mainbackground = transform.scale(mainbackground,(1000,700))
#monster setup************************************
monster = image.load("monster4.png")
monster = transform.scale(monster,(70,70))
monster1 = image.load("monster 1.png")
monster1 = transform.scale(monster1,(70,70))
monster2 = image.load("monster 2.png")
monster2 = transform.scale(monster2,(70,70))
monster3 = image.load("monster 3.png")
monster3 = transform.scale(monster3,(70,70))
#end screen e=waste
endwaste = image.load("ewaste101.png")
endwaste = transform.scale(endwaste,(300,300))
#uparrow setup
ups = image.load("up.png")
ups = transform.scale(ups,(100,100))
#down arrow setup
downs = image.load("down.png")
downs = transform.scale(downs,(100,100))
#left arrow setup
lefts = image.load("left.png")
lefts = transform.scale(lefts,(100,100))
#right arrow setup
rights = image.load("right.png")
rights = transform.scale(rights,(100,100))
#space key setup
space = image.load("space.png")
space = transform.scale(space,(100,100))
#potiosn setup
potion = image.load("potion.png")
potion = transform.scale(potion,(30,30))
#shield setup
shield = image.load("shield.png")
shield = transform.scale(shield,(400,400))

#random monster setup 
enemyPic.append(random.choice([monster, monster1, monster2, monster3]))

#modular setup******************************************************************
#menu modular**************************
def drawHomescreen(screen):
        screen.blit(background, Rect(0,0,1000,700))
        #draw.rect(screen, BLACK, (0, 0, width, height))
        draw.rect(screen, BLACK, (20, 20, 200, 50))           # 1st option
        draw.rect(screen, BLACK, (240, 20, 200, 50))           #2nd option
        draw.rect(screen, BLACK, (780, 20, 200, 50))           #3rd optiON
        option1 = "Play" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(105, 30, 200, 100))    #1st option word
        option1 = "How to play" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(290, 30, 200, 100))    #2nd option word
        option1 = "Quit" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(840, 30, 200, 100))    #3rd option word     
        option1 = "Latest survival time:                seconds" 
        text1 = myFont.render(option1, 1, BLACK)
        screen.blit(text1, Rect(20, 100, 200, 100))  
#file read
        numFile = open("in.dat", "r")
        score = numFile.readline()
        #rstrip removes the newline character read at the end of the line
        score = score.rstrip()
        text1 = myFont.render(score, 1, BLACK)
        screen.blit(text1, Rect(200, 100, 50, 20))
        numFile.close()            
        
def changecolor(mx,my):
        if 220 > mx > 20 and  20 < my < 70 :
                draw.rect(screen, BLUE, (20, 20, 200, 50))     # 1st option
        elif 440 > mx > 240 and  20 < my < 70:
                draw.rect(screen, BLUE, (240, 20, 200, 50))
        elif 980 > mx > 780 and  20 < my < 70 :
                draw.rect(screen, BLUE, (780, 20, 200, 50))        
        option1 = "Play" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(105, 30, 200, 100))    #1st option word
        option1 = "How to play" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(290, 30, 200, 100))    #2nd option word
        option1 = "Quit" 
        text1 = myFont.render(option1, 1, WHITE)
        screen.blit(text1, Rect(840, 30, 200, 100))    #3rd option word   
def changecolorback(mx ,my):
#back button****************************
        if 20 < mx < 70 and 660 < my < 680:
                draw.rect(screen, BLUE, (20,660,50,20))
        back = "back"
        text1 = myFont.render(back, 1, BLACK)
        screen.blit(text1, Rect(23, 660, 50, 20))        

def maingame(screen,mx,my):
        global vitality, timers 
#timer
        gameTimer = (time.get_ticks()- timers)/ 1000 
#back button****************************
        draw.rect(screen, WHITE, (0, 0, width, height))
        draw.rect(screen, BLACK, (20,660,50,20))
        back = "back"
        text1 = myFont.render(back, 1, WHITE)
        screen.blit(text1, Rect(23, 660, 50, 20))
        screen.blit(mainbackground, Rect(0,0,1000,700))
#ewaste wall setup
        screen.blit(ewaste, Rect(950,-20,105,78))
        screen.blit(ewaste, Rect(950,20,105,78))
        screen.blit(ewaste, Rect(950,60,105,78))
        screen.blit(ewaste, Rect(950,100,105,78))
        screen.blit(ewaste, Rect(950,140,105,78))
        screen.blit(ewaste, Rect(950,180,105,78))
        screen.blit(ewaste, Rect(950,220,105,78))
        screen.blit(ewaste, Rect(950,260,105,78))
        screen.blit(ewaste, Rect(950,300,105,78))
        screen.blit(ewaste, Rect(950,340,105,78))
        screen.blit(ewaste, Rect(950,380,105,78))
        screen.blit(ewaste, Rect(950,420,105,78))
        screen.blit(ewaste, Rect(950,460,105,78))
        screen.blit(ewaste, Rect(950,500,105,78))
        screen.blit(ewaste, Rect(950,540,105,78))
        screen.blit(ewaste, Rect(950,580,105,78))      
        screen.blit(ewaste, Rect(950,620,105,78))
        screen.blit(ewaste, Rect(950,660,105,78))
        screen.blit(ewaste, Rect(950,700,105,78))
#timer print
        timer = myFont.render(str(gameTimer), 1, WHITE)
        screen.blit(timer, Rect(20, 20, 200, 100))        
#vitality print
        stringvitals = "Wall of ewaste health:"
        vitaltext = myFont.render(stringvitals, 1, WHITE)
        screen.blit(vitaltext, Rect(200, 20, 50, 20))  
        vitals = myFont.render(str(vitality), 1, WHITE)
        screen.blit(vitals, Rect(390, 20, 50, 20))          
#main game******************************
#direction of image setup*****
        if right == True:
                screen.blit(characterr, Rect(charx,chary,105,78))
        elif left == True:
                screen.blit(characterl, Rect(charx,chary,105,78))
        elif up == True:
                screen.blit(characteru, Rect(charx,chary,105,78))
        elif down == True:
                screen.blit(characterd, Rect(charx,chary,105,78))
        else:
                screen.blit(characteru, Rect(charx,chary,105,78))
#bullets setup****************
        if fire == True:
                if right == True:
                        directionList.append(4)
                        bulletx.append(charx)
                        bullety.append(chary)                          
                elif left == True:
                        directionList.append(3)
                        bulletx.append(charx)
                        bullety.append(chary)                          
                elif up == True:
                        directionList.append(1)
                        bulletx.append(charx)
                        bullety.append(chary)                          
                elif down == True: 
                        directionList.append(2)
                        bulletx.append(charx)
                        bullety.append(chary)                          
                else:
                        print("")
        for i in range (len(bulletx)-1,-1,-1):
                draw.rect(screen, RED, (bulletx[i],bullety[i],10,10))
                if directionList[i] == 4:
                        bulletx[i] += 8
                elif directionList[i] == 3:
                        bulletx[i] -= 8
                elif directionList[i] == 1:
                        bullety[i] -= 8 
                elif directionList[i] == 2:
                        bullety[i] += 8        
                if bulletx[i] < 0 or bulletx[i] > 1000 or bullety[i] < 0 or bullety[i] > 700:
                        del(bulletx[i],bullety[i],directionList[i])        
#monster spawn
        spawn = random.randint(0,80)
        rate = int((0.02*gameTimer)+1)
        if spawn == 7:
                for i in range (rate):
                        monsterx.append(0)
                        monstery.append(random.randint(100,600))
                        enemyPic.append(random.choice([monster, monster1, monster2, monster3]))
#potion spawn
        spawnpotion = random.randint(0,1000)
        ratepotion = int((0.02*gameTimer)+1)
        if spawnpotion == 7 :
                for i in range (ratepotion):
                        potionx.append(random.randint(20,800))
                        potiony.append(random.randint(20,680))
#potion setup
        for i in range(len(potionx)-1,-1,-1):
                screen.blit(potion, Rect(potionx[i],potiony[i],105,78))
                if (potionx[i]+30 >= charx >= potionx[i]-30) and (potiony[i]+30 >= chary >= potiony[i]-30):
                        del(potionx[i], potiony[i])
                        vitality += 20
        
#monster setup 
        for i in range (len(monsterx)-1,-1,-1):
                screen.blit(enemyPic[i], Rect(monsterx[i],monstery[i],105,78))
                monsterx[i] += 3        
                if monsterx[i] >= 900:
                        del(monsterx[i],monstery[i],enemyPic[i])
                        vitality -= 20
                if vitality <= 0 :
                #file write
                        timeFile = open("in.dat", "w")
                        if gameTimer >= 0:
                                timeFile.write(str(gameTimer))        
                        timeFile.close()   
                for j in range(len(bulletx)-1,-1,-1):
                        if (monsterx[i]+50 >= bulletx[j] >= monsterx[i]) and (monstery[i]+78 >= bullety[j] >= monstery[i]):
                                del(monsterx[i], monstery[i], bulletx[j], bullety[j], directionList[j],enemyPic[i])
                                break


    
    
def howtoplay(screen):
#back button****************************
        draw.rect(screen, WHITE, (0, 0, width, height))
        draw.rect(screen, WHITE, (20,660,50,20))
        back = "back"
        text1 = myFont.render(back, 1, RED)
        screen.blit(text1, Rect(23, 660, 50, 20))
#description****************************
#move up*****************
        content = "Move up"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(160, 60, 50, 20))  
        screen.blit(ups, Rect(30,20,105,78))
#move down***************
        content = "Move down"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(160, 140, 50, 20)) 
        screen.blit(downs, Rect(30,100,105,78))
#move left***************
        content = "Move left"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(160, 220, 50, 20)) 
        screen.blit(lefts, Rect(30,180,105,78))
#move right**************
        content = "Move right"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(160, 300, 50, 20))
        screen.blit(rights, Rect(30,260,105,78))
#space key
        content = "Fire"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(160, 380, 50, 20))
        screen.blit(space, Rect(30,340,105,78))
#directional fire
        content = "The bullet fires in the direction of movement"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(30, 460, 50, 20))        
#shield
        screen.blit(shield, Rect(500, 100, 50, 20))        
        content = "Defend that ewaste!"
        text1 = myFont.render(content, 1, RED)
        screen.blit(text1, Rect(600, 530, 50, 20))
        
def endgame(screen):
        global gameTimer
        draw.rect(screen,YELLOW,(0,0,width, height))
        screen.blit(endwaste, Rect(380,200,200,100))
        #waste monsters
        screen.blit(monster1, Rect(650,230,200,100))
        screen.blit(monster2, Rect(250,230,200,100))
        screen.blit(monster3, Rect(450,500,200,100))
        results = "You survived for:               seconds"
        text1 = myFont.render(results, 1, BLACK)
        screen.blit(text1, Rect(360, 50, 50, 20))
#file read
        numFile = open("in.dat", "r")
        score = numFile.readline()
        #rstrip removes the newline character read at the end of the line
        score = score.rstrip()
        text1 = myFont.render(score, 1, BLACK)
        screen.blit(text1, Rect(510, 50, 50, 20))
        numFile.close()      
#back button
        draw.rect(screen, WHITE, (20,660,50,20))
        back = "back"
        text1 = myFont.render(back, 1, BLACK)
        screen.blit(text1, Rect(23, 660, 50, 20))        
        
def reset(screen):
        global gameTime,vitality,charx,chary,monsterx, monstery, bulletx, bullety
        gameTime = 0 
        vitality = 100
        charx = 500
        chary = 350
        monsterx = []
        monstery = []
        bulletx = []
        bullety = []
        
# Game Loop*********************************************************************
while running:
        button = 0
        fire = False
     
        for evnt in event.get():             # checks all events that happen
                if evnt.type == QUIT:
                        running = False
                elif evnt.type == MOUSEMOTION:
                        mx, my = evnt.pos     
                elif evnt.type == MOUSEBUTTONDOWN:
                        button = 1
                if evnt.type == KEYDOWN:
                        if evnt.key== K_RIGHT:
                                right = True
                                rightfire = True
                        if evnt.key== K_LEFT:
                                left = True
                                leftfire = True
                        if evnt.key== K_UP:
                                up = True
                                upfire = True
                        if evnt.key== K_DOWN:
                                down = True
                                downfire = True 
                        if evnt.key == K_SPACE:
                                fire = True
                if evnt.type == KEYUP:
                        if evnt.key== K_RIGHT:
                                right = False
                        if evnt.key== K_LEFT:
                                left = False 
                        if evnt.key== K_UP:
                                up = False
                        if evnt.key== K_DOWN:
                                down = False                  
#mouse position detection*******************************************************
        if 220 > mx > 20 and  20 < my < 70 and button == 1:           
                page = 1
#2nd timer setup*********************
                timers = time.get_ticks()
#reset 
                reset(screen)
        elif 440 > mx > 240 and  20 < my < 70 and button == 1:
                page = 2
        elif 980 > mx > 780 and  20 < my < 70 and button == 1:
                page = 3
        elif (page == 1 or page == 2 or page == 4) and 20 < mx < 70 and 660 < my < 680 and button == 1:
                page = 0
#wall of ewaste life setup******************************************************
        if vitality == 0 :
                page = 4    
                vitality = 10
#main program*******************************************************************
        if page == 0:        
                drawHomescreen(screen)    
                changecolor(mx,my)
                        
        elif page  == 1:
                maingame(screen,charx,chary)
                changecolorback(mx,my)
                #character movement******************
                if right == True:
                        charx = charx + 5
                if left == True:
                        charx = charx - 5 
                if up == True:
                        chary = chary - 5
                if down == True:
                        chary = chary + 5   
        elif page == 2:
                howtoplay(screen) 
                changecolorback(mx,my)
        elif page == 3:
                running = False
        elif page == 4:
                endgame(screen)
                changecolorback(mx,my)        
        
        
        display.flip()
        myClock.tick(60)                     # waits long enough to have 60 fps 
quit()                                
