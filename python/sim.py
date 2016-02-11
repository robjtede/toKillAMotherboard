import sys
from parse import parse
from drone import Drone

env = parse("busy_day.in")
drones = [Drone(env['warehouses'][0]['pos']) for x in xrange(env['numDrones'])]

for t in xrange(0, 1000):
    for drone in dones
        drone.timer -= 1
        if drone.timer == 0:
            drone.doAction();
print drones
