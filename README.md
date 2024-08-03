# Quantom-Tomography
This repository contains code for a TAU lab C experiment designed by students to process collected lab data. The repository is divided into multiple branches, each corresponding to a different part of the experiment.

## Branches Overview
- **Part 1**: Density matrices
- **Part 2**: Simulation
- **Part 3**: Bell's inequallity
-----
## Final3DPlotterSaraGarry.m

This matlab script reads a CSV containing the densoty matrix's data and genrates a 3D plot of it. The script than saves a .fig file from which a.jpg or a .png file can be saved manually shouldone want to. This file is located in the main directory as it is used for both part 1 and part 2 with only difference being the names of the matrices used and the script may need to be adjusted accordingly.

Description - The scripts performs the following steps

 1. Reads base (e.g. HHVV) and bit number from file name
 2. Reads density matrix from CSV file and Generates a 3D plot of it
 3. Saves the plot into a .fig file


Usage - 
 1. Ensure the relvant file is in the same directory as the matlab script
 2. Run the script so genrate and save the figure into a .fig file


-----
## Acknowledgements
  * TAU Lab C
