#Linear Threshold Model
#%config IPCompleter.greedy=True
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
from random import *
import random


G = nx.Graph()
with open(r'./Epinions.txt','r') as f:
	lines=f.readlines()
for line in lines:
	a=list(map(float,line.split()))
	#G.add_edge(a[0],a[1],weight=a[2])
	G.add_edge(a[0], a[1], weight = round(random.uniform(0,1), 2))
#degree_sequence = sorted([(n, d) for (n, d) in G.degree()], key = lambda x: x[1], reverse=True)
size_graph = len(G)


#thld = sorted([(n, d) for (n, d) in G.degree()])
#print("\n\n\n\n\nNode, Degree : = ", thld)


thrld = {}
for i in list(G.nodes()):
    thrld[i]=(round(random.uniform(0,1), 3))



#print("\n\n\n Threshold :", thrld)           #thldl is the array containing thresholds
iis = size_graph/10
seed = int(iis)


#degree Centrality
#cent = nx.degree_centrality(G)
#closeness Centrality
cent = nx.closeness_centrality(G)
#eigenvector Centrality
#cent = nx.eigenvector_centrality(G, max_iter=100000, tol=1e-06, nstart=None, weight=None)



#print("Centrality =", cent)
cent_list = [(k, v) for (k, v) in cent.items()]
cent_sorted = sorted([(n, d) for (n, d) in cent_list], key = lambda x: x[1], reverse=True)
#print("\n\n\centrality sorted: ", cent_sorted)

initial_infected_nodes = cent_sorted[0:seed]
infected_nodes = [n for (n, d) in initial_infected_nodes]



#maximum degree
#initial_infected_nodes = degree_sequence[0:seed]
#infected_nodes = [n for (n, d) in initial_infected_nodes]
#print("\n\n\n\nInfected Nodes = ", infected_nodes)

print("\n\n\n\n")
queue = deque(infected_nodes)
#print(queue)

#print(queue.popleft())
#print(queue.popleft())
# ©Shivang XD
#print(queue)

iterations = 0

while len(infected_nodes)!= len(G):

    if not queue:
        break

    act_node = queue.popleft()
    #print("\n\nActivated node : ", act_node)
    con_nodes = [k for (k,v) in G[act_node].items()]
    #print("\n\nNodes attached to the active node : ", con_nodes)


    
    
    #infections probabilities
    size_con = len(con_nodes)
    rand_probs = []
    
    for i in con_nodes:
        wgt = G[act_node][i]['weight']
        weights = [wgt, 1-wgt]
        population = [1, 0]
        prob = choices(population, weights)
        rand_probs.extend(prob)
    
    
    
    #print("Random Probabilities : ", rand_probs)


    #dictionary for nodes along with probabilities
    new_dict = dict(zip(con_nodes, rand_probs))
    #print(new_dict)

    new_con_nodes = [k for (k, v) in new_dict.items() if v == 1 ]
    n_i_nodes = []

    for i in new_con_nodes:
        wgt = G[act_node][i]['weight']

        thrld[i] = thrld[i]-wgt
        if(thrld[i]<=0):
            n_i_nodes.append(i)


    #print("\n\nNew Threshold values :", thrld)


    new_infected_nodes = [x for x in n_i_nodes if x not in infected_nodes]
    #print("\n\n New Infected nodes : ", new_infected_nodes)

    infected_nodes[1:1] = new_infected_nodes
    #print("\n\n\n\nInfected Nodes = ", infected_nodes)

    queue.extend(new_infected_nodes)
    #print("\n\n\n\n Queue ", queue)
    iterations = iterations + 1





print("\n\n Number of vertices : ", size_graph)
print("\n\n Number of edges : ", G.number_of_edges())
print("\n\n\n\nNumber of iterations :", iterations)
print("\n\n\n\n Percentage of nodes infected: ", len(infected_nodes)*100/size_graph)
print("\n\n\n\n Number of seeds taken: ", seed)
