# cblaster-bgc
Summary of [cblaster-bgc](link) results from project: `[{{ project().name }}]` 

## Description
Build a diamond database of all BGCs in the project for clustered hits from a BLAST search using cblaster.

## How to run query from local database
* Download all files from the CBlaster result:

[CBlaster database]({{ project().file_server() }}/cblaster/bgc){:target="_blank" .md-button}

* Install CBlaster conda environment using this yaml configuration (create a file called `env.yaml` and copy paste the following items to the file). See the conda guide [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file):
```yaml
name: cblaster
channels:
  - conda-forge
  - default
  - bioconda
dependencies:
  - diamond==2.0.15
  - pip
  - pip:
    - cblaster==1.3.12
```
* After having the environment installed, `cd` to the directory containing all the files, activate the environment, and run queries by:
```bash
# activate environment
conda activate cblaster
cblaster search -m local -db cblaster_genome_db.dmnd -qf <query.faa>
```
* See CBlaster guide for running local queries [here](https://cblaster.readthedocs.io/en/latest/guide/search_module.html#searches-against-local-sequence-data)

## References

<font size="2">

{% for i in project().rule_used['cblaster-bgc']['references'] %}
- *{{ i }}*
{% endfor %}

</font>
