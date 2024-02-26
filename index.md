

# `{{ project().name }}`
Summary report for project `{{ project().name }}`. Generated using [**`BGCFlow v{{ project().bgcflow_version}}`**](https://github.com/NBChub/bgcflow){:target="_blank"}

## Project Description
- {{ project().description }}
- Sample size **{{ project().sample_size }}**


## Available reports
| BGCFlow_rules                                     | description                                                                                      |
|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [seqfu](seqfu/){.md-button}                       | Calculate sequence statistics using SeqFu.                                                       |
| [mash](mash/){.md-button}                         | Calculate distance estimation for all samples using MinHash.                                     |
| [fastani](fastani/){.md-button}                   | Do pairwise Average Nucleotide Identity (ANI) calculation across all samples.                    |
| [checkm](checkm/){.md-button}                     | Assess genome quality with CheckM.                                                               |
| [prokka-gbk](prokka-gbk/){.md-button}             | Copy annotated genbank results.                                                                  |
| [antismash](antismash/){.md-button}               | Summarizes antiSMASH result.                                                                     |
| [query-bigslice](query-bigslice/){.md-button}     | Map BGCs to BiG-FAM database (https://bigfam.bioinformatics.nl/)                                 |
| [bigscape](bigscape/){.md-button}                 | Cluster BGCs using BiG-SCAPE                                                                     |
| [bigslice](bigslice/){.md-button}                 | Cluster BGCs using BiG-SLiCE (https://github.com/medema-group/bigslice)                          |
| [automlst-wrapper](automlst-wrapper/){.md-button} | Simplified Tree building using [autoMLST](https://github.com/NBChub/automlst-simplified-wrapper) |
| [arts](arts/){.md-button}                         | Run Antibiotic Resistant Target Seeker (ARTS) on samples.                                        |
| [roary](roary/){.md-button}                       | Build pangenome using Roary.                                                                     |
| [eggnog-roary](eggnog-roary/){.md-button}         | Annotate Roary output using eggNOG mapper                                                        |
| [deeptfactor](deeptfactor/){.md-button}           | Use deep learning to find Transcription Factors.                                                 |
| [cblaster-genome](cblaster-genome/){.md-button}   | Build diamond database of genomes for cblaster search.                                           |
| [cblaster-bgc](cblaster-bgc/){.md-button}         | Build diamond database of BGCs for cblaster search.                                              |


## References
If you find BGCFlow useful, please cite:

<font size="2">

  - *Nuhamunada, M., B.O. Palsson, O. S. Mohite, and T. Weber. 2022. BGCFlow [Computer software]. GITHUB: [https://github.com/NBChub/bgcflow](https://github.com/NBChub/bgcflow)*

  - *Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V., Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S., Nahnsen, S., Köster, J., 2021. Sustainable data analysis with Snakemake. [F1000Res 10, 33](https://f1000research.com/articles/10-33/v1).*

  - *Nathan C Sheffield, Michał Stolarczyk, Vincent P Reuter, André F Rendeiro, Linking big biomedical datasets to modular analysis with Portable Encapsulated Projects, [GigaScience, Volume 10, Issue 12, December 2021, giab077](https://doi.org/10.1093/gigascience/giab077)*

</font>

Please also cite each tools used in the analysis:

<font size="2">
{% for i in project().references %}
  - *{{ i }}*
{% endfor %}
</font>
