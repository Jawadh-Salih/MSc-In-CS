# this is the utility python where the necessary ops and all are happend.

from node import Node
from edge import Edge

from random import randint, random, uniform, shuffle
from scipy.optimize import curve_fit
from math import log10
import matplotlib.pyplot as plt

def cal_degree(N, E) : # Calculate the degree of a node given the set of Edges.
    count = 0
    for e in E :
        if (N.label == e.vertex1.label or N.label == e.vertex2.label) :
            count = count + 1

    return count

def create_nodes(parent_label, count) :
    # this creates a set of Nodes
    nodes = []
    for val in range(0,count) :
        nodes.append(Node(0, parent_label + str(val)))
    
    return nodes

def create_edge(u, v) :
    e = Edge(u, v)

    return e

def create_init_graph(U, V, G) :
    # I have a set of nodes. Need to set the E out those nodes U,V
    n = randint(1, int((len(U)))) # n is the number of edges will be created. * len(V))/2
    # flag = True
    for i in range(n) :
        u = U[randint(0, len(U) - 1)]
        v = V[randint(0, len(V)) - 1]
        G.insert_edge(u, v)
    # while(flag) :
        
        # if (allHasEdges(U)) :
        #     flag = False
    
    return G

def allHasEdges(U) :
    for u in U :
        if (u.degree == 0) :
            return False
    return True        
def get_random_user(U) :
    index = randint(0, len(U) - 1)
    return U[index]

def insertEdge(G, u, v) :
    # Here we dont check for the duplicate.
    # flag = False 
    # for e in G:
    #     flag = True
    #     if (e.vertex1.label == u.label and e.vertex2.label == v.label) :
    #         # Now we have a duplicate.
    #         print('Duplicate')
    #         flag = False
    #         break
    # if (flag) :
    G.insert_edge(u, v)

def get_current_degree_probs(V, tot_degree) :
    probs = list()

    for v in V:
        prob = v.degree/tot_degree
        probs.append(prob)
        v.prob = prob

    return probs

def get_max_prob_movies(M) :

    max_prob = max(m.prob for m in M)
    movies = set()
    for m in M:
        if (max_prob == m.prob) :
            movies.add(m)
            # movie.degree = m.degree
            # movie.label = m.label
            # movie.prob = m.prob

    return movies

def get_random_max_prob_movie(M, pref_prob) :

    total_degree = tot_degree(M)
    max_prob_list = []
    for m in M :
        # now get the list 
        prob = (1.0 * m.degree)/ total_degree
        if (pref_prob < prob) :
            max_prob_list.append(m)
        # if m's probability is enough then it is likely to be connected to a user.
            
    randIndex = randint(0, len(max_prob_list) - 1)

    return max_prob_list[randIndex]
            
def sort_by_degree(V) :
    return sorted(V, key=lambda v: v.degree, reverse = True)
def plot_degree_distibution(V) :
    # Sort this by degree.
    newV = sort_by_degree(V)
    # plot above distribution.
    degrees = [v.degree for v in newV]
    zipf = get_zipf_curve(degrees[0], len(V))
    
    plt.plot(zipf, 'bo')
    plt.plot(degrees, 'ro')
    plt.show()
    print(max(degrees))
    print(degrees[0])
    plt.loglog(degrees, 'ro')
    plt.loglog(zipf, 'bo')
    plt.show()
def tot_degree(V) :
    return sum(v.degree for v in V)

def get_alpha_for_degree_dist(V) :
    newV = sort_by_degree(V)
    # here we need to get an interpolation for the graph and assume or
    sum_alpha = 0
    for i in range(1, len(newV)) :
        alphaVal = (log10(newV[i].degree + 1)/log10(i + 1))
        sum_alpha = sum_alpha + alphaVal
    alpha = sum_alpha/len(newV)
    print(alpha)
    return alpha


def func_power_law (x, m, c, c0) :
    return c0 + x**m*c

def get_degrees(V) :
    return [v.degree for v in V]


def get_zipf_curve(max_degree, length) :
    zipf = list()
    for i in range(0, length) :
        zipf.insert(i, 1.0 * max_degree/(i+1))

    return zipf

def wieghted_choice(M) :
    total = sum(m.degree for m in M)
    r = uniform(0, total)
    upto = 0
    shuffle(M)
    for m in M:
        if (upto + m.degree >= r):
            return m
        upto += m.degree

#  Need to write a code 
# have the degrees of M. 
# Get the maximum degree Node out of it. 
def preferable_Node(M) :
    max_degree = max(get_degrees(M))
    rand_val = randint(0, max_degree)
    # get one node from the nodes, where degree is greater than the random degree.
    shuffle(M)
    for m in M:
        if (m.degree > rand_val) :
            return 

def get_prob_dict(U) :
    sum_degrees = tot_degree(U)
    probs = [{u.label, (1.0 * u.degree)/sum_degrees} for u in U]

    return probs

def cum_prob_dist(U):
    sum_degrees = tot_degree(U)
    cum = 0.0
    for u in U :
        if (u.degree == 0) :
            cum = cum + (1.0 /sum_degrees)
        cum = cum + (1.0 * u.degree)/sum_degrees
        u.cum_prob = cum