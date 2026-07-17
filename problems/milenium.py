gridx = [
    [1, 2, None, 3],
    [4, None, 5, 6],
    [None, 7, 8, 9],
]

def encode(grid):
    height = len(grid)
    width = len(grid[0])
    values = []
    blocked = set()
    
    for r, row in enumerate(grid):
        cells = enumerate(row) if r % 2 == 0 else reversed(list(enumerate(row)))
        for c, val in cells:
            if val is None:
                blocked.add((r, c))
            else:
                values.append(val)
        
    # for r, row in enumerate(grid):
    #     for c, val in enumerate(row):
    #         if val is None:
    #             blocked.add((r, c))
    #         else:
    #             values.append(val)
    
    
    return {'width': width, 'height': height, 'values': values, 'blocked': sorted(blocked)}
    
def decode(payload):
    clean_list = []
    width = payload['width']
    height = payload['height']
    blocked = payload['blocked']
    values = payload['values'].copy()

    for r in range(height):
        row = [None] * width
        
        # Match encode: even rows go left-to-right, odd rows go right-to-left
        cols = range(width) if r % 2 == 0 else range(width-1, -1, -1)
        
        for c in cols:
            if (r, c) not in blocked:
                row[c] = values.pop(0)
        
        clean_list.append(row)

    return clean_list
    #for each row know where the None is inserted
    # loop over values


    
payloadx = encode(gridx)
print(payloadx)

playload = {
    'width': 4,
    'height': 3,
    'values': [1, 2, 3, 6, 5, 4, 7, 8, 9],
    'blocked': {(0, 2), (1, 1), (2, 0)},
}

gridy = decode(payloadx)
print("Decoded:", gridy)

#assert gridx==gridy
assert encode(gridx) == {
    'width': 4,
    'height': 3,
    'values': [1, 2, 3, 6, 5, 4, 7, 8, 9],
    'blocked': [(0, 2), (1, 1), (2, 0)]
}

assert decode(payloadx) == [
    [1, 2, None, 3],
    [4, None, 5, 6],
    [None, 7, 8, 9],
]