#!/bin/python
from list_of_buildings import buildings 
from list_of_resources import resources 
from list_of_locations import locations 
loc = iter(locations)
from wallet import Wallet 
import pygame, sys, math
from pygame.locals import *
pygame.init()
display = pygame.display.set_mode((840, 580))
#Definitions
def drawtext(string, fs, x, y, r, g, b):
    textfont = pygame.font.SysFont('Open Sans', fs)
    textbox = textfont.render(str(string), False, (r, g, b))
    display.blit(textbox, (x, y))
def render(state):
    display.fill(state['BGCOLOR']);
    start_x_buildings = 20;
    start_y_buildings = 90;
    start_x_resources = 600;
    start_y_resources = 10;
    font_size=28;
    keys = ["T","F","R","D","K"]
    for i,b in enumerate(game_state["Buildings"]):
        costs_string = ""
        visible=True;
        for cost in b.costs:
            if not game_state['wallet'].has(cost.name):
                visible=False;
            costs_string+="("+cost.name+": "+str(round(cost.amount))+") "
        if visible:drawtext(f"{keys[i]}:) {b.name}: {str(round(b.count))} {costs_string}",font_size,start_x_buildings,start_y_buildings+i*30,255,255,192)
    for i,b in enumerate(game_state['wallet'].resources):
        drawtext(b.name+": "+str(round(b.amount)),font_size,start_x_resources,start_y_resources+i*30,255,255,192)
    #if relocations >= 1:
    #    drawtext('(F) Farms ' + '(costs: ' + str(farmcost) + ' trees): ' + str(round(farms)), 18, 10, 110, 255, 255, 255)
    pygame.display.update()

    #drawtext(str(research) + ' Research (R) is improving production by x' + str(tickrate) + ' and costs ' + str(researchcost) + ' bananas.', 18, 10, 40, 31, 255, 0)
 

def update(state):
    for building in state['Buildings']:
        for afb in building.affects:
            for resource in state['wallet'].resources:
                if afb.name==resource.name and building.count>0:
                    bonus = ((resource.bonus&building.bonus)*(resource.bonus&building.bonus))
                    resource.amount += ((afb.amount*building.count / 60)  * state['tick_rate']) + bonus
    return state;

game_state = {
    "BGCOLOR":(47,47,47),
    "Buildings":buildings,
    "Location":next(loc),
    "wallet":Wallet(),
    "tick_rate":1,
    "update":update,
    "clock":pygame.time.Clock(),
    "research_count":0,
}
game_state['wallet'].resources.append(resources[0])#we only need the first one - the rest will get added via teh game
#more can be appended here with there default value changed for testing
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
    if keypress[pygame.K_r]:game_state["Buildings"][2].buy(game_state["wallet"],game_state)
    if keypress[pygame.K_d]:game_state["Buildings"][3].buy(game_state["wallet"],[game_state,next(loc,locations[0])])
    if keypress[pygame.K_k]:game_state["Buildings"][4].buy(game_state["wallet"])

    game_state=game_state['update'](game_state);
    render(game_state)
