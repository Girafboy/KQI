# Introduction

KQI (Knowledge Quantification Index) is the first metric to quantify knowledge from the perspective of information structurization.

This repository provides a python implementation of KQI, as well as data and code examples on an imcomplete tiny academic datasets.

More details on the design of KQI can be found in the paper: [Quantifying knowledge from the perspective of information structurization](https://doi.org/10.1371/journal.pone.0279314).


# Requirements

```
python==3.8.10
igraph==0.9.8
pandas==1.1.3
tqdm==4.62.0
```

# Usage

To run the example for calculating KQI, execute the code:
```
python3 kqi_example.py
```
Then, the program will read the data in *data_example.csv*, calculate KQI and output the file *result_example.csv*.

Readers can refer to the sample code and sample data to calculate other tasks. Here's some instructions:

- *util/kqi.py*: KQI toolkit, including the self-implemented directed graph class `DiGraph`, on which all KQI calculations are based.
- *kqi_example.py*: KQI toolkit usage example, including the complete KQI computation process:
    1. create a graph.
    2. add nodes and edges.
    3. de-loop to form DAG.
    4. set the current date and decay factor (1 is no decay, 0 is the maximum decay rate).
    5. call the function to calculate KQI node-by-node.
- *data_example.csv*: The example data contains four parts: `paperid` (required), `referenceids` (required), `date` (required), and `title` (optional). `paperid` (int) should be a unique identifier for the paper. `referenceids` is the list of the reference ids of the paper. `date` is the publication date of the paper.

# Citation

Please use the following bibtex entry:
```
@article{10.1371/journal.pone.0279314,
    doi = {10.1371/journal.pone.0279314},
    author = {Wang, Xinbing AND Kang, Huquan AND Fu, Luoyi AND Yao, Ling AND Ding, Jiaxin AND Wang, Jianghao AND Gan, Xiaoying AND Zhou, Chenghu AND Hopcroft, John E.},
    journal = {PLOS ONE},
    publisher = {Public Library of Science},
    title = {Quantifying knowledge from the perspective of information structurization},
    year = {2023},
    month = {01},
    volume = {18},
    url = {https://doi.org/10.1371/journal.pone.0279314},
    pages = {1-16},
    number = {1},
}
```
