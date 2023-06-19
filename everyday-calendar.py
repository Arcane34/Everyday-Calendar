import pygame
import random

 
        
def text_objects(text, font):
    textsurface = font.render(text, True, (255, 255, 255))
    return textsurface, textsurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ic, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ac, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 10)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = (round(x + (w / 2)), round(y + (h / 2)))
    screen.blit(textsurf, textrect)


def reset():
    for i in switches:
        i.on = False



def redrawWin():
    screen.fill(bgC)
    for y in switches:
        
        y.draw()
    button("Reset",0,770,50,30,(155,155,155),(55,55,55),reset)
    pygame.display.update()

    
class Button:
    
    def __init__(self, x, y, red,green,blue , rD, gD, bD, opt,msg):
        self.x = x
        self.y = y
        self.on = False
        self.r = round(y_width/75)
        self.hlightC = (255,124,12)
        self.offC = (150,150,150)
        self.onC = (red,green,blue)
        self.rD = rD
        self.gD= gD
        self.bD= bD
        self.opt = opt
        self.msg = msg
        self.textsurf,self.textrect = text_objects(self.msg, smalltext)
    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.on == True:
            pygame.draw.circle(screen, self.onC, (self.x,self.y), self.r)
            if click[0] == 1 and self.x +(self.r) > mouse[0] > self.x - self.r and self.y + (self.r ) > mouse[1] > self.y - self.r:
                self.on = False
                pygame.time.wait(200)
        elif self.x +(self.r) > mouse[0] > self.x - self.r and self.y + (self.r ) > mouse[1] > self.y - self.r:
            pygame.draw.circle(screen, self.hlightC, (self.x,self.y), self.r)
            if click[0] == 1:
                self.on = True
                pygame.time.wait(200)
        else:
            pygame.draw.circle(screen, self.offC, (self.x,self.y), self.r)
        self.textrect.center = (round(self.x + (self.r / 2)+15), round(self.y + (self.r / 2))-5)
        screen.blit(self.textsurf, self.textrect)

        

def write():
    counter = 0
    for i in progList:
        for j in i:
            if switches[counter].on == True:
                i[i.index(j)]= 1
            else:
                i[i.index(j)]= 0
            counter+=1
    with open("progress.txt","w") as file:
        for i in progList:
            line = ""
            for j in range(len(i)):
                if j == len(i)-1:
                    line += str(i[j])
                else:
                    line+= str(i[j]) + ","
            file.write(line)
            file.write("\n")
            

pygame.init()
smalltext = pygame.font.Font("freesansbold.ttf", 15)
x_width = 1536
y_width = 800
screen = pygame.display.set_mode((x_width,y_width))
run =True
clock = pygame.time.Clock()
bgC = (0,0,0)

normal_y = [31,28,31,30,31,30,31,31,30,31,30,31]
cu = [31,59,90,120,151,181,212,243,273,304,334,365]

leap_y = [31,29,31,30,31,30,31,31,30,31,30,31]
cu_L = [31,60,91,121,152,182,213,244,274,305,335,366]


try:
    progList = []
    with open("progress.txt","r") as file:
        contents= True
        while contents != "":
            contents=file.readline()
            contents=contents.strip()
            splitContents=contents.split(",")
            if len(splitContents)==1:
                break
            progList.append(splitContents)
except:
    progList = []
    for i in leap_y:
        month = []
        for j in range(i):
            month.append(0)
        progList.append(month)
    
           

limit = 15
switches =[]
counter=0
counter1=0

