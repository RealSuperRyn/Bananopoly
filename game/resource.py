#!/usr/bin/env python
class Resource:
    def __init__(self,name,amount):
        self.name=name;
        self.amount=amount;
        self.bonus=0;
    def reset(self):
        self.amount=0;
    def update(self,value):
        self.amount=value;

class Cost(Resource):
    def __init__(self,name,amount,multi):
        self.o_amount=amount;
        self.name=name;
        self.amount=amount;
        self.multi=multi;
        self.bonus=0;
    def reset(self):
        self.amount=self.o_amount;
    def increase(self):
        self.amount+=(self.amount*self.multi)
        print("increased amount",self.amount)
class Affect(Resource):
    def __init__(self,name,amount,bonus):
        self.o_amount=amount;
        self.name=name;
        self.amount=amount;
        self.bonus=0;
    def reset(self):
        self.amount=self.o_amount;