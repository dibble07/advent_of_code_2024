import numpy as np


def get_route(map):

    status = 0
    orient = 0
    map_orient = np.empty(map.shape, dtype=object)
    for index, _ in np.ndenumerate(map_orient):
        map_orient[index] = set()

    while status == 0:
        guard_loc_ind = np.argwhere(map == "^")[0]
        if guard_loc_ind[0] == 0:
            status = 1
        elif orient in map_orient[*guard_loc_ind]:
            status = 2
        else:
            map_orient[*guard_loc_ind].add(orient)
            guard_loc_next_ind = guard_loc_ind + [-1, 0]
            guard_loc_next = map[*guard_loc_next_ind]
            if guard_loc_next in ".X":
                map[*guard_loc_ind] = "X"
                map[*guard_loc_next_ind] = "^"
            elif guard_loc_next in "#O":
                map = np.rot90(map)
                orient = (orient + 1) % 4
    map = np.rot90(map, k=4 - orient)

    return map, status
