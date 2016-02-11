import sys

def parse(fn):
    sim = {}
    with open(sys.argv[1], "r") as input:
        data = input.read().split("\n")[:-1]

    # params
    sim['rowsInArea'] = int(data[0].split(" ")[0])
    sim['columnsInArea'] = int(data[0].split(" ")[1])
    sim['numDrones'] = int(data[0].split(" ")[2])
    sim['deadline'] = int(data[0].split(" ")[3])
    sim['maxLoad'] = int(data[0].split(" ")[4])

    # weights
    sim['numProductTypes'] = int(data[1])
    sim['productWeights'] = list(map(int, data[2].split(" ")))

    # availability
    numWarehouses = int(data[3])
    sim['numWarehouses'] = numWarehouses
    ln = 4

    warehouses = []
    for x in xrange(ln, ln + (2 * numWarehouses), 2):
        warehouses.append({
            'pos': {
                'row': int(data[x].split(" ")[0]),
                'col': int(data[x].split(" ")[1])
            },
            'items': data[x + 1].split(" ")
        })
    
    sim['warehouses'] = warehouses
    
    ln = ln + (numWarehouses * 2)

    numOrders = int(data[ln])
    sim['numOrders'] = numOrders
    ln += 1

    # orders
    orders = []
    for x in xrange(ln, ln + (3 * numOrders), 3):
        orders.append({
            'pos': {
                'row': int(data[x].split(" ")[0]),
                'col': int(data[x].split(" ")[1])
            },
            'num': int(data[x + 1]),
            'products': list(map(int, data[x + 2].split(" ")))
        })
    
    sim['orders'] = orders
    
    return sim
