#!/usr/bin/env python
class Building:
    def __init__(self,name,costs,inc_val,inc_inc_val,b):
        self._or_sv=costs;
        self._or_iv=inc_val;
        self._or_ivu=inc_inc_val;

        self.name=name;
        self.costs=costs;
        self.inc=inc_val;
        self._inc_update=inc_inc_val;
        self.count=0;
        self.bonus=b;
        print(costs[0].amount)
    def buy(self,wallet):
        tests=[]
        for i,cost in enumerate(self.costs):
            for resource in wallet.resources:
                if(resource.name!=cost.name):continue;
                print(resource.name," ",resource.amount," - ",cost.name," ",cost.amount)
                if(resource.amount-cost.amount>=0): tests.append(True)
                else: tests.append(False)    
        if not all(x for x in tests): return False;
        print(tests,"should all be true")
        return self._handle_buy(wallet)
    def _handle_buy(self,wallet):
        for i,cost in enumerate(self.costs):
            for resource in wallet.resources:
                if(resource.name!=cost.name):continue;
                resource.amount=resource.amount-cost.amount;
                print(resource.name," ",resource.amount," - ",cost.name," ",cost.amount,"adjusting to")
                cost.amount=self.inc+cost.amount;
                print(cost.name," ",cost.amount,"adjusted to")

        self.count=self.count+1; 
        self.inc=self._inc_update+self.inc;
        print(self.count,self.inc,"updated count and inc")
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
        super().__init__(bld.name,bld.costs,bld.inc,bld._inc_update,bld.bonus)
        self.fn=fn;
    def buy(self, wallet,state):
        res = super().buy(wallet);
        if(res):
            self.fn([wallet,state]);
    def fn(self,args):
        self.fn(args)
