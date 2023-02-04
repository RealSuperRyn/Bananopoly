#!/usr/bin/env python
from resource import Resource;
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
        building.set_inc_plus(-rc/1000)
    game_state["wallet"].reset();
    rc=rc+1;
    game_state['wallet'].research(rc)
    for resource in game_state['wallet'].resources:
        resource.reset();
    game_state['tick_rate']*=1.25
    game_state['Location']=args[1][1];
    print("relocated",args[1][1].name)
    return True;
buildings = [
    Building("tree", [Resource("banana",1)],1,1,0),
    Building("farm", [Resource("banana",75)],75,75,1),
    Function_Building(Building("laboratory",[Resource("banana",175),Resource("research",1)],1,0,1), research_add),
    Function_Building(Building("relocation matrix",[Resource("research",275)],1,0,2), relocate)
]