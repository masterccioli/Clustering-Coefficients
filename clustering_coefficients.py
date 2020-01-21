# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:51:29 2020

@author: maste

This is a re-implementation of networkx.algorithms.cluster.clustering
Because idiots insist on using inefficient data structures to represent networks
implements Saramäki, J., Kivelä, M., Onnela, J.-P., Kaski, K., & Kertész, J. (2007). Generalizations of the clustering coefficient to weighted complex networks. Physical Review E, 75(2), 027105. https://doi.org/10.1103/PhysRevE.75.027105

"""

import numpy as np

def get_ave_clustering_coefficient(x): # x is some symmetrical distance matrix
    
    nodes = list(np.arange(len(x))) #get nodes
    c = [] # list of clustering coefficients; corresponds to order in node list
    for u in nodes:

        v_list = nodes.copy()
        v_list.remove(u)
        out = []
        for v in v_list:

            w = v_list.copy()
            w.remove(v)
            out.append(x[u][v] * np.dot(x[u][w], x[v][w]))
        num = np.power(sum(out), 1/3)
    
        deg_u = len(np.where(x[u] > 0)[0]) - 1 # subtract one to remove the reflexive element
        if deg_u >= 2: # if the node is connected to fewer than three other nodes, effectively zero
            c_u = num / (deg_u * (deg_u - 1))

            c.append(c_u)
        else:
            c.append(0)
            
    
    if len(c) == 0:
        print('\t' + str(0))
        return 0
    print('\t' + str(np.mean(c)))
    return np.mean(c)

def get_all_clustering_coefficients(x): # x is some symmetrical distance matrix
    
    nodes = list(np.arange(len(x))) #get nodes
    c = [] # list of clustering coefficients; corresponds to order in node list
    for u in nodes:

        v_list = nodes.copy()
        v_list.remove(u)
        out = []
        for v in v_list:

            w = v_list.copy()
            w.remove(v)
            out.append(x[u][v] * np.dot(x[u][w], x[v][w]))
        num = np.power(sum(out), 1/3)
    
        deg_u = len(np.where(x[u] > 0)[0]) - 1 # subtract one to remove the reflexive element
        if deg_u >= 2: # if the node is connected to fewer than three other nodes, effectively zero
            c_u = num / (deg_u * (deg_u - 1))

            c.append(c_u)
        else:
            c.append(0)
            
    
    if len(c) == 0:
        print('\t' + str(0))
        return 0
    print('\t' + str(c))
    return c
