# Copyright 2021, Hiun Shim, All rights reserved.

import numpy as np
from matplotlib import pyplot as plt
import prims

def plot_mst(mst1, coord1, mst2, coord2):#, string):#, i, save=False):
    # mst1 = prims.create_spanning_tree(prims.generate_graph_distance(coord1), 0)
    # mst2 = prims.create_spanning_tree(prims.generate_graph_distance(coord2), 0)
    coordinates1 = prims.generate_coordinates_connections(mst1, coord1)     # [[(2, 10), (5, 9)], [(5, 9), (9, 7)]]
    coordinates2 = prims.generate_coordinates_connections(mst2, coord2)     # [[(2, 10), (5, 9)], [(5, 9), (9, 7)]]
    # print(coordinates1, coordinates2)

    data1 = np.array(coordinates1)
    x1, y1 = data1.T
    plt.subplot(1, 2, 1) # row 1, col 2 index 1
    plt.scatter(x1, y1)
    plt.plot(x1, y1)
    plt.title("Design")
    plt.xlabel('X')
    plt.ylabel('Y')

    data2 = np.array(coordinates2)
    x2, y2 = data2.T
    plt.subplot(1, 2, 2) # index 2
    plt.scatter(x2, y2)
    plt.plot(x2, y2)
    plt.title("Ground")
    plt.xlabel('X')
    plt.ylabel('Y')

    # plt.savefig(string)
    plt.show()