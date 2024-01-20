import pygame
import random
import datetime
import calendar

def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b


def bezier(a, d, t):
    # a c d b
    b = lerp(a,d, 0.1)
    c = lerp(a,d, 1.1)
    pointA = lerp(a,b,t)
    pointB = lerp(b,c,t)
    pointC = lerp(c,d,t)
    pointAB = lerp(pointA, pointB, t)
    pointBC = lerp(pointB, pointC, t)

    return lerp(pointAB, pointBC, t)

# Function used to define a text surface created using the text and the font for the text, which then returns the surface and its dimensions
def text_objects(text, font, textColour):
    textsurface = font.render(text, True, textColour)
    return textsurface, textsurface.get_rect()

class Button:
    def __init__(self, x, y, size, roundedNess, colour ,msg, action = None, feed = None):
        self.pos = [x,y]
        self.size = size
        self.roundedNess = roundedNess

        self.colour = colour
        self.offColour = (max(colour[0] - 50, 0), max(colour[1] - 50, 0), max(colour[2] - 50, 0)) 
        self.onColour = (min(colour[0] + 50, 255), min(colour[1] + 50, 255), min(colour[2] + 50, 255)) 
        self.clickColour = (min(colour[0] + 70, 255), min(colour[1] + 70, 255), min(colour[2] + 70, 255)) 
        self.textColour = (255,255,255)
        
        self.disabled = False
        self.on = False
        self.msg = msg
        self.textsurf,self.textrect = text_objects(self.msg, smalltext, self.textColour)
        self.action = action
        self.feed = feed

    def draw(self, window):
        
        mouse = pygame.mouse.get_pos()
        mouse = [mouse[0] - screenOffset[0], mouse[1] - screenOffset[1]] 
        if self.feed != None:
            if type(self.feed) is tuple:
                self.pos[0] += dateOffset[0]
                self.pos[1] += dateOffset[1]
        click = pygame.mouse.get_pressed()
        if pygame.Rect.colliderect(pygame.Rect(0,0,window.get_size()[0], window.get_size()[1]), pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])):  
            self.textsurf,self.textrect = text_objects(self.msg, smalltext, self.textColour)

            
            if not self.disabled:
                if self.pos[0] +(self.size[0]) > mouse[0] > self.pos[0] and self.pos[1] + self.size[1] > mouse[1] > self.pos[1]:
                    if click[0] == 1:
                        pygame.draw.rect(window, self.clickColour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), 0, self.roundedNess)
                        self.on = True
                    else:
                        pygame.draw.rect(window, self.onColour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), 0, self.roundedNess)
                    if self.on and click[0] == 0:
                        self.on = False
                        if self.feed == None:
                            self.action()
                        else:
                            self.action(self.feed)

                else:
                    pygame.draw.rect(window, self.colour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), 0, self.roundedNess)
            else:
                pygame.draw.rect(window, self.offColour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), 0, self.roundedNess)
            
            
            self.textrect.center = (round(self.pos[0] + self.size[0]/2), round(self.pos[1] + self.size[1]/2))
            window.blit(self.textsurf, self.textrect)

        if self.feed != None:
            if type(self.feed) is tuple:
                self.pos[0] -= dateOffset[0]
                self.pos[1] -= dateOffset[1]




class Label:
    def __init__(self, x, y, size, roundedNess, colour ,msg):
        self.pos = [x,y]
        self.size = size
        self.roundedNess = roundedNess

        self.colour = colour
        self.textColour = (255,255,255)
        self.textFont = smalltext
        self.msg = msg
        if size[2] != 0:
            self.textFont = pygame.font.Font("freesansbold.ttf", self.size[2])
            self.textsurf,self.textrect = text_objects(self.msg, self.textFont, self.textColour)
            
            


    def draw(self, window):
        if pygame.Rect.colliderect(pygame.Rect(0,0,window.get_size()[0], window.get_size()[1]), pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])):  
            if self.size[2] != 0:
                self.textsurf,self.textrect = text_objects(self.msg, self.textFont, self.textColour)
            else:
                self.textsurf,self.textrect = text_objects(self.msg, smalltext, self.textColour)
            pygame.draw.rect(window, self.colour, (self.pos[0], self.pos[1], self.size[0], self.size[1]), 0, 0, self.roundedNess[0], self.roundedNess[1], self.roundedNess[2], self.roundedNess[3])
            self.textrect.center = (round(self.pos[0] + self.size[0]/2), round(self.pos[1] + self.size[1]/2))
            screen.blit(self.textsurf, self.textrect)