for i in range(len(leap_y)):
    for j in range(leap_y[i]):
        day = str(j+1)
        if counter < 25:
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , counter1*10,0,0, limit,0,0  ,0, day))

        elif counter < 50:
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255,5+counter1*10,0,0,limit,0  ,0, day))

        elif counter < 75 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255,255,counter1*10,0,0,limit  ,0,day))

        elif counter < 100 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 250-counter1*10,255,255, -limit,0,0  ,0,day))

        elif counter < 125 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 0,255-counter1*10,255, 0,-limit,0  ,0,day))

        elif counter < 150 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 5+counter1*10,0,255, limit,0,0  ,1,day))

        elif counter < 175 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255-counter1*10,counter1*10,255-counter1*10, -limit,limit,-limit  ,1,day))

        elif counter < 200 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 0,250-counter1*10,0, 0,-limit,0  ,1,day))

        elif counter < 225:
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , counter1*10,0,0, limit,0,0  ,0,day))

        elif counter < 250 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255,5+counter1*10,0,0,limit,0  ,0,day))

        elif counter < 275 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255,255,counter1*10,0,0,limit  ,0,day))

        elif counter < 300 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 250-counter1*10,255,255, -limit,0,0  ,0,day))

        elif counter < 325 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 0,255-counter1*10,255, 0,-limit,0  ,0,day))

        elif counter < 350 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 5+counter1*10,0,255, limit,0,0  ,1,day))

        elif counter < 375 :
            switches.append(Button(round(30+(x_width / 12)*i), 15+round((y_width/45)+6)*j , 255-counter1*10,counter1*10,255-counter1*10, -limit,limit,-limit  ,1,day))
        counter+=1
        counter1+=1
        if counter1 == 25:
            counter1 = 0
            
counter = 0
for i in progList:
    for j in i:
        if int(j) == 1:
            switches[counter].on = True
        else:
            switches[counter].on = False
        counter+=1
        

while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write()
            run = False
            quit()

    for switch in switches:
        red = switch.onC[0]+switch.rD
        green = switch.onC[1]+switch.gD
        blue = switch.onC[2]+switch.bD
        if red >255 and switch.rD == limit and switch.opt == 0:   # 100
            red = 255
            switch.rD = 0
            switch.gD = limit
            
        elif green > 255 and switch.gD == limit and switch.opt == 0: #110
            green = 255
            switch.gD = 0
            switch.bD = limit
            
        elif blue > 255 and switch.bD == limit and switch.opt == 0: #111
            blue = 255
            switch.bD = 0
            switch.rD = -limit
            
        elif red<0 and switch.rD == -limit and switch.opt == 0:#011
            red = 0
            switch.rD = 0
            switch.gD = -limit
            
        elif green < 0 and switch.gD == -limit and switch.opt == 0:#001
            green = 0
            switch.gD = 0
            switch.rD = limit
            switch.opt = 1
            
        elif red > 255 and switch.rD == limit and switch.opt == 1:#101
            red = 255
            switch.rD = -limit
            switch.gD = limit
            switch.bD = -limit
            
        elif red<0 and switch.rD == -limit and switch.gD == limit and switch.bD == -limit  and switch.opt == 1:#010
            red = 0
            green = 255
            blue = 0
            switch.rD = 0
            switch.gD = -limit
            switch.bD = 0
            
        elif green <0 and switch.gD == -limit and switch.opt == 1:#000
            green = 0
            switch.rD = limit
            switch.gD = 0
            switch.opt = 0

        switch.onC = (red, green, blue)
        """
        if switch.on == True:
            if random.randint(0, 10) <2:
                switch.rD += random.randint(-limit,limit)
                switch.gD += random.randint(-limit,limit)
                switch.bD += random.randint(-limit,limit)
            if switch.rD > 15:
                switch.rD=15
            elif switch.rD < -15:
                switch.rD = -15
            if switch.gD > 15:
                switch.gD=15
            elif switch.gD < -15:
                switch.gD = -15
            if switch.bD > 15:
                switch.bD=15
            elif switch.bD < -15:
                switch.bD = -15

            
            red = switch.onC[0]+switch.rD
            green = switch.onC[1]+switch.gD
            blue = switch.onC[2]+switch.bD
            h = 240
            l = 30
            if red > h:
                red = h
            elif red < l:
                red = l
            if green > h:
                green = h
            elif green < l:
                green = l
            if blue > h:
                blue = h
            elif blue < l:
                blue = l
            """
         
                    
    redrawWin()



