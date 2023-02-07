#!/usr/bin/env python
class Building:
    def __init__(self,name,costs,affects,b):
        self._or_sv=costs;

        self.name=name;
        self.costs=costs;
        print(costs[0].amount,"is amount",costs[0].name,"for that thing")
        self.affects=affects;
        self.count=0;
        self.bonus=b;
        print(costs[0].amount)
    def buy(self,wallet):
        tests=[]
        print("buy",self.costs[0].amount)
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
        for cost in self.costs:
            for resource in wallet.resources:
                if(resource.name!=cost.name):continue;
                resource.amount=resource.amount-cost.amount;
                print(resource.name," ",resource.amount," - ",cost.name," ",cost.amount,"adjusting to")
                cost.increase();
                print(cost.name," ",cost.amount,"adjusted to")

        self.count=self.count+1; 

        for afb in self.affects:
            if wallet.has(afb.name): continue;
            wallet.add(afb.name,0);

        return True;     

    def reset(self):
        self.count=0;
        for cost in self.costs:
            cost.reset();


class Function_Building(Building):
    def __init__(self,bld,fn):
        super().__init__(bld.name,bld.costs,bld.affects,bld.bonus)
        self.fn=fn;
    def buy(self, wallet,state):
        res = super().buy(wallet);
        if(res):
            self.fn([wallet,state]);
    def fn(self,args):
        self.fn(args)
