# Copyright 2021, Hiun Shim, All rights reserved.

from design_graph import design_graph
from ground_graph import ground_graph
import os
import re
from zss import simple_distance
from portrait_divergence import portrait_divergence, portrait_divergence_weighted
from write_csv import write_csv, polylines_csv
from make_img import designMST_ground_img, groundMST_ground_img, designMST_groundMST_img

def save_data(with_transformer):
    design_files, ground_files = [], []
    for file in os.listdir("./../data/design"):
        design_files.append(file)
    design_files.sort()
    for file in os.listdir("./../data/ground"):
        ground_files.append(file)
    ground_files.sort()

    npd_data = []
    npd_weighted_data = []
    zss_data = []
    for i in range(min(len(design_files), len(ground_files))):
        design_file = design_files[i]
        ground_file = ground_files[i]
        design_url = "./../data/" + "design/" + design_file
        ground_url = "./../data/" + "ground/" + ground_file
        design_file_name = re.search(r'(d[0-9]+)', design_file).group(1)
        ground_file_name = re.search(r'(g[0-9]+)', ground_file).group(1)
        transformer_id = re.search(r'([0-9]+)', ground_file).group(1)
        graph1, zss1, designMST_polylines = design_graph(design_url, with_transformer)
        graph2, zss2, groundMST_graph, groundMST_zss, groundMST_polylines, ground_polylines = ground_graph(ground_url, with_transformer)
        
        npd_data.append([design_file_name, ground_file_name, transformer_id, portrait_divergence(graph1, graph2), portrait_divergence(graph2, groundMST_graph), portrait_divergence(graph1, groundMST_graph)])
        npd_weighted_data.append([design_file_name, ground_file_name, transformer_id, portrait_divergence_weighted(graph1, graph2), portrait_divergence_weighted(graph2, groundMST_graph), portrait_divergence_weighted(graph1, groundMST_graph)])
        zss_data.append([design_file_name, ground_file_name, transformer_id, simple_distance(zss1, zss2), simple_distance(zss2, groundMST_zss), simple_distance(zss1, groundMST_zss)])
        
        polylines_csv(design_file_name, ground_file_name, transformer_id, designMST_polylines, groundMST_polylines, ground_polylines, with_transformer)
        
        designMST_ground_img(graph1, graph2, design_file_name, ground_file_name, with_transformer)
        groundMST_ground_img(groundMST_graph, graph2, ground_file_name, with_transformer)
        designMST_groundMST_img(graph1, groundMST_graph, ground_file_name, with_transformer)

    write_csv(npd_data, npd_weighted_data, zss_data, with_transformer)
    # polylines_csv(polylines, with_transformer)

# save_data(INCLUDE_TRANSFORMER)
save_data(True)
save_data(False)