#!/usr/bin/env python
from resource import Resource;
from building import *

def research_add(args):
    if(not args[0]):return False;
    game_state['research_count']= game_state['research_count']+1
def relocate(args):
    if(not args[0]): return False
    rc = game_state['research_count'];
    for building in game_state['Buildings']:
        building.reset();
        building.set_inc_plus(-re/1000)
    game_state["wallet"].reset();
    rc=rc+1;
    game_state['wallet'].research(rc)
    for resource in game_state["Resources"]:
        resource.reset();
    game_state['tick_rate']*=1.25
    game_state['Location']=next_location;
    return True;
buildings = [
    Building("tree", [Resource("banana",1)],1,0),
    Building("farm", [Resource("banana",75)],1,0),
    Function_Building(Building("research",[Resource("banana",175)],1,0), research_add),
    Function_Building(Building("move location",[Resource("banana",275)],1,0), relocate)
]