import pygame
import random

 
# Function used to define a text surface created using the text and the font for the text, which then returns the surface and its dimensions
def text_objects(text, font):
    textsurface = font.render(text, True, (255, 255, 255))
    return textsurface, textsurface.get_rect()


# Function for rendering and checking the status of the buttons, where it checks if the mouse is within its borders to change the button's appearance as required
# currently only used for the reset button
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


#reset function to turn all buttons on calendar off after a year has passed so they can reuse the calendar
def reset():
    for i in switches:
        i.on = False


# redraw window function used to draw all the ui elements every frame
def redrawWin():
    screen.fill(bgC)
    for y in switches:
        
        y.draw()
    button("Reset",0,770,50,30,(155,155,155),(55,55,55),reset)
    pygame.display.update()

    

class Button:
    # button class initialisation function where we determine x, y coordinates, the RGB values of the starting colours when activated, the RGB increments by which to change colour
    # a variable called opt that allows for more colours to be added to the array and msg which stores the number of the day in the month to be displayed
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

    # this is the draw function that will draw the button according to if it is activated, if the mouse is hovering on it and also check for clicks on the buttons
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

        
# this functions saves the state of the board of switches into a text file to be loaded at the start of the program
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
            

# initialising pygame window
pygame.init()
smalltext = pygame.font.Font("freesansbold.ttf", 15)
x_width = 1536
y_width = 800
screen = pygame.display.set_mode((x_width,y_width))
run =True
clock = pygame.time.Clock()
bgC = (0,0,0)

#defining the number of days in each month and the cumulative number of days for  normal years and leap years
normal_y = [31,28,31,30,31,30,31,31,30,31,30,31]
cu = [31,59,90,120,151,181,212,243,273,304,334,365]

leap_y = [31,29,31,30,31,30,31,31,30,31,30,31]
cu_L = [31,60,91,121,152,182,213,244,274,305,335,366]


# this checks if a text file exists that has a state of all the switches, if not it will initialise a switch board with all switches deactivated
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
    
           
# initialises the increment (limit var) for the colours, the switch board list and the respective counters to be used for creating the buttons
limit = 15
switches =[]
counter=0
counter1=0


# the following code creates all of the button objects and defines their parameters such as coordinates and so on, currently the way the colours are set is such that every switch has a
# slight offset in colour to the switches arround it, creating a wave like motion of colours
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
            
# the following code changes the states of the switches dependant on the loaded values of the switches from the text file before            
counter = 0
for i in progList:
    for j in i:
        if int(j) == 1:
            switches[counter].on = True
        else:
            switches[counter].on = False
        counter+=1
        
# this is the main loop that will execute while the program is running
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write()
            run = False
            quit()

    # this loop ensures that the colours change over time every frame for switches that are activated while ensure the increment does not cause the rgb values to be greater than 255
    # and cycles through a various combination of colours
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



