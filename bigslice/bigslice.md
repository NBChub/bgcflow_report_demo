# BiG-SLICE
Summary of [BiG-SLICE](https://github.com/medema-group/bigslice) results from project: `[{{ project().name }}]` 

## Description
A highly scalable, user-interactive tool for the large scale analysis of Biosynthetic Gene Clusters data.

## Usage

You can start the BiG-SLICE flask app to view the clustering result.

Steps:


- Install the conda environment:

```bash
    conda install -f /data/matinnu/mq_saccharopolyspora/data/processed/mq_saccharopolyspora/docs/assets/envs/bigslice.yaml
```

- Run the app

```bash
    port='5001'
    conda run -n bigslice bash /data/matinnu/mq_saccharopolyspora/data/processed/mq_saccharopolyspora/cluster_as_7.1.0/start_server.sh $port
```



## References

<font size="2">

{% for i in project().rule_used['bigslice']['references'] %}
- *{{ i }}*
{% endfor %}

</font>
