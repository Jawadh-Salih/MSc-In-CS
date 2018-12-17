from random import randint, random, shuffle
from node import Node
from graph import Graph
from utils import create_zipf_nodes, cumulative_prob_dist, create_nodes, get_prob_dict, create_init_graph, create_edge, cal_degree, get_random_user, get_current_degree_probs, insertEdge, get_random_max_prob_movie, plot_degree_distibution, get_alpha_for_degree_dist, tot_degree, wieghted_choice

import numpy as np
import matplotlib.pyplot as plt
# Create some unique labels.
# Assuming that we have got some defined Nodes for Movies and Users.
# What is the data structure for Movies set. It should be a set, Users should be a set.
# Then both the sets has to be interacted with each other as dictionery data structure. 
#  This will be a dynamic dictionery where with the time, new M,U pairs are combined. 
m_nodes = randint(900, 1000)

M = create_nodes("M", m_nodes) # Should create a dictionary
U = create_nodes("U", 10000)
Z = create_nodes('Z', m_nodes)

G = Graph(M, U)
create_init_graph(M, U, G)

G.print_graph()
print([m.degree for m in M])
# Created graph should be connected. 
# need to define a probability.
# need to see whether nodes get upon it.


print('Initial Graph is created') # This initial Graph is a collection of Edges where pair of nodes from M, U are linked 
G.print_degree_dist(M)
cumulative_prob_dist(M)
cumulative_prob_dist(U)

def BA_Model() :
    for i in range(10000) :
        u = get_random_user(U)

        for m in M:
            if (m.cumulative_prob > random()) :
                # add an edge to k
                newU = Node(0, 'U' + str(len(U)))
                U.append(newU)
                G.insert_edge(newU, m)
                cumulative_prob_dist(M)
            
                break
            else :
                G.insert_edge(u, m)
                cumulative_prob_dist(M)


def add_new_user(G, U, M, num) :
    # should add this user to m nodes from M 
    # preserving the preferencial attachment behavior
    user = Node(0, 'U' + str(len(U)))
    val = random()
    for x in range(num) :
        for m in M : 
            if (m.cumulative_prob > val) :
                U.append(user)
                G.insert_edge(user, m)
                cumulative_prob_dist(M)
                break

def add_new_movie(G, U, M, num) :
    newM = Node(0, 'M' + str(len(M)))
    # Add a new Object
    val = random()
    for x in range(num):
        for u in U : 
            if (u.cumulative_prob > val) :
                M.append(newM)
                G.insert_edge(u, newM)
                cumulative_prob_dist(U)
                break 

def add_edge_to_graph(G, U, M, num) :
    # Adding an edge to the exisiting Graph.
    val = random()
    for x in range(num):
        u = get_random_user(U) 
        val = random()
        for m in M :
            if (m.cumulative_prob > val) :
                G.insert_edge(u, m)
                cumulative_prob_dist(M)
                break

def add_edge_with_pref(G, U, M, num):
    # Adding an edge with pref prob

    tempM = None
    tempU = None
    val = random()
    for x in range(num) :
        for m in M :
            if (m.cumulative_prob > val) :
                tempM = m
                break
        val = random()
        for u in U :
            if (u.cumulative_prob > val) :
                tempU = u
                break
        
        G.insert_edge(tempU, tempM)
        cumulative_prob_dist(M)
        cumulative_prob_dist(U)

def Pref_Model() :
    for i in range(10000) :
    # Can add a new User. adding the user with the preferencial probability.
        val = random()
        for m in M:
            if (m.cumulative_prob > val) :
                # add an edge to k
                newU = Node(0, 'U' + str(len(U)))
                U.append(newU)
                G.insert_edge(newU, m)
                cumulative_prob_dist(M)
                break
        # Add a new Object
        for u in U : 
            if (u.cumulative_prob > random()) :
                newM = Node(0, 'M' + str(len(M)))
                M.append(newM)
                G.insert_edge(u, newM)
                cumulative_prob_dist(U)
                break 

        # Adding an edge to the exisiting Graph.
        u = get_random_user(U) 
        val = random()
        for m in M :
            if (m.cumulative_prob > val) :
                G.insert_edge(u, m)
                cumulative_prob_dist(M)
                break
        
        # Adding an edge with pref prob
        tempM = None
        tempU = None
        val = random()
        for m in M :
            if (m.cumulative_prob > val) :
                tempM = m
                break
        val = random()
        for u in U :
            if (u.cumulative_prob > val) :
                tempU = u
                break
        
        G.insert_edge(tempU, tempM)
        cumulative_prob_dist(M)
        cumulative_prob_dist(U)

def Pref_Model_Actual(iters) :
    for x in range(iters) :

        add_new_user(G, U, M, randint(1,10))
        add_new_movie(G, U, M, randint(1,10))
        # add_edge_to_graph(G, U, M, randint(1,10))
        add_edge_with_pref(G, U, M, randint(1,10))
Pref_Model_Actual(1000)

G.print_degree_dist(M)

jet= plt.get_cmap('jet')
colors = iter(jet(np.linspace(0,1,200)))
max_degree = max(m.degree for m in M)

create_zipf_nodes(Z, max_degree, 2)
plot_degree_distibution(plt, Z, next(colors))
create_zipf_nodes(Z, max_degree, 1)
plot_degree_distibution(plt, Z, next(colors))
plot_degree_distibution(plt, M, next(colors))
plot_degree_distibution(plt, U, next(colors))
# plot_degree_distibution(plt, U, next(colors))

plt.show()


