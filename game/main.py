#!/bin/python
from list_of_buildings import buildings 
from list_of_resouces import resources 
from list_of_locations import locations 
from wallet import Wallet 
import pygame, sys, math
from pygame.locals import *
pygame.init()
display = pygame.display.set_mode((640, 480))
#Definitions
def drawtext(string, fs, x, y, r, g, b):
    textfont = pygame.font.SysFont('Open Sans', fs)
    textbox = textfont.render(str(string), False, (r, g, b))
    display.blit(textbox, (x, y))
loc = iter(locations)
def render(state):
    display.fill(state['BGCOLOR']);
    start_x_buildings = 20;
    start_y_buildings = 10;
    start_x_resources = 280;
    start_y_resources = 10;
    font_size=28;
    for i,b in enumerate(game_state["Buildings"]):
        drawtext(b.name+": "+str(round(b.count)),font_size,start_x_buildings,start_y_buildings+i*30,255,255,192)
    for i,b in enumerate(game_state['Resources']):
        drawtext(b.name+": "+str(round(b.amount)),font_size,start_x_resources,start_y_resources+i*30,255,255,192)
    #if relocations >= 1:
    #    drawtext('(F) Farms ' + '(costs: ' + str(farmcost) + ' trees): ' + str(round(farms)), 18, 10, 110, 255, 255, 255)
    pygame.display.update()

    #drawtext(str(research) + ' Research (R) is improving production by x' + str(tickrate) + ' and costs ' + str(researchcost) + ' bananas.', 18, 10, 40, 31, 255, 0)
 

def update(state):
    print(state);
    for resource in state['wallet'].resources:
        for afb in resource.affected_by:
            resource.amount += ((state['Buildings'][afb].count / 60)  * state['tick_rate'])+(resource.bonus*(state['Buildings'][afb].bonus))
    return state;

game_state = {
    "BGCOLOR":(47,47,47),
    "Buildings":buildings,
    "Resources":resources,
    "Location":next(loc),
    "wallet":Wallet(),
    "tick_rate":1,
    "update":update,
    "clock":pygame.time.Clock()
}
while 1:
    game_state['clock'].tick(60)
    keypress = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Key bindings
    if keypress[pygame.K_t]:game_state["Buildings"][0].buy(game_state["wallet"])
    if keypress[pygame.K_f]:game_state["Buildings"][1].buy(game_state["wallet"])
    if keypress[pygame.K_r]:game_state["Buildings"][2].buy(game_state["wallet"])
    if keypress[pygame.K_d]:game_state["Buildings"][3].buy(game_state["wallet"],next(loc,locations[0]))
    game_state=game_state['update'](game_state);
    render(game_state)
