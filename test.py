import sys
from parse import parse

sim = parse(sys.argv[1])
print sim['numWarehouses']

# rowsInArea
# columnsInArea
# numDrones
# numWarehouses
# numOrders
# deadline
# productWeights
# numProductTypes
# maxLoad
# warehouses
#     pos
#         row
#         col
# orders
#     pos
#         row
#         col
#     num
#     products
