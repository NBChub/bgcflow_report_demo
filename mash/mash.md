# MASH
Summary of [MASH](https://github.com/marbl/Mash) results from project: `[{{ project().name }}]`

## Description
Fast genome and metagenome distance estimation using MinHash

## Hierarchical Clustering based on MASH distances


    
![png](mash_files/mash_5_0.png)
    


## Estimate Number of Clusters

    Estimated number of clusters: 8



    
![png](mash_files/mash_7_1.png)
    


## MASH Clustermap


    <Figure size 640x480 with 0 Axes>



    
![png](mash_files/mash_9_1.png)
    


## References
<font size="2">
{% for i in project().rule_used['mash']['references'] %}
- *{{ i }}*
{% endfor %}
</font>
