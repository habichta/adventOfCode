import numpy as np
from operator import itemgetter

def PolygonArea(corners):
        n = len(corners) # of corners
        area = 0.0
        for i in range(n):
            if corners[i][0] > 390 or corners[i][1] > 390 or corners[i][0] < 0 or corners[i][1] < 0:
                return -1
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        area = abs(area) / 2.0
        return area

with open('input.txt') as f:
    data=[]
    for line in f:
        x = line.split(',')
        data.append([int(x[0]),int(x[1])])
        
    from scipy.spatial import Voronoi, voronoi_plot_2d
    data = np.array(data)
    vor = Voronoi(data)
    #print(vor.ridge_vertices)
    import matplotlib.pyplot as plt
    areas = []
    for pr in vor.point_region:
        re = vor.regions[pr]
        if not -1 in re:
            vert=[vor.vertices[v] for v in re]
            areas.append((PolygonArea(vert),vert,re))

    max_area = max(areas,key=itemgetter(0))
    reg = max_area[2]
    ridge_ind = [[x,y] for x, y in zip(reg[:-1], reg[1:])]
    ridge_ind2 = [[ridge_ind[0][0], ridge_ind[-1][1]]]
    ridges = []
    ridges += ridge_ind
    ridges += ridge_ind2

    for i, ridge_points in enumerate(vor.ridge)
    

    print(ridges)

    voronoi_plot_2d(vor)
    plt.show()
   
    
    


    