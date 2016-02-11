class Drone:
    def __init__(self, pos, simulatedEnvironment):
        self.sim = simulatedEnvironment
        self.pos = pos
        self.timer = 0
        self.action = 'none'
        self.items = [0 for x in xrange(self.sim["numProductTypes"])]
        self.weight = 0

    def doAction():
        if(self.action == "load"):
            load()
        elif(self.action == "deliver"):
            deliver()
        #elif(self.action == "unload")
    
    # Function attempts to remove the items from here into this drone. Does not if too heavy or not enough there
    def load(item_id, item_qt):
        for w in self.sim['warehouses']:
            if w['pos']['row'] == self.pos['row'] && w['pos']['col'] == self.pos['col'] && w['products'][item_id] >= item_qt && self.sim['productWeights'][item_id] * item_qt + self.weight <= self.sim['maxLoad']:
                w['products'][item_id] -= item_qt
                self.items[item_id] += item_qt
                self.weight += self.sim['productWeights'][item_id] * item_qt

    def deliver():
        pass

    #def unload(store, item_id, item_qt):
    #    sim['drones'][drone]['products'][item_id] -= item_qt

    #def wait(time):
    #    sim['drones'][droneNumber]['timer'] = time
    
