class Drone:
    def __init__(self, pos):
        self.pos = pos
        self.timer = 0
        self.action = lambda: None
        self.items = []
    
    def load(self, store, item_id, item_qt):
        self.items['item_id'] += item_qt
        sim['warehouses'][store]['products'][item_id] -= item_qt

    def deliver(self, store):
        self.pos = sim['orders'][store]['pos']

    def unload(self, store, item_id, item_qt):
        self.items['item_id'] -= item_qt

    def wait(self, time):
        self.timer = time

