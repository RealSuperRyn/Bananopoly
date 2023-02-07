#!/usr/bin/env python
from resource import Affect,Cost;
from building import *

def research_add(args):
    if(not args[0]):return False;
    args[1]['research_count']= args[1]['research_count']+1

def relocate(args):
    if(not args[0]): return False
    game_state = args[1][0];
    rc = game_state['research_count'];
    for building in game_state['Buildings']:
        if(building.name=="relocation matrix"):continue;
        building.reset();
        building.bonus=building.bonus+1;
    game_state["wallet"].reset();
    rc=rc+1;
    game_state['wallet'].research(rc)

    game_state['tick_rate']*=1.25
    game_state['Location']=args[1][1];
    print("relocated",args[1][1].name)
    return True;
buildings = [
    Building(
        "tree",#name
        [Cost("banana",1,0.184)],#price of building 
        [Affect("banana",1,0)],# what the building affects number is multiplier per building
        0 #bonus
        ),
    Building(
        "farm", 
        [Cost("banana",75,0.223)],
        [Affect("banasteel",1,0)],
        0),
    Function_Building(
        Building(
            "laboratory",
            [Cost("banana",10,0.9), Cost("banasteel",100,1.1)],
            [Affect("research",1,0)],
            0,#bonus
            ), 
        research_add), #fn on click
    Function_Building(
        Building(
            "relocation matrix",
            [Cost("research",1000,1.2),Cost('banasteel',2000,1.3),Cost("banana",1235,1.2345)],
            [Affect("banacities",1,0)],
            1
            ), 
        relocate),
    Building(
        "bananaricks",
        [Cost("banana",1,1.2),Cost('banasteel',192,1.3),Cost("banacities",100,1.2345)],
        [Affect("bananhumans",1,0)],
        1
            ), 
]