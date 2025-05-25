"""
File name: assignment.py
Description: function to compute the centrlity ranking of the nodes of a graph

Authors:
    - Berivan Alpagu (bax1020@alu.ubu.es), Melisa YURT (myx1020@alu.ubu.es)
    
License:
    This script is licensed under the MIT License. 
    https://opensource.org/licenses/MIT
"""
"""

import networkx as nx
import pandas as pd

def net_ranking(G, weights):
    pagerank = nx.pagerank(G)
    betweenness = nx.betweenness_centrality(G)

    df = pd.DataFrame({
        'node_id': list(pagerank.keys()),
        'pagerank': list(pagerank.values()),
        'betweenness': list(betweenness.values())
    })

    df['pagerank_norm'] = (df['pagerank'] - df['pagerank'].min()) / (df['pagerank'].max() - df['pagerank'].min())
    df['betweenness_norm'] = (df['betweenness'] - df['betweenness'].min()) / (df['betweenness'].max() - df['betweenness'].min())

    pagerank_weight, betweenness_weight = weights
    df['average_index'] = (pagerank_weight * df['pagerank_norm']) + (betweenness_weight * df['betweenness_norm'])

    return df[['node_id', 'pagerank', 'betweenness', 'average_index']].sort_values('average_index', ascending=False)
