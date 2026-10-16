

from typing import Tuple, List, Set, Dict


def bruteforce(edges: List[List[int]]) -> Dict[Tuple[int, int], int]:
    # [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]
    dist_dict: Dict[Tuple[int, int], int] = {}

    if not edges or len(edges) == 0:
        return dist_dict  # return empty dict
    
    start_points: Dict[int, Set[int]] = {}
    for ed in edges:
        # collect the comprehensive starting nodes
        ed_tup: Tuple[int, int] = (ed[0], ed[1])
        if ed[0] in start_points:
            start_points[ed[0]].add(ed[1])
        else:
            start_points[ed[0]] = set([ed[1]])

        # the edge that is in the list, direct connection
        if ed_tup in dist_dict:
            if dist_dict[ed_tup] > 1: # if the point has direct connection, it's length is one
                dist_dict[ed_tup] = 1
        else:
            dist_dict[ed_tup] = 1


    print(f"FIRST RUN: STARTING POINTS: {start_points}")
    print(f"FIRST RUN: DISTANCES: {dist_dict}")
    print("---------------------")

    for st in start_points:  # loop over all starting points
        for conn in start_points[st]: # loop direct connections
            print(f" start: {st} --  to: {conn}") # edge length 1
            if conn in start_points:  # start traversing further edges
                print(f" start: {st} --  to: {conn} --  further: {start_points[conn]}")
                new_conns = start_points[conn]  # direct edges to the intermediate ones
                for nc in new_conns:
                    new_tup:Tuple[int, int] = (st, nc) # potential connection
                    if new_tup in dist_dict:  # there is a direct edge, so a loop
                        print(f"POTENTIAL LOOP: {st}-to-{conn}: {dist_dict[new_tup]}")
                    else:
                        dist_dict[new_tup] = dist_dict[(st, conn)] + 1  # further edges, so direct/intermediate edge + 1 = path lengtyh

    print(f"FINAL RUN: DISTANCES: {dist_dict}")
    print("---------------------")

    return dist_dict


if __name__ == "__main__":
    edges:List[List[int]] = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]
    bruteforce(edges)
