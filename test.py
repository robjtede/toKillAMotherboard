import sys
from parse import parse

sim = parse(sys.argv[1])
print sim['warehouses'][0]['products'][0]

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
#        products
# orders
#     pos
#         row
#         col
#     num
#     products
