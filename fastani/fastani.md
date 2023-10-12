# FastANI
Summary of [FastANI](https://github.com/ParBLiSS/FastANI) results from project: `[{{ project().name }}]`

## Description
Fast Whole-Genome Similarity (ANI) Estimation

## Hierarchical Clustering based on ANI values


    
![png](fastani_files/fastani_5_0.png)
    


## Estimate Number of Clusters

    Estimated number of clusters: 7



    
![png](fastani_files/fastani_7_1.png)
    


## ANI Clustermap


    <Figure size 640x480 with 0 Axes>



    
![png](fastani_files/fastani_9_1.png)
    


## References
<font size="2">

- Herman Saffar, O. 2022. An Approach for Choosing Number of Clusters for K-Means. [www.medium.com](https://medium.com/towards-data-science/an-approach-for-choosing-number-of-clusters-for-k-means-c28e614ecb2c)

{% for i in project().rule_used['fastani']['references'] %}
- *{{ i }}*
{% endfor %}
</font>
