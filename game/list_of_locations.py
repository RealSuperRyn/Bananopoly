#!/usr/bin/env python
from location import Location

def effect_add(game_state,res):
    if(not res): return False;
    game_state["wallet"].add("banana",1);
    return True;


locations=[
    Location("simple farm", effect_add)
]
