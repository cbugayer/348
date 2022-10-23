from importlib.resources import path
from numpy import empty
from tomlkit import TOMLDocument
from expand import expand
from collections import deque
from collections import defaultdict



def a_star_search(dis_map, time_map, start, end):
    pathl = []
    opens = []
    closeds = []
    opens.append(start)
    parent_of = {}
    travel_from_start = defaultdict(lambda: float('inf'))
    travel_from_start[start] = 0
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = dis_map[start][end]
    
    while opens:
        current = opens[0]
        for o in opens:
            if f_score[o] < f_score[current]:
                current = o
            if f_score[o] == f_score[current]:
                if dis_map[o][end] < dis_map[current][end]:
                    current = o
        if current == end:
            pathl.append(current)
            while current in parent_of.keys():
                current = parent_of[current]
                pathl.insert(0, current)
            return pathl
        opens.remove(current)
        closeds.append(current)
        for child in expand(current, time_map):
            ten_g = travel_from_start[current] + time_map[current][child]
            if ten_g < travel_from_start[child]:
                parent_of[child] = current
                travel_from_start[child] = ten_g
                f_score[child] = ten_g + dis_map[child][end]
                if child not in opens and child not in closeds:
                    opens.append(child)
    return

            
"""
    while min_place != end:
        for child in expand(min_place, time_map):
            if child not in closed:
                if child not in parent_of:
                    parent_of[child] = min_place
                travel_from_start[child] = travel_from_start[parent_of[child]] + time_map[parent_of[child]][child]
                f_score[child] = travel_from_start[child] + dis_map[child][end]

                


        closed.append(min_place)
        del f_score[min_place]
        print(f_score)
        tiers = []
        for c in f_score.keys():
            min_value = min(f_score.values())
            if f_score[c] == min_value:
                tiers.append(c)
                min_place = tiers[0]
        if len(tiers) > 1:
            min_dis = dis_map[tiers[0]][end]
            for tier in tiers:
                if min_dis > dis_map[tier][end]:
                    min_dis = dis_map[tier][end]
                    min_place = tier
    path.append(end)
    while parent_of[end] != start:
        path.insert(0, parent_of[end])
        end = parent_of[end]
    path.insert(0, start)
    return path
    
    path.append(min_place)
    while min_place != start:
        path.insert(0, parent_of[min_place])
        min_place = parent_of[min_place]
    return path
    """



def depth_first_search(time_map, start, end):
    fringe = deque()
    path = []
    diction = {}

    fringe.append(start)
    while fringe:
        vertex = fringe.pop()
        if vertex == end:
            path.append(vertex)
            if vertex in diction:
                while diction[vertex] != start:
                    path.insert(0, diction[vertex])
                    vertex = diction[vertex]
                path.insert(0, start)
            return path
        else:
            for child in expand(vertex, time_map):
                fringe.append(child)
                diction[child] = vertex
    return path


def breadth_first_search(time_map, start, end):
    fringe = deque()
    path = []
    closed = []
    diction = {}

    fringe.append(start)
    closed.append(start)

    while fringe:
        vertex = fringe.popleft()
        
        if vertex == end:
            path.append(vertex)
            if vertex in diction:
                while diction[vertex] != start:
                    path.insert(0, diction[vertex])
                    vertex = diction[vertex]
                path.insert(0, start)
            return path
        else:
            for child in expand(vertex, time_map):
                if child not in closed:
                    fringe.append(child)
                    closed.append(child)
                    
                    diction[child] = vertex
    return path


    
