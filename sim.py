import sys
from parse import parse
from drone import Drone

env = parse("busy_day.in")
drones = [Drone(env['warehouses'][0]['pos']) for x in xrange(env['numDrones'])]

print drones