def redrawWin():
    screen.fill((179,255,0))
    win.fill(bgC)

    
    

    

    for cb in calendarButtons:
        if cb.feed[0] != browseMonth[0]:
            cb.disabled = True
        else:
            cb.disabled = False
        cb.draw(screen)
    
    for b in buttons:
        b.draw(screen)

    for l in labels:
        l.draw(screen)

    
    win.blit(screen, (screenOffset[0],screenOffset[1]))
    pygame.display.update()






























# initialising pygame window
pygame.init()
smalltext = pygame.font.Font("freesansbold.ttf", 15)
bigtext = pygame.font.Font("freesansbold.ttf", 30)
x_width = 1536
y_width = 800


screen = pygame.Surface((x_width,y_width)) #calendar screen


win = pygame.display.set_mode((x_width,y_width)) # main screen


screenOffset = [0,0] #offset of window 
screenOffsetAim = [0,0]
run =True
clock = pygame.time.Clock()
time = 0
bgC = (0,0,0)

year = []
cu = []

date = datetime.date.today()
print(date)

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if calendar.isleap(date.year):   #LEAP YEAR
    year = [31,29,31,30,31,30,31,31,30,31,30,31] # each month and the number of days it has 
    cu = [31,60,91,121,152,182,213,244,274,305,335,366] # number of cumulative days in the year
else:  #NOT LEAP YEAR
    year = [31,28,31,30,31,30,31,31,30,31,30,31] # each month and the number of days it has 
    cu = [31,59,90,120,151,181,212,243,273,304,334,365] # number of cumulative days in the year













buttons = []
calendarButtons = []

def calButton(x):
    print(x)


monthOffsets = []

widthOff = (x_width*0.6) // len(WEEKDAYS)
heightOff = (y_width - 30) // 6

jan1 = datetime.date(date.year, 1, 1)
hOffset = WEEKDAYS.index(jan1.strftime("%A")) * widthOff
print(hOffset)


for mon in range(len(year)):
    monthOffsets.append(0 - heightOff * (hOffset // (widthOff * 7)) )
    for day in range(year[mon]):
        nButton = (Button( hOffset % (widthOff*7), heightOff * (hOffset // (widthOff * 7)) + 30,  (widthOff, heightOff) , 0, (200,200,200) , str(day + 1), calButton, (mon + 1,day + 1)))
        nButton.onColour = (255,255,0)
        nButton.textColour = (0,0,0)
        calendarButtons.append(nButton)
        
        hOffset += widthOff

    


def playButton():
    screenOffsetAim[0] = x_width

#buttons.append(Button(200,200,(100,50), 3 , (100,100,100), "Play", playButton))




browseMonth = [1]

labels = []
monthLabel = Label( x_width*0.6 , 0, ( x_width*0.4 , 60, 30), [0,0,10,10], (30,30,255), MONTHS[browseMonth[0] - 1])
labels.append(monthLabel)



for day in range(len(WEEKDAYS)):
    label = Label(widthOff*day,0, (widthOff,30, 0), [5,5,0,0], (30,30,255), WEEKDAYS[day])
    labels.append(label)


def moveMonth():
    browseMonth[0] += 1
    dateOffsetAim[1] = monthOffsets[browseMonth[0] - 1]

buttons.append(Button(930,750, (100,50), 0, (200,100,0), "Move Down", moveMonth))

datesMove = False
datesPos = [0,0]
dateOffset = [0,0]
dateOffsetAim = [0,0]



move = False
screenPos = [0,0]
while run:
    print(calendarButtons[70].pos)

    monthLabel.msg = MONTHS[browseMonth[0] - 1]

    time += 0.01
    if screenOffsetAim != screenOffset and (not move):
        for i in buttons:
            i.disabled = True
        move = True
        screenPos = [screenOffset[0], screenOffset[1]]
        time = 0
    elif screenOffsetAim == screenOffset:
        move = False
        for i in buttons:
            i.disabled = False
    if move:
        screenOffset[0] = bezier(screenPos[0], screenOffsetAim[0], min(time, 1))
        screenOffset[1] = bezier(screenPos[1], screenOffsetAim[1], min(time, 1))

    

    if dateOffsetAim != dateOffset and (not datesMove):
        for i in buttons:
            i.disabled = True
        datesMove = True
        datesPos = [dateOffset[0], dateOffset[1]]
        time = 0
    elif dateOffsetAim == dateOffset:
        datesMove = False
        for i in buttons:
            i.disabled = False
    if datesMove:
        dateOffset[0] = bezier(datesPos[0], dateOffsetAim[0], min(time, 1))
        dateOffset[1] = bezier(datesPos[1], dateOffsetAim[1], min(time, 1))


    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
    redrawWin()