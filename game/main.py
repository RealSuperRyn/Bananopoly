#!/bin/python
import pygame, sys, math
from pygame.locals import *
pygame.init()
display = pygame.display.set_mode((640, 480))
print("Hello, world!")
#Definitions
def drawtext(string, fs, x, y, r, g, b):
    textfont = pygame.font.SysFont('Open Sans', fs)
    textbox = textfont.render(str(string), False, (r, g, b))
    display.blit(textbox, (x, y))
#Initialize variables
BGCOLOR = (47, 47, 47)
bananas = 1
trees = 0
treecost = 1
tickrate = 1
research = 0
researchcost = 100
relocations = 0
relocationcost = 2
farms = 0
farmcost = 0
#End of variables
clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    keypress = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Keys
    if keypress[pygame.K_t]:
        if bananas >= treecost:
            bananas -= treecost
            treecost += round(math.sqrt(treecost))
            trees += 1
    if keypress[pygame.K_r]:
        if bananas >= researchcost:
            bananas -= researchcost
            researchcost *= 10
            tickrate *= 1.25
            research += 1
    if keypress[pygame.K_d]:
        if research >= relocationcost:
            relocations += 1
            relocationcost *= 2
            bananas = 1
            trees = 0
            treecost = 1
            tickrate = 1
            research = 0
            researchcost = 100
            farms = 0
            farmcost = 75
    if keypress[pygame.K_f]:
        if trees >= farmcost:
            trees = 0
            treecost = 1
            farms += 1
            farmcost += round(math.sqrt(farmcost) * 4)
    #count
    bananas += ((trees / 60) * tickrate)
    trees += ((farms / 60 ) * (tickrate))
    #render
    display.fill(BGCOLOR)
    drawtext('Bananas: ' + str(round(bananas)), 30, 10, 10, 255, 255, 192)
    drawtext('(T) Trees ' + '(costs: ' + str(treecost) + ' bananas): ' + str(round(trees)), 18, 10, 70, 255, 255, 255)
    drawtext(str(research) + ' Research (R) is improving production by x' + str(tickrate) + ' and costs ' + str(researchcost) + ' bananas.', 18, 10, 40, 31, 255, 0)
    drawtext('(D) Relocation: Requires ' + str(relocationcost) + ' Research', 15, 10, 450, 255, 255, 255)
    if relocations >= 1:
        drawtext('(F) Farms ' + '(costs: ' + str(farmcost) + ' trees): ' + str(round(farms)), 18, 10, 110, 255, 255, 255)
    pygame.display.update()
    
