# Annotated genomes
List of annotated genomes from: `[{{ project().name }}]` 

## Description
Summary table of annotated genbank files from each genomes.


<div class="itables">
<style>
.itables table td { font-style: italic; font-size: .8em;}
.itables table th { font-style: oblique; font-size: .8em; }
</style>
<table id="itables_8cde4455_2afc_4447_965a_86c6eca55b7a" class="display compact" data-quarto-disable-processing="true" style="table-layout:auto;width:auto;margin:auto;caption-side:bottom">
<thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contigs</th>
      <th>bases</th>
      <th>CDS</th>
      <th>rRNA</th>
      <th>repeat_region</th>
      <th>tRNA</th>
      <th>tmRNA</th>
      <th>gbk file</th>
      <th>CDS table</th>
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
        document.querySelectorAll("#itables_8cde4455_2afc_4447_965a_86c6eca55b7a:not(.dataTable)").forEach(table => {
            // Define the table data
            const data = [["GCF_000062885.1", 1, 8212805, 7279, 12, 3.0, 71, 1, "<a href='{{ project().file_server() }}/genbank/GCF_000062885.1.gbk' target='_blank''>GCF_000062885.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_000062885.1.tsv' target='_blank''>GCF_000062885.1.tsv</a>"], ["GCF_000194155.1", 22, 8581920, 8215, 4, 2.0, 61, 1, "<a href='{{ project().file_server() }}/genbank/GCF_000194155.1.gbk' target='_blank''>GCF_000194155.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_000194155.1.tsv' target='_blank''>GCF_000194155.1.tsv</a>"], ["GCF_002564065.1", 1, 8230103, 7307, 12, 3.0, 71, 1, "<a href='{{ project().file_server() }}/genbank/GCF_002564065.1.gbk' target='_blank''>GCF_002564065.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_002564065.1.tsv' target='_blank''>GCF_002564065.1.tsv</a>"], ["GCF_002846475.1", 1, 9020646, 8026, 16, 2.0, 61, 1, "<a href='{{ project().file_server() }}/genbank/GCF_002846475.1.gbk' target='_blank''>GCF_002846475.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_002846475.1.tsv' target='_blank''>GCF_002846475.1.tsv</a>"], ["GCF_003635025.1", 2, 8266186, 7657, 16, NaN, 68, 1, "<a href='{{ project().file_server() }}/genbank/GCF_003635025.1.gbk' target='_blank''>GCF_003635025.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_003635025.1.tsv' target='_blank''>GCF_003635025.1.tsv</a>"], ["GCF_003931915.1", 35, 5824618, 5344, 3, 1.0, 56, 1, "<a href='{{ project().file_server() }}/genbank/GCF_003931915.1.gbk' target='_blank''>GCF_003931915.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_003931915.1.tsv' target='_blank''>GCF_003931915.1.tsv</a>"], ["GCF_007829955.1", 8, 6410624, 5780, 12, NaN, 60, 1, "<a href='{{ project().file_server() }}/genbank/GCF_007829955.1.gbk' target='_blank''>GCF_007829955.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_007829955.1.tsv' target='_blank''>GCF_007829955.1.tsv</a>"], ["GCF_008630535.1", 46, 7549392, 6807, 8, 2.0, 69, 1, "<a href='{{ project().file_server() }}/genbank/GCF_008630535.1.gbk' target='_blank''>GCF_008630535.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_008630535.1.tsv' target='_blank''>GCF_008630535.1.tsv</a>"], ["GCF_012277335.1", 1, 8045912, 7501, 15, NaN, 60, 1, "<a href='{{ project().file_server() }}/genbank/GCF_012277335.1.gbk' target='_blank''>GCF_012277335.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_012277335.1.tsv' target='_blank''>GCF_012277335.1.tsv</a>"], ["GCF_013410345.1", 1, 5783988, 5266, 15, 3.0, 68, 1, "<a href='{{ project().file_server() }}/genbank/GCF_013410345.1.gbk' target='_blank''>GCF_013410345.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_013410345.1.tsv' target='_blank''>GCF_013410345.1.tsv</a>"], ["GCF_014203325.1", 1, 6825909, 5928, 12, 4.0, 70, 1, "<a href='{{ project().file_server() }}/genbank/GCF_014203325.1.gbk' target='_blank''>GCF_014203325.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_014203325.1.tsv' target='_blank''>GCF_014203325.1.tsv</a>"], ["GCF_014203395.1", 6, 8541735, 7467, 12, 3.0, 61, 1, "<a href='{{ project().file_server() }}/genbank/GCF_014203395.1.gbk' target='_blank''>GCF_014203395.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_014203395.1.tsv' target='_blank''>GCF_014203395.1.tsv</a>"], ["GCF_014490055.1", 1, 8876435, 8026, 15, 2.0, 62, 1, "<a href='{{ project().file_server() }}/genbank/GCF_014490055.1.gbk' target='_blank''>GCF_014490055.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_014490055.1.tsv' target='_blank''>GCF_014490055.1.tsv</a>"], ["GCF_014697215.1", 3, 9608180, 9215, 15, 1.0, 59, 1, "<a href='{{ project().file_server() }}/genbank/GCF_014697215.1.gbk' target='_blank''>GCF_014697215.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_014697215.1.tsv' target='_blank''>GCF_014697215.1.tsv</a>"], ["GCF_016526145.1", 34, 6397171, 5807, 5, 3.0, 57, 1, "<a href='{{ project().file_server() }}/genbank/GCF_016526145.1.gbk' target='_blank''>GCF_016526145.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_016526145.1.tsv' target='_blank''>GCF_016526145.1.tsv</a>"], ["GCF_016859185.1", 1, 8305652, 7407, 12, 3.0, 70, 1, "<a href='{{ project().file_server() }}/genbank/GCF_016859185.1.gbk' target='_blank''>GCF_016859185.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_016859185.1.tsv' target='_blank''>GCF_016859185.1.tsv</a>"], ["GCF_018070075.1", 34, 7167017, 6628, 6, 7.0, 63, 1, "<a href='{{ project().file_server() }}/genbank/GCF_018070075.1.gbk' target='_blank''>GCF_018070075.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_018070075.1.tsv' target='_blank''>GCF_018070075.1.tsv</a>"], ["GCF_018141105.1", 1, 8243897, 7432, 12, 1.0, 58, 1, "<a href='{{ project().file_server() }}/genbank/GCF_018141105.1.gbk' target='_blank''>GCF_018141105.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_018141105.1.tsv' target='_blank''>GCF_018141105.1.tsv</a>"], ["GCF_022392385.1", 2, 8181083, 7263, 5, 3.0, 70, 1, "<a href='{{ project().file_server() }}/genbank/GCF_022392385.1.gbk' target='_blank''>GCF_022392385.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_022392385.1.tsv' target='_blank''>GCF_022392385.1.tsv</a>"], ["GCF_022828475.1", 1, 6878695, 6056, 12, 5.0, 67, 1, "<a href='{{ project().file_server() }}/genbank/GCF_022828475.1.gbk' target='_blank''>GCF_022828475.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_022828475.1.tsv' target='_blank''>GCF_022828475.1.tsv</a>"], ["GCF_024734405.1", 1, 6344421, 5540, 12, 4.0, 69, 1, "<a href='{{ project().file_server() }}/genbank/GCF_024734405.1.gbk' target='_blank''>GCF_024734405.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_024734405.1.tsv' target='_blank''>GCF_024734405.1.tsv</a>"], ["GCF_025643595.1", 1, 6562638, 6032, 12, 3.0, 66, 1, "<a href='{{ project().file_server() }}/genbank/GCF_025643595.1.gbk' target='_blank''>GCF_025643595.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_025643595.1.tsv' target='_blank''>GCF_025643595.1.tsv</a>"], ["GCF_900108315.1", 27, 7744048, 7169, 7, 1.0, 66, 1, "<a href='{{ project().file_server() }}/genbank/GCF_900108315.1.gbk' target='_blank''>GCF_900108315.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_900108315.1.tsv' target='_blank''>GCF_900108315.1.tsv</a>"], ["GCF_900112555.1", 28, 7777251, 7245, 6, 1.0, 66, 1, "<a href='{{ project().file_server() }}/genbank/GCF_900112555.1.gbk' target='_blank''>GCF_900112555.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_900112555.1.tsv' target='_blank''>GCF_900112555.1.tsv</a>"], ["GCF_900114905.1", 43, 8219321, 7645, 7, NaN, 68, 1, "<a href='{{ project().file_server() }}/genbank/GCF_900114905.1.gbk' target='_blank''>GCF_900114905.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_900114905.1.tsv' target='_blank''>GCF_900114905.1.tsv</a>"], ["GCF_900116135.1", 22, 6291299, 5626, 5, 5.0, 65, 1, "<a href='{{ project().file_server() }}/genbank/GCF_900116135.1.gbk' target='_blank''>GCF_900116135.1.gbk</a>", "<a href='{{ project().file_server() }}/genbank/GCF_900116135.1.tsv' target='_blank''>GCF_900116135.1.tsv</a>"]];

            // Define the dt_args
            let dt_args = {"columnDefs": [{"className": "dt-center", "targets": "_all"}], "lengthMenu": [5, 10, 20, 50, 100, 200, 500], "order": []};
            dt_args["data"] = data;


            new $.fn.dataTable(table, dt_args);
        });
    });
