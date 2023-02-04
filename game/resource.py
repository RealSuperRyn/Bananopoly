#!/usr/bin/env python
class Resource:
    def __init__(self,name,amount,afb=None):
        self.name=name;
        self.amount=amount;
        self.bonus=0;
        self.affected_by=afb;
    def reset(self):
        self.amount=0;
    def update(self,value):
        this.value=value;