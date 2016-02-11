def load(drone, store, item_id, item_qt):
    sim['drones'][drone]['products'][item_id] += item_qt
    sim['drones'][drone]['commands'] = 'load'
    sim['drones'][drone]['time'] = 1
    
def deliver():
    pass

def unload():
    pass

def wait(droneNumber, time):
    sim['drones'][droneNumber]['timer'] = time
