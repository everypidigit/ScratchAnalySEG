# Different ways to segment scratch assay images to count the area that cancer cells cover with time

### The scratch-wound assay is a simple, reproducible assay commonly used to measure basic cell migration parameters such as speed, persistence, and polarity. 
Cells are grown to confluence and a thin "wound" introduced by scratching with a pipette tip. Cells at the wound edge polarise and migrate into the wound space [1].

Scratch assays are a notoriously tedious task since most of them are done by hand. Although some tools for automatic segmentation and area counting exist, they do not account for cancer cells that are left in the middle of a wound after scratch. 

We propose a Python-based segmentation solution that accounts for all cells and reduces measurement error.

#### Using image downscaling, followed by entropy and finding countours, we are able to capture as many cells as possible.


1. https://pubmed.ncbi.nlm.nih.gov/21748666/
