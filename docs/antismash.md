# antiSMASH 
Summary of BGCs detected in each genome for: `[{{ project().name }}]`

## Description
> antiSMASH allows the rapid genome-wide identification, annotation and analysis of secondary metabolite biosynthesis gene clusters in bacterial and fungal genomes.

## Result Summary


AntiSMASH detected **735** BGCs from **26** genomes with the median of **25**. Out of these, **94.01%** are deemed as complete.


> Note: Here the incomplete BGCs are denoted by those that were identified to be on the contig edge by antiSMASH and thus are likely to be incomplete.





<style>
  #altair-viz-7e0fd7281fd7454d8423edd788695491.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-7e0fd7281fd7454d8423edd788695491.vega-embed details,
  #altair-viz-7e0fd7281fd7454d8423edd788695491.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-7e0fd7281fd7454d8423edd788695491"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-7e0fd7281fd7454d8423edd788695491") {
      outputDiv = document.getElementById("altair-viz-7e0fd7281fd7454d8423edd788695491");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm/vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm/vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm/vega-lite@5.15.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm/vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "5.15.1"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "data": {"name": "data-3f1ca1750db15a411338364e5677a133"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "GTDB genus", "type": "nominal"}, "tooltip": [{"field": "Genome ID", "type": "nominal"}, {"field": "GTDB species", "type": "nominal"}, {"field": "BGCs", "type": "quantitative"}, {"field": "Incomplete BGCs", "type": "quantitative"}], "x": {"axis": {"title": "BGCs"}, "bin": true, "field": "BGCs", "type": "quantitative"}, "y": {"aggregate": "count", "axis": {"title": "Genomes"}, "type": "quantitative"}}, "params": [{"name": "param_1", "select": {"type": "interval", "encodings": ["x", "y"]}, "bind": "scales"}], "$schema": "https://vega.github.io/schema/vega-lite/v5.15.1.json", "datasets": {"data-3f1ca1750db15a411338364e5677a133": [{"Genome ID": "GCF_003635025.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora antimicrobica", "Strain": null, "BGCs": 26.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_900114905.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora antimicrobica", "Strain": null, "BGCs": 25.0, "Incomplete BGCs": 7.0}, {"Genome ID": "GCF_007829955.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora dendranthemae", "Strain": null, "BGCs": 22.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_018070075.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora endophytica", "Strain": null, "BGCs": 26.0, "Incomplete BGCs": 7.0}, {"Genome ID": "GCF_016859185.1", "GTDB genus": "Saccharopolyspora_D", "GTDB species": "Saccharopolyspora_D erythraea", "Strain": null, "BGCs": 39.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_018141105.1", "GTDB genus": "Saccharopolyspora_D", "GTDB species": "Saccharopolyspora_D erythraea_A", "Strain": null, "BGCs": 36.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_022392385.1", "GTDB genus": "Saccharopolyspora_D", "GTDB species": "Saccharopolyspora_D erythraea", "Strain": null, "BGCs": 38.0, "Incomplete BGCs": 1.0}, {"Genome ID": "GCF_000062885.1", "GTDB genus": "Saccharopolyspora_D", "GTDB species": "Saccharopolyspora_D erythraea", "Strain": null, "BGCs": 38.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_002564065.1", "GTDB genus": "Saccharopolyspora_D", "GTDB species": "Saccharopolyspora_D erythraea", "Strain": null, "BGCs": 37.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_900116135.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora flava", "Strain": null, "BGCs": 19.0, "Incomplete BGCs": 4.0}, {"Genome ID": "GCF_014203325.1", "GTDB genus": "Saccharopolyspora_C", "GTDB species": "Saccharopolyspora_C gloriosae", "Strain": null, "BGCs": 24.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_022828475.1", "GTDB genus": "Saccharopolyspora_C", "GTDB species": "Saccharopolyspora_C sp.", "Strain": null, "BGCs": 25.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_024734405.1", "GTDB genus": "Saccharopolyspora_C", "GTDB species": "Saccharopolyspora_C sp.", "Strain": null, "BGCs": 24.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_008630535.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora hirsuta", "Strain": null, "BGCs": 22.0, "Incomplete BGCs": 7.0}, {"Genome ID": "GCF_013410345.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora hordei", "Strain": null, "BGCs": 13.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_900112555.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora jiangxiensis", "Strain": null, "BGCs": 23.0, "Incomplete BGCs": 4.0}, {"Genome ID": "GCF_900108315.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora jiangxiensis", "Strain": null, "BGCs": 24.0, "Incomplete BGCs": 1.0}, {"Genome ID": "GCF_014203395.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora phatthalungensis", "Strain": null, "BGCs": 37.0, "Incomplete BGCs": 1.0}, {"Genome ID": "GCF_014697215.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora pogona", "Strain": null, "BGCs": 38.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_003931915.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora rhizosphaerae", "Strain": null, "BGCs": 14.0, "Incomplete BGCs": 2.0}, {"Genome ID": "GCF_025643595.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora sp.", "Strain": null, "BGCs": 17.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_012277335.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora pogona", "Strain": null, "BGCs": 33.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_016526145.1", "GTDB genus": "Saccharopolyspora_C", "GTDB species": "Saccharopolyspora_C sp016526145", "Strain": null, "BGCs": 25.0, "Incomplete BGCs": 7.0}, {"Genome ID": "GCF_014490055.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora spinosa", "Strain": null, "BGCs": 37.0, "Incomplete BGCs": 1.0}, {"Genome ID": "GCF_002846475.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora spinosa", "Strain": null, "BGCs": 37.0, "Incomplete BGCs": 0.0}, {"Genome ID": "GCF_000194155.1", "GTDB genus": "Saccharopolyspora", "GTDB species": "Saccharopolyspora spinosa", "Strain": null, "BGCs": 36.0, "Incomplete BGCs": 2.0}]}}, {"mode": "vega-lite"});
</script>



## Summary Table
Click on the genome ids to get the antiSMASH result.

[Download Table]({{ project().file_server() }}/tables/df_antismash_{{project().dependency_version()}}_summary.csv){:target="_blank" .md-button}


<style>
.itables table td { font-style: italic; font-size: .8em;}
.itables table th { font-style: oblique; font-size: .8em; }
</style>
<div class="itables">
<table id="d1cd132c-ded5-4291-a401-a7afe9961345" class="display compact"style="table-layout:auto;width:auto;margin:auto;caption-side:bottom"><thead>
    <tr style="text-align: right;">

      <th>Genome ID</th>
      <th>GTDB genus</th>
      <th>GTDB species</th>
      <th>Strain</th>
      <th>BGCs</th>
      <th>Incomplete BGCs</th>
    </tr>
  </thead><tbody><tr><td>Loading... (need <a href=https://mwouts.github.io/itables/troubleshooting.html>help</a>?)</td></tr></tbody></table>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
<script type="module">
    // Import jquery and DataTable
    import 'https://code.jquery.com/jquery-3.6.0.min.js';
    import dt from 'https://cdn.datatables.net/1.12.1/js/jquery.dataTables.mjs';
    dt($);

    // Define the table data
    const data = [["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_003635025.1/index.html' target='_blank''>GCF_003635025.1</a>", "Saccharopolyspora", "Saccharopolyspora antimicrobica", NaN, 26.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_900114905.1/index.html' target='_blank''>GCF_900114905.1</a>", "Saccharopolyspora", "Saccharopolyspora antimicrobica", NaN, 25.0, 7.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_007829955.1/index.html' target='_blank''>GCF_007829955.1</a>", "Saccharopolyspora", "Saccharopolyspora dendranthemae", NaN, 22.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_018070075.1/index.html' target='_blank''>GCF_018070075.1</a>", "Saccharopolyspora", "Saccharopolyspora endophytica", NaN, 26.0, 7.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_016859185.1/index.html' target='_blank''>GCF_016859185.1</a>", "Saccharopolyspora_D", "Saccharopolyspora_D erythraea", NaN, 39.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_018141105.1/index.html' target='_blank''>GCF_018141105.1</a>", "Saccharopolyspora_D", "Saccharopolyspora_D erythraea_A", NaN, 36.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_022392385.1/index.html' target='_blank''>GCF_022392385.1</a>", "Saccharopolyspora_D", "Saccharopolyspora_D erythraea", NaN, 38.0, 1.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_000062885.1/index.html' target='_blank''>GCF_000062885.1</a>", "Saccharopolyspora_D", "Saccharopolyspora_D erythraea", NaN, 38.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_002564065.1/index.html' target='_blank''>GCF_002564065.1</a>", "Saccharopolyspora_D", "Saccharopolyspora_D erythraea", NaN, 37.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_900116135.1/index.html' target='_blank''>GCF_900116135.1</a>", "Saccharopolyspora", "Saccharopolyspora flava", NaN, 19.0, 4.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_014203325.1/index.html' target='_blank''>GCF_014203325.1</a>", "Saccharopolyspora_C", "Saccharopolyspora_C gloriosae", NaN, 24.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_022828475.1/index.html' target='_blank''>GCF_022828475.1</a>", "Saccharopolyspora_C", "Saccharopolyspora_C sp.", NaN, 25.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_024734405.1/index.html' target='_blank''>GCF_024734405.1</a>", "Saccharopolyspora_C", "Saccharopolyspora_C sp.", NaN, 24.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_008630535.1/index.html' target='_blank''>GCF_008630535.1</a>", "Saccharopolyspora", "Saccharopolyspora hirsuta", NaN, 22.0, 7.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_013410345.1/index.html' target='_blank''>GCF_013410345.1</a>", "Saccharopolyspora", "Saccharopolyspora hordei", NaN, 13.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_900112555.1/index.html' target='_blank''>GCF_900112555.1</a>", "Saccharopolyspora", "Saccharopolyspora jiangxiensis", NaN, 23.0, 4.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_900108315.1/index.html' target='_blank''>GCF_900108315.1</a>", "Saccharopolyspora", "Saccharopolyspora jiangxiensis", NaN, 24.0, 1.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_014203395.1/index.html' target='_blank''>GCF_014203395.1</a>", "Saccharopolyspora", "Saccharopolyspora phatthalungensis", NaN, 37.0, 1.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_014697215.1/index.html' target='_blank''>GCF_014697215.1</a>", "Saccharopolyspora", "Saccharopolyspora pogona", NaN, 38.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_003931915.1/index.html' target='_blank''>GCF_003931915.1</a>", "Saccharopolyspora", "Saccharopolyspora rhizosphaerae", NaN, 14.0, 2.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_025643595.1/index.html' target='_blank''>GCF_025643595.1</a>", "Saccharopolyspora", "Saccharopolyspora sp.", NaN, 17.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_012277335.1/index.html' target='_blank''>GCF_012277335.1</a>", "Saccharopolyspora", "Saccharopolyspora pogona", NaN, 33.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_016526145.1/index.html' target='_blank''>GCF_016526145.1</a>", "Saccharopolyspora_C", "Saccharopolyspora_C sp016526145", NaN, 25.0, 7.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_014490055.1/index.html' target='_blank''>GCF_014490055.1</a>", "Saccharopolyspora", "Saccharopolyspora spinosa", NaN, 37.0, 1.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_002846475.1/index.html' target='_blank''>GCF_002846475.1</a>", "Saccharopolyspora", "Saccharopolyspora spinosa", NaN, 37.0, 0.0], ["<a href='{{ project().file_server() }}/antismash/{{project().dependency_version()}}/GCF_000194155.1/index.html' target='_blank''>GCF_000194155.1</a>", "Saccharopolyspora", "Saccharopolyspora spinosa", NaN, 36.0, 2.0]];

    // Define the dt_args
    let dt_args = {"columnDefs": [{"className": "dt-center", "targets": "_all"}], "lengthMenu": [5, 10, 20, 50, 100, 200, 500], "order": []};
    dt_args["data"] = data;

    $(document).ready(function () {

        $('#d1cd132c-ded5-4291-a401-a7afe9961345').DataTable(dt_args);
    });
</script>
</div>



## References
<font size="2">
{% for i in project().rule_used['antismash']['references'] %}
- {{ i }} 
{% endfor %}
</font>
