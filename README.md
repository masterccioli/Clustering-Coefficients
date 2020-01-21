# Clustering Coefficients
 Faster implementation of getting average clustering coefficients

 This is a re-implementation of networkx.algorithms.cluster.clustering

 Because idiots insist on using inefficient data structures to represent networks

 implements Saramäki, J., Kivelä, M., Onnela, J.-P., Kaski, K., & Kertész, J. (2007). Generalizations of the clustering coefficient to weighted complex networks. Physical Review E, 75(2), 027105. https://doi.org/10.1103/PhysRevE.75.027105

## functions

### get_ave_clustering_coefficient
 Arguments: symmetrical distance matrix
 Returns: average clustering coefficient for network
 
### get_all_clustering_coefficients
 Arguments: symmetrical distance matrix
 Returns: list of clustering coefficients for each node in the network