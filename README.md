### Scratch-wound assay is a simple, reproducible assay commonly used to measure basic cell migration parameters such as speed, persistence, and polarity.

Cells are grown to confluence and a thin "wound" introduced by scratching with a pipette tip. Cells at the wound edge polarise and migrate into the wound space [1].

Scratch assays are a notoriously tedious task since most of them are done by hand. Although some tools for automatic segmentation and area counting exist, they do not account for cancer cells that are left in the middle of a wound after scratch.

This repository contains code for a proposed Python-based segmentation solution that accounts for all cells and reduces measurement errorr.

The basic example included in this repository is a scratch assay done at Nazarbayev University. There are 10 images of the first 10 hours of an experiment.

To run the example code, type:

###### python analyseg.py

It will then output a graph with areas plotted against time.

The repository will be updated in the future to add new functionality and better performance.



#### Masks that are created during computations (1 & 2) and the original image (3):


#### Segmentation example:





###### References:

1. https://pubmed.ncbi.nlm.nih.gov/21748666/
