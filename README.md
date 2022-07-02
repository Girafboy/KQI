# Introduction

KQI (Knowledge Quantification Index) is the first metric to quantify knowledge from the perspective of information structurization.

This repository provides a python implementation of KQI, as well as data and code examples on an imcomplete tiny academic datasets.

More details on the design of KQI can be found in the paper: [Exploring the Disproportion Between Scientific Productivity and Knowledge Amount](https://arxiv.org/abs/2106.02989).


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
@article{fu2021exploring,
  title={Exploring the Disproportion Between Scientific Productivity and Knowledge Amount},
  author={Fu, Luoyi and Kang, Huquan and Wang, Jianghao and Yao, Ling and Wang, Xinbing and Zhou, Chenghu},
  journal={arXiv preprint arXiv:2106.02989},
  year={2021}
}
```