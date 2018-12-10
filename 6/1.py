import numpy as np, matplotlib.pyplot as plt, collections as co
from scipy.spatial import Voronoi, voronoi_plot_2d
from operator import itemgetter
def gauss_area(corners):
        n,area = len(corners),0.0
        for i in range(n):
            if corners[i][0] > 390 or corners[i][1] > 390 or corners[i][0] < 0 or corners[i][1] < 0: return -1
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        return abs(area) / 2.0

def find_region_with_voronoi(data): #O(K (N log(N)))
    vor, areas, points = Voronoi(np.array(data)),[],[]
    for pr in vor.point_region:
        re = vor.regions[pr]
        if not -1 in re:
            vert = [vor.vertices[v] for v in re]
            areas.append((gauss_area(vert), vert, re))
    reg_max = max(areas, key=itemgetter(0))[2]
    ridges = [sorted([x, y]) for x, y in zip(reg_max[:-1], reg_max[1:])] + [sorted([reg_max[0], reg_max[-1]])]
    points = [list(vor.ridge_points[i]) for i,rpoint in enumerate(vor.ridge_vertices) if sorted(rpoint) in ridges]
    c = co.Counter([p for sl in points for p in sl])
    #voronoi_plot_2d(vor)
    #plt.show()
    return [list(vor.points[x[0]]) for x in c.items() if x[1]>1] , [list(vor.points[x[0]]) for x in c.items() if x[1]==1]

def area(center,periphery):
    x_coord = [x[0] for x in periphery]
    y_coord = [x[1] for x in periphery]
    x_min,y_min,x_max,y_max = min(x_coord), min(y_coord), max(x_coord), max(y_coord)

    #for range .... , compare manhatten with center point, count for center point

with open('input.txt') as f:
    center, periphery = find_region_with_voronoi([line.split(',') for line in f])
    area(center,periphery)


        






   
    
    


    