</script>
</div>



## Summary Statistics





<style>
  #altair-viz-0f118805e4ef4729a92d3a5c992af7be.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-0f118805e4ef4729a92d3a5c992af7be.vega-embed details,
  #altair-viz-0f118805e4ef4729a92d3a5c992af7be.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-0f118805e4ef4729a92d3a5c992af7be"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-0f118805e4ef4729a92d3a5c992af7be") {
      outputDiv = document.getElementById("altair-viz-0f118805e4ef4729a92d3a5c992af7be");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm/vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm/vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm/vega-lite@5.16.3?noext",
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
        .then(() => maybeLoadScript("vega-lite", "5.16.3"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "hconcat": [{"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#66c2a5"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "contigs", "scale": {"domain": [-3.5, 50.5]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "contigs", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#fc8d62"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "bases", "scale": {"domain": [5401568.8, 9990599.2]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "bases", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#8da0cb"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "CDS", "scale": {"domain": [4871.1, 9609.9]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "CDS", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#e78ac3"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "rRNA", "scale": {"domain": [1.7, 17.3]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "rRNA", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#a6d854"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "repeat_region", "scale": {"domain": [0.3999999999999999, 7.6]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "repeat_region", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#ffd92f"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "tRNA", "scale": {"domain": [54.5, 72.5]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "tRNA", "width": 100}, {"mark": {"type": "boxplot", "median": {"color": "black"}, "size": 50}, "encoding": {"color": {"value": "#e5c494"}, "opacity": {"value": 0.7}, "x": {"axis": null, "field": "dataset", "type": "nominal"}, "y": {"field": "tmRNA", "scale": {"domain": [1.0, 1.0]}, "title": null, "type": "quantitative"}}, "height": 150, "title": "tmRNA", "width": 100}], "data": {"name": "data-47db1bf7df20faa2260bff4800cabf33"}, "$schema": "https://vega.github.io/schema/vega-lite/v5.16.3.json", "datasets": {"data-47db1bf7df20faa2260bff4800cabf33": [{"contigs": 1, "bases": 8212805, "CDS": 7279, "rRNA": 12, "repeat_region": 3.0, "tRNA": 71, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_000062885.1.gbk' target='_blank''>GCF_000062885.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_000062885.1.tsv' target='_blank''>GCF_000062885.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 22, "bases": 8581920, "CDS": 8215, "rRNA": 4, "repeat_region": 2.0, "tRNA": 61, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_000194155.1.gbk' target='_blank''>GCF_000194155.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_000194155.1.tsv' target='_blank''>GCF_000194155.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 8230103, "CDS": 7307, "rRNA": 12, "repeat_region": 3.0, "tRNA": 71, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_002564065.1.gbk' target='_blank''>GCF_002564065.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_002564065.1.tsv' target='_blank''>GCF_002564065.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 9020646, "CDS": 8026, "rRNA": 16, "repeat_region": 2.0, "tRNA": 61, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_002846475.1.gbk' target='_blank''>GCF_002846475.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_002846475.1.tsv' target='_blank''>GCF_002846475.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 2, "bases": 8266186, "CDS": 7657, "rRNA": 16, "repeat_region": null, "tRNA": 68, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_003635025.1.gbk' target='_blank''>GCF_003635025.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_003635025.1.tsv' target='_blank''>GCF_003635025.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 35, "bases": 5824618, "CDS": 5344, "rRNA": 3, "repeat_region": 1.0, "tRNA": 56, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_003931915.1.gbk' target='_blank''>GCF_003931915.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_003931915.1.tsv' target='_blank''>GCF_003931915.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 8, "bases": 6410624, "CDS": 5780, "rRNA": 12, "repeat_region": null, "tRNA": 60, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_007829955.1.gbk' target='_blank''>GCF_007829955.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_007829955.1.tsv' target='_blank''>GCF_007829955.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 46, "bases": 7549392, "CDS": 6807, "rRNA": 8, "repeat_region": 2.0, "tRNA": 69, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_008630535.1.gbk' target='_blank''>GCF_008630535.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_008630535.1.tsv' target='_blank''>GCF_008630535.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 8045912, "CDS": 7501, "rRNA": 15, "repeat_region": null, "tRNA": 60, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_012277335.1.gbk' target='_blank''>GCF_012277335.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_012277335.1.tsv' target='_blank''>GCF_012277335.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 5783988, "CDS": 5266, "rRNA": 15, "repeat_region": 3.0, "tRNA": 68, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_013410345.1.gbk' target='_blank''>GCF_013410345.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_013410345.1.tsv' target='_blank''>GCF_013410345.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 6825909, "CDS": 5928, "rRNA": 12, "repeat_region": 4.0, "tRNA": 70, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_014203325.1.gbk' target='_blank''>GCF_014203325.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_014203325.1.tsv' target='_blank''>GCF_014203325.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 6, "bases": 8541735, "CDS": 7467, "rRNA": 12, "repeat_region": 3.0, "tRNA": 61, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_014203395.1.gbk' target='_blank''>GCF_014203395.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_014203395.1.tsv' target='_blank''>GCF_014203395.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 8876435, "CDS": 8026, "rRNA": 15, "repeat_region": 2.0, "tRNA": 62, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_014490055.1.gbk' target='_blank''>GCF_014490055.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_014490055.1.tsv' target='_blank''>GCF_014490055.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 3, "bases": 9608180, "CDS": 9215, "rRNA": 15, "repeat_region": 1.0, "tRNA": 59, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_014697215.1.gbk' target='_blank''>GCF_014697215.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_014697215.1.tsv' target='_blank''>GCF_014697215.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 34, "bases": 6397171, "CDS": 5807, "rRNA": 5, "repeat_region": 3.0, "tRNA": 57, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_016526145.1.gbk' target='_blank''>GCF_016526145.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_016526145.1.tsv' target='_blank''>GCF_016526145.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 8305652, "CDS": 7407, "rRNA": 12, "repeat_region": 3.0, "tRNA": 70, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_016859185.1.gbk' target='_blank''>GCF_016859185.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_016859185.1.tsv' target='_blank''>GCF_016859185.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 34, "bases": 7167017, "CDS": 6628, "rRNA": 6, "repeat_region": 7.0, "tRNA": 63, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_018070075.1.gbk' target='_blank''>GCF_018070075.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_018070075.1.tsv' target='_blank''>GCF_018070075.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 8243897, "CDS": 7432, "rRNA": 12, "repeat_region": 1.0, "tRNA": 58, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_018141105.1.gbk' target='_blank''>GCF_018141105.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_018141105.1.tsv' target='_blank''>GCF_018141105.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 2, "bases": 8181083, "CDS": 7263, "rRNA": 5, "repeat_region": 3.0, "tRNA": 70, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_022392385.1.gbk' target='_blank''>GCF_022392385.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_022392385.1.tsv' target='_blank''>GCF_022392385.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 6878695, "CDS": 6056, "rRNA": 12, "repeat_region": 5.0, "tRNA": 67, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_022828475.1.gbk' target='_blank''>GCF_022828475.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_022828475.1.tsv' target='_blank''>GCF_022828475.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 6344421, "CDS": 5540, "rRNA": 12, "repeat_region": 4.0, "tRNA": 69, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_024734405.1.gbk' target='_blank''>GCF_024734405.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_024734405.1.tsv' target='_blank''>GCF_024734405.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 1, "bases": 6562638, "CDS": 6032, "rRNA": 12, "repeat_region": 3.0, "tRNA": 66, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_025643595.1.gbk' target='_blank''>GCF_025643595.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_025643595.1.tsv' target='_blank''>GCF_025643595.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 27, "bases": 7744048, "CDS": 7169, "rRNA": 7, "repeat_region": 1.0, "tRNA": 66, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_900108315.1.gbk' target='_blank''>GCF_900108315.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_900108315.1.tsv' target='_blank''>GCF_900108315.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 28, "bases": 7777251, "CDS": 7245, "rRNA": 6, "repeat_region": 1.0, "tRNA": 66, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_900112555.1.gbk' target='_blank''>GCF_900112555.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_900112555.1.tsv' target='_blank''>GCF_900112555.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 43, "bases": 8219321, "CDS": 7645, "rRNA": 7, "repeat_region": null, "tRNA": 68, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_900114905.1.gbk' target='_blank''>GCF_900114905.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_900114905.1.tsv' target='_blank''>GCF_900114905.1.tsv</a>", "dataset": "mq_saccharopolyspora"}, {"contigs": 22, "bases": 6291299, "CDS": 5626, "rRNA": 5, "repeat_region": 5.0, "tRNA": 65, "tmRNA": 1, "gbk file": "<a href='{{ project().file_server() }}/genbank/GCF_900116135.1.gbk' target='_blank''>GCF_900116135.1.gbk</a>", "CDS table": "<a href='{{ project().file_server() }}/genbank/GCF_900116135.1.tsv' target='_blank''>GCF_900116135.1.tsv</a>", "dataset": "mq_saccharopolyspora"}]}}, {"mode": "vega-lite"});
</script>



## References

<font size="2">

{% for i in project().rule_used['prokka-gbk']['references'] %}
- *{{ i }}*
{% endfor %}

</font>
