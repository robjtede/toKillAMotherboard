def load(drone, store, item_id, item_qt):
    sim['drones'][drone]['products'][item_id] += item_qt
    sim['warehouses'][store]['products'][item_id] -= item_qt
    
    
def deliver(drone, store):
    sim['drones'][drone]['pos']['row'] = sim['warehouses'][store]['pos']['row']
    sim['drones'][drone]['pos']['col'] = sim['warehouses'][store]['pos']['col']

def unload(drone, store, item_id, item_qt):
    sim['drones'][drone]['products'][item_id] -= item_qt

def wait(droneNumber, time):
    sim['drones'][droneNumber]['timer'] = time
