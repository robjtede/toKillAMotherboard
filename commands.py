def load(drone, store, item_id, item_qt):
	sim['drones'][drone]['products'][item_id] += item_qt
	
def deliver():
    pass

def unload():
    pass

def wait(droneNumber, time):
    sim['drones'][droneNumber]['timer'] = time
