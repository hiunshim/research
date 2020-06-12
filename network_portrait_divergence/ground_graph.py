# Copyright 2021, Hiun Shim, All rights reserved.

from collections import defaultdict
import pandas as pd
import prims

def ground_graph(file, with_transformer):
    ground_df = pd.read_stata(file)
    ground_coordinates = {} 

    ######### THIS IS WITH TRANSFORMER ################################
    if with_transformer:
        ground_coordinates[0] = (ground_df.loc[0, 'lon_tx'], ground_df.loc[0, 'lat_tx'])
        ground_connections = defaultdict(set)
        # ground_df = ground_df.dropna()
        for row in range(0, len(ground_df)):
            ground_connections[ground_df.loc[row, "pole_connected_id"]].add(ground_df.loc[row, "id"])
            ground_coordinates[ground_df.loc[row, 'id']] = (ground_df.loc[row, 'lon'], ground_df.loc[row, 'lat'])
       
        # distances = prims.generate_graph_distance(ground_coordinates)
        # ground_mst = prims.create_spanning_tree(distances, 0)

        # real_graph = prims.generate_graph(ground_connections, ground_coordinates)
        # real_zss = prims.generate_zss(ground_connections, 0)

        # mst_graph = prims.generate_graph(ground_mst, ground_coordinates)
        # mst_zss = prims.generate_zss(ground_mst, 0)
    ######################################################################

    ####### THIS IS WITHOUT TRANSFORMER #################################
    else:
        ground_coordinates[0] = (ground_df.loc[0, 'lon'], ground_df.loc[0, 'lat'])
        ground_connections = defaultdict(set)
        # ground_df = ground_df.dropna()
        for row in range(0, len(ground_df)):
            ground_connections[ground_df.loc[row, "pole_connected_id"]].add(ground_df.loc[row, "id"])
            ground_coordinates[ground_df.loc[row, 'id']] = (ground_df.loc[row, 'lon'], ground_df.loc[row, 'lat'])
       
        # ground_coordinates[ground_df.loc[0, 'id']] = (ground_df.loc[0, 'lat'], ground_df.loc[0, 'lon'])
        # ground_connections = defaultdict(set)
        # # ground_df = ground_df.dropna()
        # for row in range(1, len(ground_df)):
        #     ground_connections[ground_df.loc[row, "pole_connected_id"]].add(ground_df.loc[row, "id"])
        # for row in range(0, len(ground_df)):
        #     ground_coordinates[ground_df.loc[row, 'id']] = (ground_df.loc[row, 'lat'], ground_df.loc[row, 'lon'])
        
        # distances = prims.generate_graph_distance(ground_coordinates)
        # ground_mst = prims.create_spanning_tree(distances, ground_df.loc[0, 'id'])

        # real_graph = prims.generate_graph(ground_connections, ground_coordinates)
        # real_zss = prims.generate_zss(ground_connections, ground_df.loc[0, 'id'])

        # mst_graph = prims.generate_graph(ground_mst, ground_coordinates)
        # mst_zss = prims.generate_zss(ground_mst, ground_df.loc[0, 'id'])
    ########################################################################

    distances = prims.generate_graph_distance(ground_coordinates)
    ground_mst = prims.create_spanning_tree(distances, 0)

    real_graph = prims.generate_graph(ground_connections, ground_coordinates)
    real_zss = prims.generate_zss(ground_connections, 0)

    mst_graph = prims.generate_graph(ground_mst, ground_coordinates)
    mst_zss = prims.generate_zss(ground_mst, 0)


    groundMST_polylines = prims.generate_coordinates_connections(ground_connections, ground_coordinates)
    ground_polylines = prims.generate_coordinates_connections(ground_mst, ground_coordinates)


    return real_graph, real_zss, mst_graph, mst_zss, groundMST_polylines, ground_polylines
    