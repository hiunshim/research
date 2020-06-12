# Copyright 2021, Hiun Shim, All rights reserved.

import pandas as pd
import prims

def design_graph(file, with_transformer):
    design_df = pd.read_stata(file)
    design_coordinates = {}
    ######### THIS IS WITH TRANSFORMER ###############################
    if with_transformer:
        design_coordinates[0] = (design_df.loc[0, 'lon_tx'], design_df.loc[0, 'lat_tx'])
        for i in range(1, len(design_df)):
            design_coordinates[design_df.loc[i, 'id']] = (design_df.loc[i, 'lon'], design_df.loc[i, 'lat'])
            # WITHOUT ID design_coordinates[i] = (design_df.loc[i, 'lat'], design_df.loc[i, 'lon'])
    ##################################################################
    else:
    ####### THIS IS WITHOUT TRANSFORMER ##############################
        # design_coordinates[0] = (design_df.loc[0, 'lat_tx'], design_df.loc[0, 'lon_tx'])
        for i in range(0, len(design_df)):
            design_coordinates[design_df.loc[i, 'id']] = (design_df.loc[i, 'lon'], design_df.loc[i, 'lat'])
            # WITHOUT ID design_coordinates[i] = (design_df.loc[i, 'lat'], design_df.loc[i, 'lon'])
    ###################################################################
    distances = prims.generate_graph_distance(design_coordinates)
    design_mst = prims.create_spanning_tree(distances, 0)

    graph = prims.generate_graph(design_mst, design_coordinates)
    zss = prims.generate_zss(design_mst, 0)
    polylines = prims.generate_coordinates_connections(design_mst, design_coordinates)



    return graph, zss, polylines

