#!/usr/bin/env python
from resource import Resource
class Wallet:
    def __init__(self):
        self.resources=[];
        self.discount_bonus=0;
    def reset(self):
        for cur in self.resources:
            cur.reset();
    def set_discount(self,val):
        self.discount_bonus=val;
    def Buy(self,building):
        return building.buy(self);
    def add(self, resourceName,amount):
        result = False;
        resource = Resource(resourceName,amount);
        for r in self.resources:
            if r.name !=resource.name : continue;
            r.amount=r.amount+resource.amount;
            result=True;
        if not result:
            self.resources.append(resource)
        