class Drone:
    def __init__(self, pos):
        self.pos = pos
        self.timer = 0
        self.action = lambda: pass
        self.items = []
    
    def load(store, item_id, item_qt):
        self.items['item_id'] += item_qt
        sim['warehouses'][store]['products'][item_id] -= item_qt

    def deliver(store):
        self.pos = sim['orders'][store]['pos']

    def unload(store, item_id, item_qt):
        self.items['item_id'] -= item_qt

    def wait(time):
        self.timer = time
    
