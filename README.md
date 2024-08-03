# Quantom-Tomography
## Genral

This repository consists of a TAU lab C expiriment code created by students in order to process the data that was collected in the lab.
In this particalular brunch you can find the codes relvant for the part 3 i.e. bells inequality calculations. 
-----
## Plotter_Garry_for_part_c.m

This  matlab scripts reads video file of the expiriment and creat a csv file with the intensities read by each camera.

Description - The scripts performs the following steps
  1. Reads vidoe file
  2. Itrates over each frame and calcualte the intensity value for each camera
  3. Saves the data for each camera in csv file with name extructed from the video's name

Usage -
  1. Ensure file (e.g. +90+112.5.mp4) is in the same directory as the script
  2. Run script to generate CSV file with the data extructed

*Note -
It is assumed that each one of the videos files is named Angle1Angle2.mp4 with the sign of the angle (i.e. + or - while zero gets no sign). This is important as the python script assums the same format for the CVS files.
-----
## Bell_test_calculator.py

This python script reads the CSV files extructed using Plotter_Garry_for_part_c.m file that are located in the same folders calculate the bell inequality and its uncertentny and plots a grpah of the measured intensities from the files.

Description - The scripts performs the following steps
  1. Reads CSV with the angles names in directory
  2. Itrates over each file and identify simultaneous reads above the trushold 
  3. Calculate (all) N and E parameters
  4. Use E and N parameters to calculate S and it's uncertainty
  5. Plots the read data (plot needs to be saved manually)

Usage -
  1. Ensure all files (e.g. +90+112.5.csv etc...) are in the same directory as the script
  2. Run script to calculate S, it's uncertainty and generate plotted data

Dependencies - 
  * numpy
  * pandas
  * matplotlib
