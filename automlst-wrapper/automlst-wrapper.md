# autoMLST Wrapper
Summary of [autoMLST Wrapper](https://github.com/KatSteinke/automlst-simplified-wrapper) results from project: `[{{ project().name }}]`

## Description
This report provides an overview of the result from [autoMLST Wrapper](https://github.com/KatSteinke/automlst-simplified-wrapper), a modified version of [autoMLST](https://bitbucket.org/ziemertlab/automlst) tailored for simplified usability. By integrating a straightforward wrapper script, this fork eliminates the need for additional organism selection steps, streamlining the process for users.

## Visualization
The tree visualization represents the phylogenetic relationships between various strains of the genus. This visualization aids in understanding the genetic diversity and evolutionary history of these genomes.


    
![png](automlst-wrapper_files/automlst-wrapper_5_0.png)
    


[Download Tree](assets/data/final_corrected.newick){:target="_blank" .md-button}


<div class="itables">
<style>
.itables table td { font-style: italic; font-size: .8em;}
.itables table th { font-style: oblique; font-size: .8em; }
</style>
<table id="itables_31cb6e57_e130_4585_ad3a_56e688e8260c" class="display compact" data-quarto-disable-processing="true" style="table-layout:auto;width:auto;margin:auto;caption-side:bottom">
<thead>
    <tr style="text-align: right;">

      <th>genome_id</th>
      <th>genus_original</th>
      <th>species_original</th>
      <th>strain</th>
      <th>genus</th>
      <th>species</th>
    </tr>
  </thead><tbody><tr><td>Loading... (need <a href=https://mwouts.github.io/itables/troubleshooting.html>help</a>?)</td></tr></tbody>

</table>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
<script type="module">
    // Import jquery and DataTable
    import 'https://code.jquery.com/jquery-3.6.0.min.js';
    import dt from 'https://cdn.datatables.net/1.12.1/js/jquery.dataTables.mjs';
    dt($);

    $(document).ready(function () {
        document.querySelectorAll("#itables_31cb6e57_e130_4585_ad3a_56e688e8260c:not(.dataTable)").forEach(table => {
            // Define the table data
            const data = [["GCF_002564065.1", "Saccharopolyspora", "erythraea", "DSM 40517", "g__Saccharopolyspora_D", "erythraea"], ["GCF_022828475.1", "Saccharopolyspora", "gloriosae", "MLY014", "g__Saccharopolyspora_C", "NaN"], ["GCF_014203325.1", "Saccharopolyspora", "gloriosae", "DSM 45582", "g__Saccharopolyspora_C", "gloriosae"], ["GCF_024734405.1", "Saccharopolyspora", "gregorii", "BM8-3", "g__Saccharopolyspora_C", "NaN"], ["GCF_016526145.1", "Saccharopolyspora", "sp.", "HNM0986", "g__Saccharopolyspora_C", "sp016526145"], ["GCF_002846475.1", "Saccharopolyspora", "spinosa", "DSM 44228", "g__Saccharopolyspora", "spinosa"], ["GCF_000194155.1", "Saccharopolyspora", "spinosa", "NRRL 18395", "g__Saccharopolyspora", "spinosa"], ["GCF_014490055.1", "Saccharopolyspora", "spinosa", "CCTCC M206084", "g__Saccharopolyspora", "spinosa"], ["GCF_014697215.1", "Saccharopolyspora", "pogona", "NRRL30141", "g__Saccharopolyspora", "pogona"], ["GCF_012277335.1", "Saccharopolyspora", "sp.", "ASAGF58", "g__Saccharopolyspora", "pogona"], ["GCF_014203395.1", "Saccharopolyspora", "phatthalungensis", "DSM 45584", "g__Saccharopolyspora", "phatthalungensis"], ["GCF_013410345.1", "Saccharopolyspora", "hordei", "DSM 44065", "g__Saccharopolyspora", "hordei"], ["GCF_003635025.1", "Saccharopolyspora", "antimicrobica", "DSM 45119", "g__Saccharopolyspora", "antimicrobica"], ["GCF_900114905.1", "Saccharopolyspora", "antimicrobica", "CPCC 201259", "g__Saccharopolyspora", "antimicrobica"], ["GCF_900112555.1", "Saccharopolyspora", "kobensis", "CGMCC 4.3529", "g__Saccharopolyspora", "kobensis"], ["GCF_900108315.1", "Saccharopolyspora", "kobensis", "ATCC 20501", "g__Saccharopolyspora", "kobensis"], ["GCF_008630535.1", "Saccharopolyspora", "hirsuta", "VKM Ac-666", "g__Saccharopolyspora", "hirsuta"], ["GCF_018070075.1", "Saccharopolyspora", "endophytica", "KCTC 19397", "g__Saccharopolyspora", "endophytica"], ["GCF_003931915.1", "Saccharopolyspora", "rhizosphaerae", "H219", "g__Saccharopolyspora", "rhizosphaerae"], ["GCF_900116135.1", "Saccharopolyspora", "flava", "DSM 44771", "g__Saccharopolyspora", "flava"], ["GCF_007829955.1", "Saccharopolyspora", "dendranthemae", "DSM 46699", "g__Saccharopolyspora", "dendranthemae"], ["GCF_025643595.1", "Saccharopolyspora", "rosea", "A22", "g__Saccharopolyspora", "NaN"], ["GCF_018141105.1", "Saccharopolyspora", "erythraea", "SCSIO 07745", "g__Saccharopolyspora_D", "erythraea_A"], ["GCF_016859185.1", "Saccharopolyspora", "erythraea", "NRRL 23338", "g__Saccharopolyspora_D", "erythraea"], ["GCF_000062885.1", "Saccharopolyspora", "erythraea", "NRRL 2338", "g__Saccharopolyspora_D", "erythraea"], ["GCF_022392385.1", "Saccharopolyspora", "erythraea", "E3", "g__Saccharopolyspora_D", "erythraea"]];

            // Define the dt_args
            let dt_args = {"scrollX": true, "lengthMenu": [5, 10, 20, 50, 100, 200, 500], "order": []};
            dt_args["data"] = data;


            new $.fn.dataTable(table, dt_args);
        });
    });
</script>
</div>



[Download Table](assets/tables/automlst_tree_table.csv){:target="_blank" .md-button}

## Interactive Visualization with iTOL
For an enhanced, interactive visualization experience, users are encouraged to download the tree file and the corresponding metadata table. These files can be uploaded to [iTOL (Interactive Tree Of Life)](https://itol.embl.de/), a web-based tool for the display, manipulation, and annotation of phylogenetic trees.

## References
<font size="2">

- **G Yu**, DK Smith, H Zhu, Y Guan, TTY Lam<sup>\*</sup>. ggtree: an
    R package for visualization and annotation of phylogenetic trees
    with their covariates and other associated data. ***Methods in
    Ecology and Evolution***. 2017, 8(1):28-36. doi:
    [10.1111/2041-210X.12628](https://doi.org/10.1111/2041-210X.12628)

{% for i in project().rule_used['automlst-wrapper']['references'] %}
- *{{ i }}*
{% endfor %}
</font>
