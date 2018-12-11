import numpy as np, matplotlib.pyplot as plt, collections as co
from scipy.spatial import Voronoi, voronoi_plot_2d
def find_region_with_voronoi(data): #O(K (N log(N)))
    vor, areas, points, areas_points = Voronoi(np.array(data)),[],[],[]
    for pr in vor.point_region:
        re = vor.regions[pr]
        if not -1 in re:
            ridges = [sorted([x, y]) for x, y in zip(re[:-1], re[1:])] + [sorted([re[0], re[-1]])]
            points = [list(vor.ridge_points[i]) for i,rpoint in enumerate(vor.ridge_vertices) if sorted(rpoint) in ridges]
            c = co.Counter([p for sl in points for p in sl])
            center_point, peripheral_points = [list(vor.points[x[0]]) for x in c.items() if x[1]>1],[list(vor.points[x[0]]) for x in c.items() if x[1]==1]
            areas_points.append([center_point,peripheral_points])
    voronoi_plot_2d(vor)
    plt.show()
    return areas_points
def area_c(points):
    x_coord, x_center = [x[0] for x in points[1]], points[0][0][0]
    y_coord, y_center = [x[1] for x in points[1]], points[0][0][1]
    x_min,y_min,x_max,y_max = int(min(x_coord)), int(min(y_coord)), int(max(x_coord)), int(max(y_coord))
    area = 0
    print(x_center,y_center)
    for x in range(0,390):
        for y in range(0,390):

            diff_p = [abs(int(p[0])-x)+abs(int(p[1])-y) for p in points[1]]
            diff_c = abs(int(x_center)-x)+abs(int(y_center-y))
            if diff_c < min(diff_p):
                area+=1

    return area




from collections import defaultdict

file = open("input.txt")
points = [[int(s) for s in line.rstrip().split(",")] for line in file.readlines()]

area = defaultdict(lambda: 0)
infinite = set()


# manhattan distance function
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# xr = x_range, yr = y_range
xr = [i for i in range(min([a[0] for a in points]), max([a[0] for a in points]) + 1)]
yr = [i for i in range(min([a[1] for a in points]), max([a[1] for a in points]) + 1)]

# for part 2
within = 0

for y in yr:
    # check vertical edges
    edge_y = y == yr[0] or y == yr[-1]
    for x in xr:
        # check horizontal edges
        edge_x = x == xr[0] or x == xr[-1]
        # map all points to an array of [distance, point as string]
        d = sorted(map(lambda p: [dist(p, [x, y]), str(p)], points))
        # if closest distance is single closest distance (not duplicate)
        if d[0][0] != d[1][0]:
            area[d[0][1]] += 1
        # if on any of the edges it is infinite because it will extend infinitely
        if edge_x or edge_y:
            infinite.add(d[0][1])
        # if sum distances is smaller than 10000, its within the region (part2)
        within += sum([a[0] for a in d]) < 10000

# print max area that is not infinite
print(area)
print(infinite)
print(max([x[1] for x in area.items() if str(x[0]) not in infinite]))
print(within)




with open('input.txt') as f:
    points_info = find_region_with_voronoi([line.split(',') for line in f])
    for point in points_info:
        print(area_c(point))






   
    
    


    