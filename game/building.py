#!/usr/bin/env python
class Building:
    def __init__(self,name,costs,inc_val,inc_inc_val):
        self._or_sv=costs;
        self._or_iv=inc_val;
        self._or_ivu=inc_inc_val;

        self.name=name;
        self.costs=costs;
        self.inc=inc_val;
        self._inc_update=inc_inc_val;
        self.count=0;
        self.bonus=0;
    
    def buy(self,wallet):
        tests=[]
        for i,cost in enumerate(self.costs):
            for resource in wallet.resources:
                if(resource.name!=cost.name):continue;
                if(resource[cost.name].amount-cost.amount>0): tests.append(True)
                else: tests.append(False)    
        if not all(x for x in tests): return False;
        return self._handle_buy(wallet)
    def _handle_buy(self,wallet):
        for i,cost in enumerate(self.costs):
            for resource in wallet.resources:
                if(resource.name!=cost.name):continue;
                wallet[cost.name].amount=wallet[cost.name].amount-cost.amount;
                cost.amount=self.inc_val+cost.amount;
        self.count=self.count+1; 
        self.inc=self._inc_update+self.inc;
        return True;     

    def set_inc_plus(self,v):
        self.inc_update=self._inc_update+v;
    def reset(self):
        self.count=0;
        self.cost=self._or_sv;
        self.inc=self._or_iv;
        self._inc_update=self._or_ivu;



class Function_Building(Building):
    def __init__(self,bld,fn):
        super().__init__(bld.name,bld.costs,bld.inc,bld._inc_update)
        self.fn=fn;
    def buy(self, wallet,res):
        res = super().buy(wallet);
        self.fn(wallet,res);
    def fn(self,args):
        self.fn(args)
