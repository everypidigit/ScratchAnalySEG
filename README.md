### Scratch-wound assay is a simple, reproducible assay commonly used to measure basic cell migration parameters such as speed, persistence, and polarity.

Cells are grown to confluence and a thin "wound" introduced by scratching with a pipette tip. Cells at the wound edge polarise and migrate into the wound space [1].

Scratch assays are a notoriously tedious task since most of them are done by hand. Although some tools for automatic segmentation and area counting exist, they do not account for cancer cells that are left in the middle of a wound after scratch.

This repository contains code for a proposed Python-based segmentation solution that accounts for all cells and reduces measurement errorr.

The basic example included in this repository is a scratch assay done at Nazarbayev University. There are 10 images of the first 10 hours of an experiment. 

To run the example code, type:

###### python analyseg.py

It will then output a graph with areas plotted against time. 


The repository will be updated in the future to add new functionality and better performance. 

##### Using image downscaling, followed by entropy and finding countours, we are able to capture as many cells as possible.

![alt text](https://github.com/everypidigit/ScratchAnalySEG/blob/main/Screenshot%202023-06-13%20at%2012.12.41.png)
![alt text](https://github.com/everypidigit/ScratchAnalySEG/blob/main/Screenshot%202023-06-13%20at%2012.12.48.png)

1. https://pubmed.ncbi.nlm.nih.gov/21748666/
