import helper
import numpy as np

data = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
]

# data = helper.get_puzzle_input(d=15, y=2021)

axis_0 = len(data)
axis_1 = len(data[0])
data = [int(x) for x in ''.join(data)]
data = np.array(data).reshape((axis_0, axis_1))
print(data)


def nbors2(y, x, ylen, xlen):
    left = x-1 if x-1 > -1 else x
    right = x+2 if x+2 < axis_1 else x+1
    up = y-1 if y-1 > -1 else y
    down = y+2 if y+2 < axis_0 else y+1

    data[up:down, left:right]
    
    out_coords = []
    left = x-1 if x-1 > 0 else np.nan
    right = x+1 if x+1 < xlen else np.nan
    up = y-1 if y-1 > 0 else np.nan
    down = y+1 if y+1 < ylen else np.nan

    L = [y, left]
    R = [y, right]
    U = [up, x]
    D = [down, x]
    UL = [up, left]
    UR = [up, right]
    DL = [down, left]
    DR = [down, right]
    
    all_nb_coords = [L, R, U, D, UL, UR, DL, DR]
    
    for coords in all_nb_coords:
        if np.nan not in coords:
            crds = (coords[0], coords[1])
            out_coords.append(crds)
    return out_coords
    

days = 5
flashes = 0
for d in range(days):
    
    # Increase energy level +1
    data += 1
    
    # Reset energy levels > 9 to 0
    
    
    # Count initial flashes
    # flashes += np.count_nonzero(data == 0)
    
    print(f'------\nDay {d+1}\n')#, np.where(data == 0, np.nan, data))
    init_flashes = np.count_nonzero(data > 9)
    prev_flashes = init_flashes
    new_flashes = 0
    
    do_it = True
    
    while do_it:
        data = np.where(data > 9, 0, data)
        flash_y, flash_x = np.where(data == 0)
        flash_nbors = []
        for y, x in zip(flash_y, flash_x):
            flash_nbors.append(nbors2(y, x, axis_1, axis_0))

        for flash in flash_nbors:
            for coord in flash:
                data[coord] += 1
        
        data = np.where(data > 9, 0, data)
        do_it = False
        
        # end_init = np.count_nonzero(data == 0)
        # print(data)
        # print(start_init, end_init)
        # do_it = False if start_init == end_init else True
        
    
    # print(data)
    # print(f'Flashes: {flashes}')