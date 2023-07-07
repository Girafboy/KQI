# KQI

![GitHub](https://img.shields.io/github/license/girafboy/kqi)
![GitHub Repo stars](https://img.shields.io/github/stars/girafboy/kqi)
![GitHub issues](https://img.shields.io/github/issues/girafboy/kqi)

KQI (Knowledge Quantification Index) is the first metric to quantify knowledge from the perspective of information structurization.

This repository provides a python implementation of KQI, as well as data and code examples on an imcomplete tiny academic datasets.

More details on the design of KQI can be found in the paper: [Quantifying knowledge from the perspective of information structurization](https://doi.org/10.1371/journal.pone.0279314).

## System Requirements

### Hardware requirements

`KQI` package requires only a standard computer with enough RAM to support the in-memory operations.

### Software requirements

#### OS Requirements

This package can run on any operating system where python and its dependencies can be installed properly. The package has been tested on the *Ubuntu 18.04.4*.

#### Python Dependencies

```txt
python==3.8.10
igraph==0.9.8
pandas==1.1.3
tqdm==4.62.0
```

## Installation guide

### Install from Github

```bash
git clone https://github.com/Girafboy/KQI
cd KQI
pip install -r requirements.txt
```

- `sudo`, if required.
- The installation process may take a few minutes to complete, which depends on the network environment.

## Usage

### Demo

To run the example for calculating KQI, execute the code:

```bash
python3 kqi_example.py
```

Then, the program will read the data in *data_example.csv*, calculate KQI and output the file *result_example.csv*. This process may last a few seconds.

### Migrate to other tasks

Readers can refer to the sample code and sample data to calculate other tasks. Here's some instructions:

- *util/kqi.py*: KQI toolkit, including the self-implemented directed graph class `DiGraph`, on which all KQI calculations are based.
- *kqi_example.py*: KQI toolkit usage example, including the complete KQI computation process:
    1. create a graph.
    2. add nodes and edges.
    3. de-loop to form DAG. (not required if the graph is already DAG)
    4. set the current date and decay factor (1 is no decay, 0 is the maximum decay rate). (not required if time attenuation is not considered)
    5. call the function to calculate KQI node-by-node.
- *data_example.csv*: The example data contains four parts: `paperid` (required), `referenceids` (required), `date` (optional), and `title` (optional). `paperid` (int) should be a unique identifier for the paper. `referenceids` is the list of the reference ids of the paper. `date` is the publication date of the paper.

### Open publications dataset

If readers would like to reproduce our work, we also provide a full [publication dataset](https://zenodo.org/record/7878551). This dataset contains citation relationships, publication dates, and academic fields for 213,715,816 publications from 1800 to 2020. These publications cover 292 secondary subjects in 19 major disciplines, including Economics, Biology, Computer Science, Physics, and more. The data are requested from Shanghai Jiao Tong University [Acemap](https://www.acemap.info) and sourced from the last snapshot of Microsoft Academic Graph (MAG) as of December 31, 2021.

## Citation

Please use the following bibtex entry:

```bib
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
