# Copyright 2021, Hiun Shim, All rights reserved.

from matplotlib import pyplot as plt
from plot_graph import plot_graphs

def designMST_ground_img(graph1, graph2, name1, name2, with_transformer):
    if with_transformer:
        file_name = "./../images/with_transformer/designMST_ground_images/"+name1+"_"+name2+".jpg"
    else:
        file_name = "./../images/without_transformer/designMST_ground_images/"+name1+"_"+name2+".jpg"
    plot_graphs(graph1, graph2, "design")
    plt.savefig(file_name)
    plt.clf()

def groundMST_ground_img(graph1, graph2, name, with_transformer):
    if with_transformer:
        file_name = "./../images/with_transformer/groundMST_ground_images/"+name+".jpg"
    else:
        file_name = "./../images/without_transformer/groundMST_ground_images/"+name+".jpg"
    plot_graphs(graph1, graph2, "ground")
    plt.savefig(file_name)
    plt.clf()

def designMST_groundMST_img(graph1, graph2, name, with_transformer):
    if with_transformer:
        file_name = "./../images/with_transformer/designMST_groundMST_images/"+name+".jpg"
    else:
        file_name = "./../images/without_transformer/designMST_groundMST_images/"+name+".jpg"
    plot_graphs(graph1, graph2, "ground")
    plt.savefig(file_name)
    plt.clf()
    