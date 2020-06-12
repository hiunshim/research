# Copyright 2021, Hiun Shim, All rights reserved.

from matplotlib import pyplot as plt
import networkx as nx

def plot_graphs(graph1, graph2, type="design"):
    if type == "design":
        plt.subplot(1, 2, 1) # index 2
        plt.title("Design MST")
        # pos = nx.spring_layout(graph1)                ##### WITH TRANS
        pos=nx.get_node_attributes(graph1,'pos')        ########## WITHOUT TRANS
        # labels = nx.get_edge_attributes(graph1,'weight')
        # nx.draw_networkx_edge_labels(graph1,pos,edge_labels=labels)
        nx.draw_networkx_labels(graph1, pos, font_size=8, font_family="sans-serif")
        nx.draw(graph1,pos,font_size=8)
        plt.axis("off")
    else:
        plt.subplot(1, 2, 1) # index 2
        plt.title("Ground MST")
        # pos = nx.spring_layout(graph1)                ##### WITH TRANS
        pos=nx.get_node_attributes(graph1,'pos')        ########## WITHOUT TRANS
        # labels = nx.get_edge_attributes(graph1,'weight')
        # nx.draw_networkx_edge_labels(graph1,pos,edge_labels=labels)
        nx.draw_networkx_labels(graph1, pos, font_size=8, font_family="sans-serif")
        nx.draw(graph1,pos,font_size=8)
        plt.axis("off")

    plt.subplot(1, 2, 2) # index 2 
    plt.title("Ground")
    # pos = nx.spring_layout(graph2)            ##### WITH TRANS
    pos=nx.get_node_attributes(graph2,'pos')    ########## WITHOUT TRANS
    # labels = nx.get_edge_attributes(graph2,'weight')
    # nx.draw_networkx_edge_labels(graph2,pos,edge_labels=labels)
    nx.draw_networkx_labels(graph2,pos, font_size=8, font_family="sans-serif")
    nx.draw(graph2,pos,font_size=8)
    plt.axis("off")    
    