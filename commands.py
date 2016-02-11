def load(drone, item_id, item_qt):
	
	store_pos = sim['warehouses'][x]['pos'] for x in xrange(sim['numWarehouses'])
	
	
	
	# move to nearest warehouse
	    # remove free contents from warehouse
	    # add reserve contents to warehouse
	    # wait [distance]
	    # set drone pos to warehouse pos
	    
	# collect items
	    # wait 1
	    # add available contents to drone
	    # remove reserve contents from warehouse

# must run second
def deliver(drone, order):
    # reserve items
        # add expected contents to order
        # wait [distance]
        # set drone pos to order pos
        
    # deliver items
        # wait 1
        # remove available contents from drone
        # remove expected contents from order
        # add available contents to order

# must run first
def unload(drone, store, item_id, item_qt):
    # move to warehouse
        # add expected contents to warehouse
        # wait [distance]
        # set drone pos to order pos
    # unload items
        # wait 1
        # remove available contents from drone
        # remove expected contents from warehouse
        # add available contents to warehouse
    
def wait(droneNumber, time):
    # wait [time]