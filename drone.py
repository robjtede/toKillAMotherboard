class Drone:    
    def __init__(self, pos):
        self.pos = pos
        self.timer = 0
        self.action = 'none'
        self.items = []
    
    def load(store, item_id, item_qt):
        sim['drones'][drone]['products'][item_id] += item_qt

    def deliver():
        pass

    def unload(store, item_id, item_qt):
        sim['drones'][drone]['products'][item_id] -= item_qt

    def wait(time):
        sim['drones'][droneNumber]['timer'] = time
    
